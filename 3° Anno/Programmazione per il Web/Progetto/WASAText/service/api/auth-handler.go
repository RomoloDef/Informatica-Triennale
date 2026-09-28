package api

import (
	"encoding/json"
	"errors"
	"net/http"

	"github.com/RomoloDef/WASAText/service/api/reqcontext"
	"github.com/RomoloDef/WASAText/service/model"
	"github.com/julienschmidt/httprouter"
)

// La funzione doLogin gestisce la richiesta di login/registrazione di un utente tramite la chiamata POST /users.
func (rt *_router) doLogin(w http.ResponseWriter, r *http.Request, ps httprouter.Params, ctx reqcontext.RequestContext) {

	// FASE 1: Decodifica Richiesta HTTP
	var req model.LoginUserRequest
	err := json.NewDecoder(r.Body).Decode(&req)
	if err != nil {
		// Logga l'errore di decodifica
		ctx.Logger.WithError(err).Error("error decoding request body")
		// Risposta di errore (400 Bad Request)
		rt.encodeResponse(w, model.ErrorResponse{Code: "400", Message: "Invalid request body"}, http.StatusBadRequest)
		return
	}

	// FASE 2: Validazione del Campo 'name'
	// Controlla che il nome sia presente e rispetti i vincoli di lunghezza (3-16 caratteri)
	if req.Name == "" || len(req.Name) < 3 || len(req.Name) > 16 {
		ctx.Logger.Warnf("invalid username format: %s", req.Name)
		rt.encodeResponse(w, model.ErrorResponse{Code: "400", Message: "Username must be between 3 and 16 characters."}, http.StatusBadRequest)
		return
	}

	// FASE 3: Chiamata al Database

	// Il DB cerca un utente con quel nome, se non esiste lo crea.
	// Viene richiamata la funzione DoLogin del database.
	user, err := rt.db.DoLogin(req.Name)
	if err != nil {
		// Controlla se l'errore è un conflitto (es. nome già usato se non è il simplified login)
		if errors.Is(err, model.ErrConflict) {
			rt.encodeResponse(w, model.ErrorResponse{Code: "409", Message: "Username already taken."}, http.StatusConflict)
			return
		}

		// Gestione errore interno del DB
		ctx.Logger.WithError(err).Error("error during DoLogin database operation")
		rt.encodeResponse(w, model.ErrorResponse{Code: "500", Message: "Internal server error"}, http.StatusInternalServerError)
		return
	}

	// FASE 4 & 5: Costruzione, Codifica e Invio Risposta

	// Costruisce l'oggetto di risposta finale
	res := model.User{
		ID:       user.ID, // L'ID utente restituito dal DB
		Name:     user.Name,
		PhotoURL: user.PhotoURL,
	}

	// Il login (anche se crea) restituisce 201 Created come da specifica OpenAPI.
	ctx.Logger.WithField("user_id", user.ID).Infof("User successfully logged in/registered")
	rt.encodeResponse(w, res, http.StatusCreated)
}

func (rt *_router) encodeResponse(w http.ResponseWriter, data interface{}, status int) {
	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(status)
	err := json.NewEncoder(w).Encode(data)
	if err != nil {
		rt.baseLogger.WithError(err).Error("error encoding response")
	}
}
