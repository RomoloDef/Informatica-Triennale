package model

import (
	"errors"
)

/*  Inserisco le mie strutture dati qui

Lo faccio per sezioni:

*/

// SEZIONE 1 - UTENTI

type User struct {
	ID       int    `json:"id"`
	Name     string `json:"name"`
	PhotoURL string `json:"photo_url"`
}

type LoginUserRequest struct {
	Name string `json:"name"`
}

type SetNameRequest struct {
	Name string `json:"name"`
}

type SetPhotoRequest struct {
	PhotoURL string `json:"photo_url"`
}

// SEZIONE 2 - CHAT

type Chat struct {
	ID          int                 `json:"id"`
	Type        string              `json:"type"`           // individual o group
	Name        string              `json:"name,omitempty"` // nome del gruppo
	PhotoURL    string              `json:"photo_url,omitempty"`
	Members     []User              `json:"members"`
	IsAdmin     bool                `json:"is_admin,omitempty"`
	LastMessage *LastMessagePreview `json:"last_message,omitempty"`
	Description string              `json:"description,omitempty"`
}

type CreateChatRequest struct {
	Type            string `json:"type"`         // individual o group
	ParticipantsIDs []int  `json:"participants"` // IDs degli utenti partecipanti
	// Per chat di gruppo
	GroupName   string `json:"group_name,omitempty"`
	Description string `json:"description,omitempty"`
	IconURL     string `json:"icon_url,omitempty"`
	GroupIcon   string `json:"group_icon,omitempty"`
}

type SetGroupNameRequest struct {
	GroupName string `json:"group_name"`
}

type SetGroupPhotoRequest struct {
	GroupIcon string `json:"group_icon"`
}

type SetGroupDescriptionRequest struct {
	Description string `json:"description"`
}

type AddParticipantsRequest struct {
	UserIDs []int `json:"user_ids"`
}

// SEZIONE 3 - MESSAGGI

type Message struct {
	ID          int        `json:"id"`
	ChatID      int        `json:"chat_id"`
	SenderID    int        `json:"sender_id"`
	Type        string     `json:"type"`
	Content     string     `json:"content"`
	MediaURL    string     `json:"media_url"`
	Timestamp   string     `json:"timestamp"`
	Status      string     `json:"status"`
	ReplyTo     *int       `json:"reply_to"`
	Reactions   []Reaction `json:"reactions"`
	IsForwarded bool       `json:"is_forwarded"`
}

type CreateMessageRequest struct {
	Type             string `json:"type"` // text, image, file, etc.
	Content          string `json:"content,omitempty"`
	MediaURL         string `json:"media_url,omitempty"`
	ReplyToMessageID *int   `json:"reply_to_message_id,omitempty"`
}

type UpdateMessageStatusRequest struct {
	Status string `json:"status"` // delivered, read
}

type ForwardMessageRequest struct {
	TargetChatIDs []int `json:"target_chat_ids"` // IDs delle chat di destinazione
}

type LastMessagePreview struct {
	Type      string `json:"type"`
	Content   string `json:"text,omitempty"` // Mappiamo 'content' su 'text' del JSON
	Timestamp string `json:"timestamp"`
}

// SEZIONE 4 - REAZIONI

type Reaction struct {
	ID        int    `json:"id"` // Nota: Nel DB non abbiamo un ID univoco per la reazione, useremo 0 o un hash
	MessageID int    `json:"message_id"`
	UserID    int    `json:"user_id"`
	UserName  string `json:"user_name"`
	EmojiCode string `json:"emoji_code"`
	CreatedAt string `json:"created_at"`
}

type CreateReactionRequest struct {
	EmojiCode string `json:"emoji_code"`
}

// SEZIONE ? - RISPOSTE DI ERRORE

type ErrorResponse struct {
	Code    string `json:"code"`
	Message string `json:"message"`
}

var ErrConflict = errors.New("conflict error")
