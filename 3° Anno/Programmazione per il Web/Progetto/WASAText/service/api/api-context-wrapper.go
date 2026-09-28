package api

import (
	"net/http"

	"strconv"
	"strings"

	"github.com/RomoloDef/WASAText/service/api/reqcontext"
	"github.com/RomoloDef/WASAText/service/model"
	"github.com/gofrs/uuid"
	"github.com/julienschmidt/httprouter"
	"github.com/sirupsen/logrus"
)

// httpRouterHandler is the signature for functions that accepts a reqcontext.RequestContext in addition to those
// required by the httprouter package.
type httpRouterHandler func(http.ResponseWriter, *http.Request, httprouter.Params, reqcontext.RequestContext)

// wrap parses the request and adds a reqcontext.RequestContext instance related to the request.
func (rt *_router) wrap(fn httpRouterHandler) func(http.ResponseWriter, *http.Request, httprouter.Params) {
	return func(w http.ResponseWriter, r *http.Request, ps httprouter.Params) {
		reqUUID, err := uuid.NewV4()
		if err != nil {
			rt.baseLogger.WithError(err).Error("can't generate a request UUID")
			w.WriteHeader(http.StatusInternalServerError)
			return
		}
		var ctx = reqcontext.RequestContext{
			ReqUUID: reqUUID,
		}

		// Create a request-specific logger
		ctx.Logger = rt.baseLogger.WithFields(logrus.Fields{
			"reqid":     ctx.ReqUUID.String(),
			"remote-ip": r.RemoteAddr,
		})

		// Call the next handler in chain (usually, the handler function for the path)
		fn(w, r, ps, ctx)
	}
}

// authRouterHandler è la firma per gli handler protetti che usano il contesto.
type authRouterHandler = httpRouterHandler

// authWrap (wrapper per rotte protette: aggiunge UUID, Logger E verifica l'AUTH)
func (rt *_router) authWrap(fn authRouterHandler) func(http.ResponseWriter, *http.Request, httprouter.Params) {
	return func(w http.ResponseWriter, r *http.Request, ps httprouter.Params) {

		// 1. Esegui la logica di base (creazione UUID e Logger)
		reqUUID, err := uuid.NewV4()
		if err != nil {
			rt.baseLogger.WithError(err).Error("can't generate a request UUID")
			w.WriteHeader(http.StatusInternalServerError)
			return
		}

		var ctx = reqcontext.RequestContext{
			ReqUUID: reqUUID,
		}

		ctx.Logger = rt.baseLogger.WithFields(logrus.Fields{
			"reqid":     ctx.ReqUUID.String(),
			"remote-ip": r.RemoteAddr,
		})

		// 2. Estrai e valida l'ID Utente dall'header Authorization
		authHeader := r.Header.Get("Authorization")
		if authHeader == "" || !strings.HasPrefix(authHeader, "Bearer ") {
			ctx.Logger.Error("Authentication required: Bearer token missing or malformed")
			rt.encodeResponse(w, model.ErrorResponse{Code: "401", Message: "Authentication required"}, http.StatusUnauthorized)
			return
		}

		token := strings.TrimPrefix(authHeader, "Bearer ")

		userID, err := strconv.Atoi(token)
		if err != nil {
			ctx.Logger.WithError(err).Error("Invalid user ID format in Authorization token")
			rt.encodeResponse(w, model.ErrorResponse{Code: "401", Message: "Invalid token format"}, http.StatusUnauthorized)
			return
		}

		// 3. Popola ctx.UserID
		ctx.UserID = userID

		// 4. Chiama l'handler finale
		fn(w, r, ps, ctx)
	}
}
