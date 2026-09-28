package database

import (
	"errors"
	"fmt"
	"time"

	"github.com/RomoloDef/WASAText/service/model"
)

// CommentMessage aggiunge o aggiorna una reazione a un messaggio e restituisce il NOME dell'utente.
func (db *appdbimpl) CommentMessage(userID int, chatID int, messageID int, emojiCode string) (model.Reaction, error) {
	// 1. Verifica che il messaggio esista nella chat specificata
	var exists bool
	err := db.c.QueryRow("SELECT EXISTS(SELECT 1 FROM messages WHERE id = ? AND chat_id = ?)", messageID, chatID).Scan(&exists)
	if err != nil {
		return model.Reaction{}, err
	}
	if !exists {
		return model.Reaction{}, errors.New("message not found in this chat")
	}

	// 2. Verifica che l'utente sia membro della chat
	err = db.c.QueryRow("SELECT EXISTS(SELECT 1 FROM chat_members WHERE chat_id = ? AND user_id = ?)", chatID, userID).Scan(&exists)
	if err != nil {
		return model.Reaction{}, err
	}
	if !exists {
		return model.Reaction{}, errors.New("user not authorized")
	}

	// 3. Inserisce o Sostituisce la reazione
	query := `
		INSERT INTO reactions (message_id, user_id, emoji_code, created_at)
		VALUES (?, ?, ?, CURRENT_TIMESTAMP)
		ON CONFLICT(message_id, user_id) DO UPDATE SET emoji_code = excluded.emoji_code, created_at = CURRENT_TIMESTAMP
	`
	_, err = db.c.Exec(query, messageID, userID, emojiCode)
	if err != nil {
		return model.Reaction{}, fmt.Errorf("error adding reaction: %w", err)
	}

	// 4. RECUPERA IL NOME UTENTE PER LA RISPOSTA
	// Viene effettuata una query per ottenere il nome, così il frontend può visualizzarlo subito.
	var userName string
	err = db.c.QueryRow("SELECT name FROM users WHERE id = ?", userID).Scan(&userName)
	if err != nil {
		return model.Reaction{}, fmt.Errorf("error fetching user name: %w", err)
	}

	// 5. Costruisce la risposta completa
	timestamp := time.Now().Format(time.RFC3339)

	return model.Reaction{
		ID:        0,
		MessageID: messageID,
		UserID:    userID,
		UserName:  userName,
		EmojiCode: emojiCode,
		CreatedAt: timestamp,
	}, nil
}

// UncommentMessage rimuove la reazione di un utente a un messaggio.
func (db *appdbimpl) UncommentMessage(userID int, chatID int, messageID int) error {
	// 1. Verifica esistenza messaggio/chat
	var exists bool
	err := db.c.QueryRow("SELECT EXISTS(SELECT 1 FROM messages WHERE id = ? AND chat_id = ?)", messageID, chatID).Scan(&exists)
	if err != nil {
		return err
	}
	if !exists {
		return errors.New("message not found in this chat")
	}

	// 2. Elimina la reazione
	res, err := db.c.Exec("DELETE FROM reactions WHERE message_id = ? AND user_id = ?", messageID, userID)
	if err != nil {
		return fmt.Errorf("error removing reaction: %w", err)
	}

	rows, err := res.RowsAffected()
	if err != nil {
		return err
	}
	if rows == 0 {
		return errors.New("reaction not found")
	}

	return nil
}
