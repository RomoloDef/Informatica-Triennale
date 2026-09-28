package api

import (
	"encoding/json"
	"errors"
	"io"
	"net/http"
	"os"
	"path/filepath"
	"strconv"
	"strings"

	"github.com/RomoloDef/WASAText/service/api/reqcontext"
	"github.com/RomoloDef/WASAText/service/database"
	"github.com/RomoloDef/WASAText/service/model"
	"github.com/julienschmidt/httprouter"
)

// createConversation gestisce la POST /chats per la creazione di chat individuali o di gruppo.
func (rt *_router) createConversation(w http.ResponseWriter, r *http.Request, ps httprouter.Params, ctx reqcontext.RequestContext) {
	// FASE 1: Decodifica Richiesta
	var req model.CreateChatRequest
	if err := json.NewDecoder(r.Body).Decode(&req); err != nil {
		ctx.Logger.WithError(err).Error("error decoding request body")
		rt.encodeResponse(w, model.ErrorResponse{Code: "400", Message: "Invalid request body"}, http.StatusBadRequest)
		return
	}

	// FASE 2: Validazione e Pre-elaborazione dei Partecipanti
	creatorID := ctx.UserID

	// 1. Usa una mappa per garantire l'unicità dei partecipanti e l'aggiunta del creatore
	uniqueParticipants := make(map[int]bool)

	// Aggiungi i partecipanti esterni (dal body JSON)
	for _, id := range req.ParticipantsIDs {
		if id <= 0 {
			rt.encodeResponse(w, model.ErrorResponse{Code: "400", Message: "Invalid participant ID provided."}, http.StatusBadRequest)
			return
		}
		uniqueParticipants[id] = true
	}

	// 2. Aggiungo il creatore (garantendo che sia presente)
	uniqueParticipants[creatorID] = true

	// 3. Riconversione in slice per la chiamata al DB
	req.ParticipantsIDs = make([]int, 0, len(uniqueParticipants))
	for id := range uniqueParticipants {
		req.ParticipantsIDs = append(req.ParticipantsIDs, id)
	}

	// Conto finale dei partecipanti unici
	finalCount := len(req.ParticipantsIDs)

	// 4. Validazione specifica per tipo di chat
	if req.Type == "individual" {

		// CONDIZIONE DI SUCCESSO: Devono esserci esattamente 2 partecipanti totali (Creatore + 1)
		if finalCount != 2 {
			ctx.Logger.Warnf("Invalid number of participants for individual chat: %d", finalCount)
			rt.encodeResponse(w, model.ErrorResponse{Code: "400", Message: "An individual chat must have exactly 2 unique participants (including yourself)."}, http.StatusBadRequest)
			return
		}
		if req.GroupName != "" {
			rt.encodeResponse(w, model.ErrorResponse{Code: "400", Message: "GroupName should not be specified for an individual chat."}, http.StatusBadRequest)
			return
		}

	} else if req.Type == "group" {

		// CONDIZIONE DI SUCCESSO: Devono esserci almeno 3 partecipanti totali (Creatore + 2)
		if finalCount < 3 {
			ctx.Logger.Warnf("Invalid number of participants for group chat: %d", finalCount)
			rt.encodeResponse(w, model.ErrorResponse{Code: "400", Message: "A group chat must have at least 3 unique participants (including yourself)."}, http.StatusBadRequest)
			return
		}
		// Utilizzo strings.TrimSpace per assicurarmi che il nome del gruppo
		// contenga caratteri validi e non sia composto solo da spazi vuoti (whitespace).
		req.GroupName = strings.TrimSpace(req.GroupName)
		if req.GroupName == "" {
			rt.encodeResponse(w, model.ErrorResponse{Code: "400", Message: "GroupName is required for a group chat."}, http.StatusBadRequest)
			return
		}

		if len(req.GroupIcon) > 2048 {
			rt.encodeResponse(w, model.ErrorResponse{Code: "400", Message: "Group photo URL is too long."}, http.StatusBadRequest)
			return
		}

	} else {
		rt.encodeResponse(w, model.ErrorResponse{Code: "400", Message: "Invalid chat type. Must be 'individual' or 'group'."}, http.StatusBadRequest)
		return
	}

	// FASE 3: Chiamata al Database
	newChat, err := rt.db.CreateConversation(creatorID, req)

	if err != nil {
		if errors.Is(err, database.ErrInvalidParticipant) {
			rt.encodeResponse(w, model.ErrorResponse{Code: "400", Message: "One or more participant IDs are invalid or do not exist."}, http.StatusBadRequest)
			return
		}

		// Restituiamo invece la chat esistente con un 200 OK.
		if errors.Is(err, database.ErrChatExists) {
			ctx.Logger.WithField("chat_id", newChat.ID).Info("Chat already exists, returning existing one.")
			// newChat contiene già l'ID della chat esistente (restituito dal db)
			rt.encodeResponse(w, newChat, http.StatusOK)
			return
		}

		// Errore generico (Internal Server Error)
		ctx.Logger.WithError(err).Error("error creating conversation in DB")
		rt.encodeResponse(w, model.ErrorResponse{Code: "500", Message: "Internal server error"}, http.StatusInternalServerError)
		return
	}

	// FASE 4: Risposta (201 Created)
	ctx.Logger.WithField("chat_id", newChat.ID).Infof("New conversation created: %s", req.Type)
	rt.encodeResponse(w, newChat, http.StatusCreated)
}

