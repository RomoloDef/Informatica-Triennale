package api

import (
	"encoding/json"
	"errors"
	"net/http"
	"strings"

	"github.com/RomoloDef/WASAText/service/api/reqcontext"
	"github.com/RomoloDef/WASAText/service/model"
	"github.com/julienschmidt/httprouter"
)

// getMyProfile gestisce la GET /users/me
func (rt *_router) getMyProfile(w http.ResponseWriter, r *http.Request, ps httprouter.Params, ctx reqcontext.RequestContext) {
	// Prende l'ID dal token di login (popolato grazie a authWrap)
	user, err := rt.db.GetUserById(ctx.UserID)
	if err != nil {
		ctx.Logger.WithError(err).Error("error retrieving user profile")
		w.WriteHeader(http.StatusInternalServerError)
		return
	}

	w.Header().Set("Content-Type", "application/json")
	rt.encodeResponse(w, user, http.StatusOK)
}

// setMyUserName gestisce la PUT /users/me/name
func (rt *_router) setMyUserName(w http.ResponseWriter, r *http.Request, ps httprouter.Params, ctx reqcontext.RequestContext) {
	var req model.SetNameRequest
	// 1. Decodifica Richiesta
	// Tramite il costrutto json.NewDecoder(r.Body).Decode(&req) decodifico il body della richiesta HTTP in un oggetto Go (SetNameRequest).
	err := json.NewDecoder(r.Body).Decode(&req)
	// Se la decodifica fallisce (ad esempio, se il body non è un JSON valido o non corrisponde alla struttura di SetNameRequest), viene restituito un errore.
	if err != nil {
		ctx.Logger.WithError(err).Error("error decoding request body")
		rt.encodeResponse(w, model.ErrorResponse{Code: "400", Message: "Invalid request body"}, http.StatusBadRequest)
		return
	}

	// 2. Validazione
	if req.Name == "" || len(req.Name) < 3 || len(req.Name) > 16 {
		ctx.Logger.Warnf("invalid username format: %s", req.Name)
		rt.encodeResponse(w, model.ErrorResponse{Code: "400", Message: "Username must be between 3 and 16 characters."}, http.StatusBadRequest)
		return
	}

	// 3. Chiamata al Database
	userID := ctx.UserID
	err = rt.db.UpdateUserName(userID, req.Name)

	if err != nil {
		if errors.Is(err, model.ErrConflict) {
			rt.encodeResponse(w, model.ErrorResponse{Code: "409", Message: "Username already taken."}, http.StatusConflict)
			return
		}
		ctx.Logger.WithError(err).Error("error updating username in DB")
		rt.encodeResponse(w, model.ErrorResponse{Code: "500", Message: "Internal server error"}, http.StatusInternalServerError)
		return
	}

	// 4. Recupera l'utente aggiornato per restituirlo
	updatedUser, err := rt.db.GetUserById(userID)
	if err != nil {
		ctx.Logger.WithError(err).Error("error retrieving updated user profile")
		rt.encodeResponse(w, model.ErrorResponse{Code: "500", Message: "Internal server error"}, http.StatusInternalServerError)
		return
	}

	// 5. Risposta: 200 OK con l'oggetto User
	ctx.Logger.Infof("User %d successfully updated name to %s", userID, req.Name)
	rt.encodeResponse(w, updatedUser, http.StatusOK)
}

// setMyPhoto gestisce la PUT /users/me/photo
func (rt *_router) setMyPhoto(w http.ResponseWriter, r *http.Request, ps httprouter.Params, ctx reqcontext.RequestContext) {
	// 1. Decodifica Richiesta
	// Tramite il costrutto json.NewDecoder(r.Body).Decode(&req) decodifico il body della richiesta HTTP in un oggetto Go (SetPhotoRequest).
	var req model.SetPhotoRequest
	err := json.NewDecoder(r.Body).Decode(&req)
	if err != nil {
		ctx.Logger.WithError(err).Error("error decoding request body")
		rt.encodeResponse(w, model.ErrorResponse{Code: "400", Message: "Invalid request body"}, http.StatusBadRequest)
		return
	}

	// 2. Validazione
	if len(req.PhotoURL) > 2048 {
		ctx.Logger.Warnf("photo URL too long")
		rt.encodeResponse(w, model.ErrorResponse{Code: "400", Message: "Photo URL is too long."}, http.StatusBadRequest)
		return
	}

	// 3. Chiamata al Database
	userID := ctx.UserID
	err = rt.db.UpdateUserPhoto(userID, req.PhotoURL)

	if err != nil {
		ctx.Logger.WithError(err).Error("error updating user photo in DB")
		rt.encodeResponse(w, model.ErrorResponse{Code: "500", Message: "Internal server error"}, http.StatusInternalServerError)
		return
	}

	// 4. Recupera l'utente aggiornato per restituirlo
	updatedUser, err := rt.db.GetUserById(userID)
	if err != nil {
		ctx.Logger.WithError(err).Error("error retrieving updated user profile")
		rt.encodeResponse(w, model.ErrorResponse{Code: "500", Message: "Internal server error"}, http.StatusInternalServerError)
		return
	}

	// 5. Risposta: 200 OK con l'oggetto User
	ctx.Logger.Infof("User %d successfully updated photo URL", userID)
	rt.encodeResponse(w, updatedUser, http.StatusOK)
}

// searchUsers gestisce la GET /users/search
func (rt *_router) searchUsers(w http.ResponseWriter, r *http.Request, ps httprouter.Params, ctx reqcontext.RequestContext) {
	// 1. Recupero Parametro (username)
	query := r.URL.Query().Get("username")

	// 2. Validazione
	if strings.TrimSpace(query) == "" {
		rt.encodeResponse(w, model.ErrorResponse{Code: "400", Message: "Query parameter 'username' is required."}, http.StatusBadRequest)
		return
	}

	// 3. Chiamata al Database
	users, err := rt.db.SearchUsers(query)

	if err != nil {
		ctx.Logger.WithError(err).Error("error searching users in DB")
		rt.encodeResponse(w, model.ErrorResponse{Code: "500", Message: "Internal server error"}, http.StatusInternalServerError)
		return
	}

	// 4. Risposta: 200 OK
	ctx.Logger.Infof("Search for '%s' returned %d results", query, len(users))
	rt.encodeResponse(w, users, http.StatusOK)
}

// deleteMyAccount gestisce la DELETE /users/me
func (rt *_router) deleteMyAccount(w http.ResponseWriter, r *http.Request, ps httprouter.Params, ctx reqcontext.RequestContext) {
	userID := ctx.UserID
	// 1. Chiamata al Database
	err := rt.db.DeleteUser(userID)
	// Se l'eliminazione fallisce, restituisce un errore 500 Internal Server Error, poiché non ci si aspetta che un utente autenticato non esista.
	if err != nil {
		ctx.Logger.WithError(err).Error("error deleting user in DB")
		rt.encodeResponse(w, model.ErrorResponse{Code: "500", Message: "Internal server error"}, http.StatusInternalServerError)
		return
	}

	// Risposta: 204 No Content
	ctx.Logger.WithField("user_id", userID).Warnf("User successfully deleted account")
	w.WriteHeader(http.StatusNoContent)
}
