package api

import (
	"crypto/rand"
	"encoding/hex"
	"encoding/json"
	"errors"
	"io"
	"mime/multipart"
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

// Funzione per generare nomi file casuali (32 caratteri) senza librerie esterne
func generateRandomString(n int) (string, error) {
	bytes := make([]byte, n)
	if _, err := rand.Read(bytes); err != nil {
		return "", err
	}
	return hex.EncodeToString(bytes), nil
}

// sendMessage gestisce POST /chats/{chat_id}/messages
// Supporta sia JSON (testo) che Multipart/Form-Data (immagini)
func (rt *_router) sendMessage(w http.ResponseWriter, r *http.Request, ps httprouter.Params, ctx reqcontext.RequestContext) {
	// Estrazione chat_id da URL tramite strconv.Atoi. Se non è un numero valido, ritorna 400 Bad Request.
	chatID, err := strconv.Atoi(ps.ByName("chat_id"))
	if err != nil {
		rt.encodeResponse(w, model.ErrorResponse{Code: "400", Message: "Invalid Chat ID"}, http.StatusBadRequest)
		return
	}

	var req model.CreateMessageRequest
	var file multipart.File
	var fileHeader *multipart.FileHeader

	// Controlla il Content-Type per decidere come leggere la richiesta
	contentType := r.Header.Get("Content-Type")
	// Controllo due casi principali: se è multipart/form-data, gestiamo l'upload di file. Altrimenti, assumiamo che sia JSON per messaggi di solo testo.
	if strings.HasPrefix(contentType, "multipart/form-data") {
		// --- CASO 1: UPLOAD FILE (Multipart) ---
		// Alloco fino a 10MB per il parsing del form. Se il file è più grande, ritorna 400 Bad Request.
		err = r.ParseMultipartForm(10 << 20)
		if err != nil {
			rt.encodeResponse(w, model.ErrorResponse{Code: "400", Message: "File too large or invalid form"}, http.StatusBadRequest)
			return
		}

		// 2. Legge i campi testuali
		req.Content = r.FormValue("content")
		req.Type = r.FormValue("type")
		if req.Type == "" {
			req.Type = "text"
		}

		// 3. Legge il file e estrae il nome originale
		file, fileHeader, err = r.FormFile("file")
		if err != nil && !errors.Is(err, http.ErrMissingFile) {
			rt.encodeResponse(w, model.ErrorResponse{Code: "400", Message: "Error reading file"}, http.StatusBadRequest)
			return
		}
		if file != nil {
			defer file.Close()
		}

	} else {
		// --- CASO 2: SOLO TESTO (JSON) ---
		if err := json.NewDecoder(r.Body).Decode(&req); err != nil {
			rt.encodeResponse(w, model.ErrorResponse{Code: "400", Message: "Invalid request body"}, http.StatusBadRequest)
			return
		}
	}

	// --- SALVATAGGIO FILE ---
	if file != nil {
		// Genera nome casuale univoco
		randomName, err := generateRandomString(16)
		if err != nil {
			ctx.Logger.WithError(err).Error("error generating random filename")
			rt.encodeResponse(w, model.ErrorResponse{Code: "500", Message: "Internal Server Error"}, http.StatusInternalServerError)
			return
		}

		ext := filepath.Ext(fileHeader.Filename)
		newFileName := randomName + ext

		// --- MODIFICA FONDAMENTALE: Percorso Dinamico ---
		// Se si è in Docker, userà /app/uploads. Se si è in Locale, userà ./uploads
		uploadDir := os.Getenv("UPLOAD_DIR")
		if uploadDir == "" {
			uploadDir = "./uploads"
		}

		savePath := filepath.Join(uploadDir, newFileName)

		// Viene creata la cartella di upload se non esiste
		if err := os.MkdirAll(uploadDir, os.ModePerm); err != nil {
			ctx.Logger.WithError(err).Error("error creating upload directory")
			rt.encodeResponse(w, model.ErrorResponse{Code: "500", Message: "Unable to create upload directory"}, http.StatusInternalServerError)
			return
		}

		// Crea il file su disco
		out, err := os.Create(savePath)
		if err != nil {
			ctx.Logger.WithError(err).Error("error creating file on disk")
			rt.encodeResponse(w, model.ErrorResponse{Code: "500", Message: "Unable to save file"}, http.StatusInternalServerError)
			return
		}
		defer out.Close()

		// Scrive il contenuto
		if _, err = io.Copy(out, file); err != nil {
			ctx.Logger.WithError(err).Error("error writing file content")
			rt.encodeResponse(w, model.ErrorResponse{Code: "500", Message: "Unable to write file"}, http.StatusInternalServerError)
			return
		}

		// Imposta URL pubblico e Tipo per il DB
		req.MediaURL = "/uploads/" + newFileName
		req.Type = "image"
	}

	// Validazione contenuto
	if req.Type == "text" && strings.TrimSpace(req.Content) == "" {
		rt.encodeResponse(w, model.ErrorResponse{Code: "400", Message: "Content required for text messages"}, http.StatusBadRequest)
		return
	}
	if (req.Type == "image" || req.Type == "video") && req.MediaURL == "" {
		rt.encodeResponse(w, model.ErrorResponse{Code: "400", Message: "MediaURL required for media messages"}, http.StatusBadRequest)
		return
	}

	// Chiama il DB
	msg, err := rt.db.SendMessage(ctx.UserID, chatID, req)
	if err != nil {
		if err.Error() == "user not authorized to send messages to this chat" {
			rt.encodeResponse(w, model.ErrorResponse{Code: "404", Message: "Chat not found"}, http.StatusNotFound)
			return
		}
		ctx.Logger.WithError(err).Error("error sending message")
		rt.encodeResponse(w, model.ErrorResponse{Code: "500", Message: "Internal Server Error"}, http.StatusInternalServerError)
		return
	}

	rt.encodeResponse(w, msg, http.StatusCreated)
}

// getMessages gestisce GET /chats/{chat_id}/messages
func (rt *_router) getMessages(w http.ResponseWriter, r *http.Request, ps httprouter.Params, ctx reqcontext.RequestContext) {
	chatID, err := strconv.Atoi(ps.ByName("chat_id"))
	if err != nil {
		rt.encodeResponse(w, model.ErrorResponse{Code: "400", Message: "Invalid Chat ID"}, http.StatusBadRequest)
		return
	}

	// Chiamata al database per ottenere i messaggi della chat. Se la chat non esiste o l'utente non è autorizzato, ritorna 404.
	messages, err := rt.db.GetMessages(ctx.UserID, chatID)
	if err != nil {
		if err.Error() == database.ErrMsgChatNotFound {
			rt.encodeResponse(w, model.ErrorResponse{Code: "404", Message: "Chat not found"}, http.StatusNotFound)
			return
		}
		ctx.Logger.WithError(err).Error("error getting messages")
		rt.encodeResponse(w, model.ErrorResponse{Code: "500", Message: "Internal Server Error"}, http.StatusInternalServerError)
		return
	}

	if messages == nil {
		messages = []model.Message{}
	}

	rt.encodeResponse(w, messages, http.StatusOK)
}

// deleteMessage gestisce DELETE /chats/{chat_id}/messages/{message_id}
func (rt *_router) deleteMessage(w http.ResponseWriter, r *http.Request, ps httprouter.Params, ctx reqcontext.RequestContext) {
	// Estrazione chat_id e message_id da URL tramite strconv.Atoi. Se non sono numeri validi, ritorna 400 Bad Request.
	chatID, _ := strconv.Atoi(ps.ByName("chat_id"))
	messageID, err := strconv.Atoi(ps.ByName("message_id"))
	if err != nil {
		rt.encodeResponse(w, model.ErrorResponse{Code: "400", Message: "Invalid Message ID"}, http.StatusBadRequest)
		return
	}
	// Chiamata al database per eliminare il messaggio. Se la chat o il messaggio non esistono, o se l'utente non è autorizzato a eliminarlo, ritorna 404.
	err = rt.db.DeleteMessage(ctx.UserID, chatID, messageID)
	if err != nil {
		if err.Error() == "message not found or user not authorized to delete" {
			rt.encodeResponse(w, model.ErrorResponse{Code: "404", Message: "Message not found or forbidden"}, http.StatusNotFound)
			return
		}
		ctx.Logger.WithError(err).Error("error deleting message")
		rt.encodeResponse(w, model.ErrorResponse{Code: "500", Message: "Internal Server Error"}, http.StatusInternalServerError)
		return
	}

	w.WriteHeader(http.StatusNoContent)
}

// replyToMessage gestisce POST /chats/{chat_id}/messages/{message_id}/reply
// Supporta anche qui invio di immagini come risposta
func (rt *_router) replyToMessage(w http.ResponseWriter, r *http.Request, ps httprouter.Params, ctx reqcontext.RequestContext) {
	chatID, _ := strconv.Atoi(ps.ByName("chat_id"))
	parentMessageID, err := strconv.Atoi(ps.ByName("message_id"))
	if err != nil {
		rt.encodeResponse(w, model.ErrorResponse{Code: "400", Message: "Invalid Parent Message ID"}, http.StatusBadRequest)
		return
	}

	var req model.CreateMessageRequest
	var file multipart.File
	var fileHeader *multipart.FileHeader

	// Logica identica a sendMessage per gestione Multipart vs JSON
	contentType := r.Header.Get("Content-Type")

	if strings.HasPrefix(contentType, "multipart/form-data") {
		err = r.ParseMultipartForm(10 << 20)
		if err != nil {
			rt.encodeResponse(w, model.ErrorResponse{Code: "400", Message: "File too large"}, http.StatusBadRequest)
			return
		}
		req.Content = r.FormValue("content")
		req.Type = r.FormValue("type")
		if req.Type == "" {
			req.Type = "text"
		}

		file, fileHeader, err = r.FormFile("file")
		if err != nil && !errors.Is(err, http.ErrMissingFile) {
			rt.encodeResponse(w, model.ErrorResponse{Code: "400", Message: "Error reading file"}, http.StatusBadRequest)
			return
		}
		if file != nil {
			defer file.Close()
		}
	} else {
		if err := json.NewDecoder(r.Body).Decode(&req); err != nil {
			rt.encodeResponse(w, model.ErrorResponse{Code: "400", Message: "Invalid request body"}, http.StatusBadRequest)
			return
		}
	}

	// Gestione salvataggio file risposta
	if file != nil {
		randomName, err := generateRandomString(16)
		if err != nil {
			ctx.Logger.WithError(err).Error("error generating filename")
			rt.encodeResponse(w, model.ErrorResponse{Code: "500", Message: "Internal Server Error"}, http.StatusInternalServerError)
			return
		}

		ext := filepath.Ext(fileHeader.Filename)
		newFileName := randomName + ext

		// Percorso Dinamico
		uploadDir := os.Getenv("UPLOAD_DIR")
		if uploadDir == "" {
			uploadDir = "./uploads"
		}

		savePath := filepath.Join(uploadDir, newFileName)

		// Crea la cartella se non esiste
		if err := os.MkdirAll(uploadDir, os.ModePerm); err != nil {
			ctx.Logger.WithError(err).Error("error creating upload directory")
			rt.encodeResponse(w, model.ErrorResponse{Code: "500", Message: "Unable to create upload directory"}, http.StatusInternalServerError)
			return
		}

		out, err := os.Create(savePath)
		if err != nil {
			ctx.Logger.WithError(err).Error("error creating file")
			rt.encodeResponse(w, model.ErrorResponse{Code: "500", Message: "Internal Server Error"}, http.StatusInternalServerError)
			return
		}
		defer out.Close()

		if _, err = io.Copy(out, file); err != nil {
			ctx.Logger.WithError(err).Error("error writing file")
			rt.encodeResponse(w, model.ErrorResponse{Code: "500", Message: "Internal Server Error"}, http.StatusInternalServerError)
			return
		}

		req.MediaURL = "/uploads/" + newFileName
		req.Type = "image"
	}

	// Validazione contenuto
	if req.Type == "text" && strings.TrimSpace(req.Content) == "" {
		rt.encodeResponse(w, model.ErrorResponse{Code: "400", Message: "Content required"}, http.StatusBadRequest)
		return
	}

	msg, err := rt.db.ReplyToMessage(ctx.UserID, chatID, parentMessageID, req)
	if err != nil {
		if err.Error() == "parent message not found in this chat" {
			rt.encodeResponse(w, model.ErrorResponse{Code: "404", Message: "Parent message not found"}, http.StatusNotFound)
			return
		}
		ctx.Logger.WithError(err).Error("error sending reply")
		rt.encodeResponse(w, model.ErrorResponse{Code: "500", Message: "Internal Server Error"}, http.StatusInternalServerError)
		return
	}

	rt.encodeResponse(w, msg, http.StatusCreated)
}

// forwardMessage gestisce POST /chats/{chat_id}/messages/{message_id}/forward
func (rt *_router) forwardMessage(w http.ResponseWriter, r *http.Request, ps httprouter.Params, ctx reqcontext.RequestContext) {
	// Estrazione chat_id e message_id da URL tramite strconv.Atoi. Se non sono numeri validi, ritorna 400 Bad Request.
	sourceChatID, _ := strconv.Atoi(ps.ByName("chat_id"))
	sourceMessageID, err := strconv.Atoi(ps.ByName("message_id"))
	if err != nil {
		rt.encodeResponse(w, model.ErrorResponse{Code: "400", Message: "Invalid Message ID"}, http.StatusBadRequest)
		return
	}
	// Decodifica del body per ottenere la lista di chat di destinazione. Se il body non è un JSON valido o manca la lista, ritorna 400 Bad Request.
	var req model.ForwardMessageRequest
	if err := json.NewDecoder(r.Body).Decode(&req); err != nil {
		rt.encodeResponse(w, model.ErrorResponse{Code: "400", Message: "Invalid request body"}, http.StatusBadRequest)
		return
	}

	if len(req.TargetChatIDs) == 0 {
		rt.encodeResponse(w, model.ErrorResponse{Code: "400", Message: "At least one target chat ID is required"}, http.StatusBadRequest)
		return
	}
	// Chiamata al database per inoltrare il messaggio. Se la chat o il messaggio di origine non esistono, o se l'utente non è autorizzato a inoltrare, ritorna 404. Se l'utente non è autorizzato a postare in una delle chat di destinazione, ritorna 403.
	forwardedMsgs, err := rt.db.ForwardMessage(ctx.UserID, sourceChatID, sourceMessageID, req.TargetChatIDs)
	if err != nil {
		if err.Error() == "source chat not found or user not authorized" || err.Error() == "original message not found" {
			rt.encodeResponse(w, model.ErrorResponse{Code: "404", Message: "Message or source chat not found"}, http.StatusNotFound)
			return
		}
		if strings.Contains(err.Error(), "not authorized to post") {
			rt.encodeResponse(w, model.ErrorResponse{Code: "403", Message: err.Error()}, http.StatusForbidden)
			return
		}

		ctx.Logger.WithError(err).Error("error forwarding message")
		rt.encodeResponse(w, model.ErrorResponse{Code: "500", Message: "Internal Server Error"}, http.StatusInternalServerError)
		return
	}

	rt.encodeResponse(w, forwardedMsgs, http.StatusCreated)
}