// getMyConversations gestisce la GET /chats
func (rt *_router) getMyConversations(w http.ResponseWriter, r *http.Request, ps httprouter.Params, ctx reqcontext.RequestContext) {
	// L'ID utente arriva dal token (popolato grazie a authWrap)
	userID := ctx.UserID

	// Recupera le chat dal DB
	chats, err := rt.db.GetMyConversations(userID)
	if err != nil {
		ctx.Logger.WithError(err).Error("error fetching user conversations")
		rt.encodeResponse(w, model.ErrorResponse{Code: "500", Message: "Internal server error"}, http.StatusInternalServerError)
		return
	}

	// Se non ci sono chat, restituisce un array vuoto invece di null
	if chats == nil {
		chats = []model.Chat{}
	}

	// Risposta 200 OK
	rt.encodeResponse(w, chats, http.StatusOK)
}

// getConversation gestisce la GET /chats/{chat_id}
func (rt *_router) getConversation(w http.ResponseWriter, r *http.Request, ps httprouter.Params, ctx reqcontext.RequestContext) {
	// Estraggo e faccio la validazione dell'ID tramite il costrutto strconv.Atoi che prende la stringa "chat_id" dai parametri dell'URL e la converte in un intero.
	// Se la conversione fallisce, restituisce un errore 400 Bad Request.
	chatID, err := strconv.Atoi(ps.ByName("chat_id"))
	if err != nil {
		rt.encodeResponse(w, model.ErrorResponse{Code: "400", Message: "Invalid Chat ID"}, http.StatusBadRequest)
		return
	}

	chat, err := rt.db.GetConversation(ctx.UserID, chatID)
	if err != nil {
		// Se l'errore contiene "not found", restituisce 404
		if err.Error() == database.ErrMsgChatNotFound {
			rt.encodeResponse(w, model.ErrorResponse{Code: "404", Message: "Chat not found"}, http.StatusNotFound)
			return
		}
		ctx.Logger.WithError(err).Error("error getting conversation")
		rt.encodeResponse(w, model.ErrorResponse{Code: "500", Message: "Internal Server Error"}, http.StatusInternalServerError)
		return
	}

	rt.encodeResponse(w, chat, http.StatusOK)
}

