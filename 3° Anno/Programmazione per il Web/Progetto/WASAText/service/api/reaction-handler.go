package api

import (
	"encoding/json"
	"net/http"
	"strconv"

	"github.com/RomoloDef/WASAText/service/api/reqcontext"
	"github.com/RomoloDef/WASAText/service/model"
	"github.com/julienschmidt/httprouter"
)

// commentMessage gestisce POST /chats/{chat_id}/messages/{message_id}/reaction
func (rt *_router) commentMessage(w http.ResponseWriter, r *http.Request, ps httprouter.Params, ctx reqcontext.RequestContext) {
	// Estrae chat_id e message_id dai parametri dell'URL
	chatID, _ := strconv.Atoi(ps.ByName("chat_id"))
	messageID, err := strconv.Atoi(ps.ByName("message_id"))
	if err != nil {
		rt.encodeResponse(w, model.ErrorResponse{Code: "400", Message: "Invalid Message ID"}, http.StatusBadRequest)
		return
	}

	// Decodifica il corpo della richiesta per ottenere l'emoji_code
	var req model.CreateReactionRequest
	if err := json.NewDecoder(r.Body).Decode(&req); err != nil {
		rt.encodeResponse(w, model.ErrorResponse{Code: "400", Message: "Invalid request body"}, http.StatusBadRequest)
		return
	}

	if req.EmojiCode == "" {
		rt.encodeResponse(w, model.ErrorResponse{Code: "400", Message: "Emoji code is required"}, http.StatusBadRequest)
		return
	}
	// Chiamata al database per aggiungere o aggiornare la reazione
	reaction, err := rt.db.CommentMessage(ctx.UserID, chatID, messageID, req.EmojiCode)
	if err != nil {
		if err.Error() == "message not found in this chat" || err.Error() == "user not authorized" {
			rt.encodeResponse(w, model.ErrorResponse{Code: "404", Message: "Message not found or forbidden"}, http.StatusNotFound)
			return
		}
		ctx.Logger.WithError(err).Error("error adding reaction")
		rt.encodeResponse(w, model.ErrorResponse{Code: "500", Message: "Internal Server Error"}, http.StatusInternalServerError)
		return
	}

	rt.encodeResponse(w, reaction, http.StatusCreated)
}

// uncommentMessage gestisce DELETE /chats/{chat_id}/messages/{message_id}/reaction
func (rt *_router) uncommentMessage(w http.ResponseWriter, r *http.Request, ps httprouter.Params, ctx reqcontext.RequestContext) {
	// Estrae chat_id e message_id dai parametri dell'URL
	chatID, _ := strconv.Atoi(ps.ByName("chat_id"))
	messageID, err := strconv.Atoi(ps.ByName("message_id"))
	if err != nil {
		rt.encodeResponse(w, model.ErrorResponse{Code: "400", Message: "Invalid Message ID"}, http.StatusBadRequest)
		return
	}
	// Chiamata al database per rimuovere la reazione
	err = rt.db.UncommentMessage(ctx.UserID, chatID, messageID)
	if err != nil {
		if err.Error() == "message not found in this chat" || err.Error() == "reaction not found" {
			rt.encodeResponse(w, model.ErrorResponse{Code: "404", Message: "Reaction or message not found"}, http.StatusNotFound)
			return
		}
		ctx.Logger.WithError(err).Error("error removing reaction")
		rt.encodeResponse(w, model.ErrorResponse{Code: "500", Message: "Internal Server Error"}, http.StatusInternalServerError)
		return
	}

	w.WriteHeader(http.StatusNoContent)
}
