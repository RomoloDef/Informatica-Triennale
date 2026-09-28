package api

import (
	"net/http"
	"os"
)

// Handler returns an instance of httprouter.Router that handle APIs registered here
func (rt *_router) Handler() http.Handler {
	// Rotta per le immagini caricate dagli utenti
	// Se c'è la variabile d'ambiente UPLOAD_DIR (in Docker), usa quella.
	// Altrimenti usa "./uploads" (cartella locale).
	uploadDir := os.Getenv("UPLOAD_DIR")
	if uploadDir == "" {
		uploadDir = "./uploads"
	}
	// Serve i file dalla cartella di upload
	rt.router.ServeFiles("/uploads/*filepath", http.Dir(uploadDir))
	// SEZIONE 0 - REGISTRAZIONE
	rt.router.GET("/", rt.getHelloWorld)
	rt.router.GET("/context", rt.wrap(rt.getContextReply))
	// SEZIONE 1 - UTENTI
	rt.router.POST("/users", rt.wrap(rt.doLogin))
	rt.router.GET("/users/me", rt.authWrap(rt.getMyProfile))
	rt.router.PUT("/users/me/name", rt.authWrap(rt.setMyUserName))
	rt.router.PUT("/users/me/photo", rt.authWrap(rt.setMyPhoto))
	rt.router.GET("/users/search", rt.authWrap(rt.searchUsers))
	rt.router.DELETE("/users/me", rt.authWrap(rt.deleteMyAccount))
	// SEZIONE 2 - CHAT
	rt.router.POST("/chats", rt.authWrap(rt.createConversation))
	rt.router.GET("/chats", rt.authWrap(rt.getMyConversations))
	rt.router.GET("/chats/:chat_id", rt.authWrap(rt.getConversation))
	rt.router.PUT("/chats/:chat_id", rt.authWrap(rt.setGroupName))
	rt.router.PUT("/chats/:chat_id/photo", rt.authWrap(rt.setGroupPhoto))
	rt.router.PUT("/chats/:chat_id/description", rt.authWrap(rt.setGroupDescription))
	rt.router.DELETE("/chats/:chat_id", rt.authWrap(rt.deleteConversation))
	rt.router.POST("/chats/:chat_id/participants", rt.authWrap(rt.addToGroup))
	rt.router.DELETE("/chats/:chat_id/participants/me", rt.authWrap(rt.leaveGroup))
	// SEZIONE 3 - MESSAGGI
	rt.router.POST("/chats/:chat_id/messages", rt.authWrap(rt.sendMessage))
	rt.router.GET("/chats/:chat_id/messages", rt.authWrap(rt.getMessages))
	rt.router.DELETE("/chats/:chat_id/messages/:message_id", rt.authWrap(rt.deleteMessage))
	rt.router.POST("/chats/:chat_id/messages/:message_id/reply", rt.authWrap(rt.replyToMessage))
	rt.router.POST("/chats/:chat_id/messages/:message_id/forward", rt.authWrap(rt.forwardMessage))
	// SEZIONE 4 - REAZIONI
	rt.router.POST("/chats/:chat_id/messages/:message_id/reaction", rt.authWrap(rt.commentMessage))
	rt.router.DELETE("/chats/:chat_id/messages/:message_id/reaction", rt.authWrap(rt.uncommentMessage))
	// Special routes
	rt.router.GET("/liveness", rt.liveness)

	return rt.router
}