// setGroupName gestisce la PUT /chats/{chat_id}
func (rt *_router) setGroupName(w http.ResponseWriter, r *http.Request, ps httprouter.Params, ctx reqcontext.RequestContext) {
	// Validazione ID chat tramite strconv.Atoi
	chatID, err := strconv.Atoi(ps.ByName("chat_id"))
	if err != nil {
		rt.encodeResponse(w, model.ErrorResponse{Code: "400", Message: "Invalid Chat ID"}, http.StatusBadRequest)
		return
	}

	var req model.SetGroupNameRequest
	if err := json.NewDecoder(r.Body).Decode(&req); err != nil {
		rt.encodeResponse(w, model.ErrorResponse{Code: "400", Message: "Invalid request body"}, http.StatusBadRequest)
		return
	}

	if strings.TrimSpace(req.GroupName) == "" {
		rt.encodeResponse(w, model.ErrorResponse{Code: "400", Message: "Group name cannot be empty"}, http.StatusBadRequest)
		return
	}

	chat, err := rt.db.SetGroupName(ctx.UserID, chatID, req.GroupName)
	if err != nil {
		if err.Error() == database.ErrMsgChatNotFound {
			rt.encodeResponse(w, model.ErrorResponse{Code: "404", Message: "Chat not found"}, http.StatusNotFound)
			return
		}
		if err.Error() == "cannot rename an individual chat" {
			rt.encodeResponse(w, model.ErrorResponse{Code: "400", Message: "Cannot rename an individual chat"}, http.StatusBadRequest)
			return
		}
		ctx.Logger.WithError(err).Error("error setting group name")
		rt.encodeResponse(w, model.ErrorResponse{Code: "500", Message: "Internal Server Error"}, http.StatusInternalServerError)
		return
	}

	rt.encodeResponse(w, chat, http.StatusOK)
}

// deleteConversation gestisce la DELETE /chats/{chat_id}
func (rt *_router) deleteConversation(w http.ResponseWriter, r *http.Request, ps httprouter.Params, ctx reqcontext.RequestContext) {
	// Validazione ID chat tramite strconv.Atoi
	chatID, err := strconv.Atoi(ps.ByName("chat_id"))
	if err != nil {
		rt.encodeResponse(w, model.ErrorResponse{Code: "400", Message: "Invalid Chat ID"}, http.StatusBadRequest)
		return
	}

	err = rt.db.DeleteConversation(ctx.UserID, chatID)
	if err != nil {
		if err.Error() == database.ErrMsgChatNotFound {
			rt.encodeResponse(w, model.ErrorResponse{Code: "404", Message: "Chat not found"}, http.StatusNotFound)
			return
		}
		ctx.Logger.WithError(err).Error("error deleting conversation")
		rt.encodeResponse(w, model.ErrorResponse{Code: "500", Message: "Internal Server Error"}, http.StatusInternalServerError)
		return
	}

	w.WriteHeader(http.StatusNoContent)
}

// addToGroup gestisce POST /chats/{chat_id}/participants
func (rt *_router) addToGroup(w http.ResponseWriter, r *http.Request, ps httprouter.Params, ctx reqcontext.RequestContext) {
	// Validazione ID chat tramite strconv.Atoi
	chatID, err := strconv.Atoi(ps.ByName("chat_id"))
	if err != nil {
		rt.encodeResponse(w, model.ErrorResponse{Code: "400", Message: "Invalid Chat ID"}, http.StatusBadRequest)
		return
	}

	_, err = rt.db.GetConversation(ctx.UserID, chatID)
	if err != nil {
		// Se l'utente non fa parte della chat (o la chat non esiste), blocchiamo l'accesso.
		rt.encodeResponse(w, model.ErrorResponse{Code: "403", Message: "User not authorized (must be a member)"}, http.StatusForbidden)
		return
	}

	// 2. Decodifica body
	var req model.AddParticipantsRequest
	if err := json.NewDecoder(r.Body).Decode(&req); err != nil {
		rt.encodeResponse(w, model.ErrorResponse{Code: "400", Message: "Invalid request body"}, http.StatusBadRequest)
		return
	}
	if len(req.UserIDs) == 0 {
		rt.encodeResponse(w, model.ErrorResponse{Code: "400", Message: "No users provided"}, http.StatusBadRequest)
		return
	}

	// 3. Aggiunta al DB
	err = rt.db.AddToGroup(chatID, req.UserIDs)
	if err != nil {
		// Gestione errore "utente non trovato" (se provi ad aggiungere un ID che non esiste nel DB)
		if strings.Contains(err.Error(), "does not exist") { // Assicurati che il messaggio d'errore del DB contenga questa stringa o adattala
			rt.encodeResponse(w, model.ErrorResponse{Code: "400", Message: "One or more users do not exist"}, http.StatusBadRequest)
			return
		}

		ctx.Logger.WithError(err).Error("error adding participants")
		rt.encodeResponse(w, model.ErrorResponse{Code: "500", Message: "Internal server error"}, http.StatusInternalServerError)
		return
	}

	// 4. Restituisce la chat aggiornata
	chat, err := rt.db.GetConversation(ctx.UserID, chatID)
	if err != nil {
		ctx.Logger.WithError(err).Error("error fetching updated chat")
		rt.encodeResponse(w, model.ErrorResponse{Code: "500", Message: "Error fetching updated chat"}, http.StatusInternalServerError)
		return
	}
	rt.encodeResponse(w, chat, http.StatusOK)
}

// leaveGroup gestisce DELETE /chats/{chat_id}/participants/me
func (rt *_router) leaveGroup(w http.ResponseWriter, r *http.Request, ps httprouter.Params, ctx reqcontext.RequestContext) {
	// Validazione ID chat tramite strconv.Atoi
	chatID, err := strconv.Atoi(ps.ByName("chat_id"))
	if err != nil {
		rt.encodeResponse(w, model.ErrorResponse{Code: "400", Message: "Invalid Chat ID"}, http.StatusBadRequest)
		return
	}

	// Recupera la chat PRIMA di uscire per restituirla nella risposta
	chat, err := rt.db.GetConversation(ctx.UserID, chatID)
	if err != nil {
		rt.encodeResponse(w, model.ErrorResponse{Code: "404", Message: "Chat not found"}, http.StatusNotFound)
		return
	}

	err = rt.db.LeaveGroup(chatID, ctx.UserID)
	if err != nil {
		ctx.Logger.WithError(err).Error("error leaving group")
		rt.encodeResponse(w, model.ErrorResponse{Code: "500", Message: "Internal server error"}, http.StatusInternalServerError)
		return
	}

	// Restituisce l'oggetto chat (lo stato prima di uscire, o un oggetto parziale)
	rt.encodeResponse(w, chat, http.StatusOK)
}

// setGroupPhoto gestisce la PUT /chats/{chat_id}/photo
func (rt *_router) setGroupPhoto(w http.ResponseWriter, r *http.Request, ps httprouter.Params, ctx reqcontext.RequestContext) {
	// 1. Legge l'URL e viene estratto e validato l'ID della chat tramite strconv.Atoi, che converte la stringa "chat_id" dai parametri dell'URL in un intero.
	// Se la conversione fallisce, viene restituito un errore 400 Bad Request. Questo passaggio è fondamentale per assicurarsi che l'ID della chat sia valido prima di procedere con l'elaborazione della richiesta.
	chatID, err := strconv.Atoi(ps.ByName("chat_id"))
	if err != nil {
		rt.encodeResponse(w, model.ErrorResponse{Code: "400", Message: "Invalid Chat ID"}, http.StatusBadRequest)
		return
	}

	// 2. Parsing del form Multipart (max 10MB)
	err = r.ParseMultipartForm(10 << 20)
	if err != nil {
		ctx.Logger.WithError(err).Error("error parsing multipart form")
		rt.encodeResponse(w, model.ErrorResponse{Code: "400", Message: "Invalid form data or file too large"}, http.StatusBadRequest)
		return
	}

	// 3. Recupero del file - Si cerca il campo "file" all'interno del form multipart.
	// Se il campo non è presente o si verifica un errore durante il recupero, viene restituito un errore 400 Bad Request
	// con un messaggio che indica che il file è mancante. Se il file viene recuperato correttamente, viene chiuso al termine dell'elaborazione per evitare perdite di risorse.
	file, fileHeader, err := r.FormFile("file")
	if err != nil {
		rt.encodeResponse(w, model.ErrorResponse{Code: "400", Message: "Missing file"}, http.StatusBadRequest)
		return
	}
	defer file.Close()

	// 4. Generazione nome univoco e salvataggio
	// Nota: generateRandomString è visibile perché è nello stesso package 'api' (file messages-handler.go)
	randomName, err := generateRandomString(16)
	if err != nil {
		ctx.Logger.WithError(err).Error("error generating random filename")
		rt.encodeResponse(w, model.ErrorResponse{Code: "500", Message: "Internal Server Error"}, http.StatusInternalServerError)
		return
	}

	// Estrae l'estensione originale del file per preservarla (es. .jpg, .png)
	ext := filepath.Ext(fileHeader.Filename)
	newFileName := randomName + ext

	// Determina cartella upload (Docker vs Locale) - Si decide dove salvare il file
	uploadDir := os.Getenv("UPLOAD_DIR")
	if uploadDir == "" {
		uploadDir = "./uploads"
	}

	savePath := filepath.Join(uploadDir, newFileName)

	// Assicura che la cartella esista e se cosi non è, la crea.
	if err := os.MkdirAll(uploadDir, os.ModePerm); err != nil {
		ctx.Logger.WithError(err).Error("error creating upload directory")
		rt.encodeResponse(w, model.ErrorResponse{Code: "500", Message: "Internal Server Error"}, http.StatusInternalServerError)
		return
	}

	// Crea il file vuoto
	out, err := os.Create(savePath)
	if err != nil {
		ctx.Logger.WithError(err).Error("error creating file on disk")
		rt.encodeResponse(w, model.ErrorResponse{Code: "500", Message: "Internal Server Error"}, http.StatusInternalServerError)
		return
	}
	defer out.Close()

	// Questa è l'azione vera e propria. Prende i byte dal file ricevuto e li versa dentro il file vuoto out.
	// Ora l'immagine è fisicamente salvata sul disco (o nel volume Docker, a seconda dell'ambiente).
	// Se si verifica un errore durante questa operazione, viene restituito un errore 500 Internal Server Error.
	if _, err = io.Copy(out, file); err != nil {
		ctx.Logger.WithError(err).Error("error writing file content")
		rt.encodeResponse(w, model.ErrorResponse{Code: "500", Message: "Internal Server Error"}, http.StatusInternalServerError)
		return
	}

	// 5. Aggiornamento Database
	photoURL := "/uploads/" + newFileName

	chat, err := rt.db.SetGroupPhoto(ctx.UserID, chatID, photoURL)
	if err != nil {
		if err.Error() == database.ErrMsgChatNotFound {
			rt.encodeResponse(w, model.ErrorResponse{Code: "404", Message: "Chat not found"}, http.StatusNotFound)
			return
		}
		if err.Error() == "cannot change photo of an individual chat" {
			rt.encodeResponse(w, model.ErrorResponse{Code: "400", Message: "Cannot change photo of an individual chat"}, http.StatusBadRequest)
			return
		}
		ctx.Logger.WithError(err).Error("error setting group photo in DB")
		rt.encodeResponse(w, model.ErrorResponse{Code: "500", Message: "Internal Server Error"}, http.StatusInternalServerError)
		return
	}

	// 6. Restituisce la chat aggiornata
	rt.encodeResponse(w, chat, http.StatusOK)
}

// setGroupDescription (PUT /chats/:chat_id/description)
func (rt *_router) setGroupDescription(w http.ResponseWriter, r *http.Request, ps httprouter.Params, ctx reqcontext.RequestContext) {
	// Validazione ID chat tramite strconv.Atoi
	chatID, err := strconv.Atoi(ps.ByName("chat_id"))
	if err != nil {
		rt.encodeResponse(w, model.ErrorResponse{Code: "400", Message: "Invalid ID"}, http.StatusBadRequest)
		return
	}

	var req model.SetGroupDescriptionRequest
	if err := json.NewDecoder(r.Body).Decode(&req); err != nil {
		rt.encodeResponse(w, model.ErrorResponse{Code: "400", Message: "Invalid Body"}, http.StatusBadRequest)
		return
	}

	chat, err := rt.db.SetGroupDescription(ctx.UserID, chatID, req.Description)
	if err != nil {
		rt.encodeResponse(w, model.ErrorResponse{Code: "500", Message: err.Error()}, http.StatusInternalServerError)
		return
	}

	rt.encodeResponse(w, chat, http.StatusOK)
}
