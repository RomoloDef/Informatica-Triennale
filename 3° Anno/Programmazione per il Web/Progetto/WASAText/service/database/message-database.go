// service/database/message-database.go

package database

import (
	"database/sql"
	"errors"
	"fmt"
	"time"

	"github.com/RomoloDef/WASAText/service/model"
)

// SendMessage inserisce un nuovo messaggio nel database.
func (db *appdbimpl) SendMessage(senderID int, chatID int, req model.CreateMessageRequest) (model.Message, error) {
	// 1. Verifica che l'utente sia membro della chat
	var isMember bool
	// La query controlla se esiste una riga in chat_members che corrisponde a chatID e senderID
	err := db.c.QueryRow("SELECT EXISTS(SELECT 1 FROM chat_members WHERE chat_id = ? AND user_id = ?)", chatID, senderID).Scan(&isMember)
	if err != nil {
		return model.Message{}, fmt.Errorf("error checking chat membership: %w", err)
	}
	if !isMember {
		return model.Message{}, errors.New("user not authorized to send messages to this chat")
	}

	// 2. Inserisce il messaggio (reply_to è NULL qui, is_forwarded è 0)
	// La funzione NULLIF(?, '') mi serve a convertire stringhe vuote in NULL, così da gestire correttamente i campi opzionali
	query := `
		INSERT INTO messages (chat_id, sender_id, type, content, media_url, status, timestamp, reply_to, is_forwarded) 
		VALUES (?, ?, ?, NULLIF(?, ''), NULLIF(?, ''), 'delivered', CURRENT_TIMESTAMP, NULL, 0)
	`
	res, err := db.c.Exec(query, chatID, senderID, req.Type, req.Content, req.MediaURL)
	if err != nil {
		return model.Message{}, fmt.Errorf("error inserting message: %w", err)
	}

	msgID, err := res.LastInsertId()
	if err != nil {
		return model.Message{}, err
	}

	// 3. Aggiorna updated_at della chat
	// Questo è importante per l'ordinamento delle chat nella UI (ultima chat aggiornata in cima)
	_, _ = db.c.Exec("UPDATE chats SET updated_at = CURRENT_TIMESTAMP WHERE id = ?", chatID)

	// 4. Costruisce l'oggetto da restituire
	return model.Message{
		ID:          int(msgID),
		ChatID:      chatID,
		SenderID:    senderID,
		Type:        req.Type,
		Content:     req.Content,
		MediaURL:    req.MediaURL,
		Status:      "delivered",
		Timestamp:   time.Now().Format(time.RFC3339),
		ReplyTo:     nil, // Nessuna risposta
		IsForwarded: false,
		Reactions:   []model.Reaction{},
	}, nil
}

// GetMessages recupera i messaggi di una chat.
// Viene implementata anche la logica delle SPUNTE BLU .
func (db *appdbimpl) GetMessages(userID int, chatID int) ([]model.Message, error) {

	// --- LOGICA SPUNTE BLU ---

	// 1. Aggiorna l'istante di lettura dell'utente corrente per questa chat
	// Viene usato CURRENT_TIMESTAMP per dire "ho letto fino ad ora".
	// Tramite la query aggiorno il campo last_read_at nella tabella chat_members per questo utente e questa chat.
	_, err := db.c.Exec("UPDATE chat_members SET last_read_at = CURRENT_TIMESTAMP WHERE chat_id = ? AND user_id = ?", chatID, userID)
	if err != nil {
		return nil, fmt.Errorf("error updating last_read_at: %w", err)
	}

	// 2. Aggiorna lo stato dei messaggi a 'read'
	updateQuery := `
		UPDATE messages
		SET status = 'read'
		WHERE chat_id = ?
		AND status != 'read'
		AND datetime(timestamp) <= (
			SELECT MIN(datetime(last_read_at)) 
			FROM chat_members 
			WHERE chat_id = ?
		)
	`
	_, _ = db.c.Exec(updateQuery, chatID, chatID)

	// -------------------------------------

	// RECUPERO MESSAGGI

	// 3. Query Standard per recuperare i messaggi
	const query = `
		SELECT id, chat_id, sender_id, type, content, media_url, timestamp, status, reply_to, is_forwarded
		FROM messages 
		WHERE chat_id = ? 
		ORDER BY timestamp DESC
	`
	rows, err := db.c.Query(query, chatID)
	if err != nil {
		return nil, err
	}
	// Chiudo per evitare che il server esaurisca le connessioni al database. La chiusura avviene quando la funzione termina, anche in caso di errori.
	defer rows.Close()

	var messages []model.Message

	for rows.Next() {
		var m model.Message
		var content, mediaURL sql.NullString
		var replyTo sql.NullInt64

		err = rows.Scan(
			&m.ID,
			&m.ChatID,
			&m.SenderID,
			&m.Type,
			&content,
			&mediaURL,
			&m.Timestamp,
			&m.Status,
			&replyTo,
			&m.IsForwarded,
		)

		if err != nil {
			return nil, fmt.Errorf("error scanning message: %w", err)
		}

		if content.Valid {
			m.Content = content.String
		}
		if mediaURL.Valid {
			m.MediaURL = mediaURL.String
		}
		if replyTo.Valid {
			id := int(replyTo.Int64)
			m.ReplyTo = &id
		}

		// RECUPERO REAZIONI PER OGNI MESSAGGIO

		reactionQuery := `
			SELECT r.message_id, r.user_id, r.emoji_code, r.created_at, u.name 
			FROM reactions r
			JOIN users u ON r.user_id = u.id
			WHERE r.message_id = ?
		`
		reactionRows, err := db.c.Query(reactionQuery, m.ID)
		if err == nil {
			var reactions []model.Reaction
			// Itero sui risultati delle reazioni
			for reactionRows.Next() {
				var r model.Reaction
				// Scansiono i campi della reazione, incluso il nome dell'utente che ha reagito
				if err := reactionRows.Scan(&r.MessageID, &r.UserID, &r.EmojiCode, &r.CreatedAt, &r.UserName); err == nil {
					// Se la scansione è andata a buon fine, aggiungo la reazione alla lista delle reazioni del messaggio
					reactions = append(reactions, r)
				}
			}

			if err := reactionRows.Err(); err != nil {
				reactionRows.Close()
				return nil, fmt.Errorf("error iterating reactions: %w", err)
			}
			reactionRows.Close()
			m.Reactions = reactions
		} else {
			m.Reactions = []model.Reaction{}
		}

		messages = append(messages, m)
	}

	if err = rows.Err(); err != nil {
		return nil, err
	}

	return messages, nil
}

// DeleteMessage elimina un messaggio (solo se l'utente è il mittente).
func (db *appdbimpl) DeleteMessage(userID int, chatID int, messageID int) error {
	// Una semplice query di DELETE con condizioni su id, chat_id e sender_id per garantire che solo il mittente possa eliminare il messaggio.
	res, err := db.c.Exec("DELETE FROM messages WHERE id = ? AND chat_id = ? AND sender_id = ?", messageID, chatID, userID)
	if err != nil {
		return fmt.Errorf("error deleting message: %w", err)
	}

	rows, err := res.RowsAffected()
	if err != nil {
		return err
	}
	if rows == 0 {
		return errors.New("message not found or user not authorized to delete")
	}
	return nil
}

/*
// UpdateMessageStatus aggiorna lo stato di un messaggio.
func (db *appdbimpl) UpdateMessageStatus(userID int, chatID int, messageID int, newStatus string) (model.Message, error) {
	// Verifica appartenenza chat
	var isMember bool
	// La query controlla se esiste una riga in chat_members che corrisponde a chatID e userID
	err := db.c.QueryRow("SELECT EXISTS(SELECT 1 FROM chat_members WHERE chat_id = ? AND user_id = ?)", chatID, userID).Scan(&isMember)
	if err != nil {
		return model.Message{}, err
	}
	if !isMember {
		return model.Message{}, errors.New("user not authorized")
	}

	// Update
	res, err := db.c.Exec("UPDATE messages SET status = ? WHERE id = ? AND chat_id = ?", newStatus, messageID, chatID)
	if err != nil {
		return model.Message{}, fmt.Errorf("error updating message status: %w", err)
	}
	if rows, _ := res.RowsAffected(); rows == 0 {
		return model.Message{}, errors.New("message not found")
	}

	// Recupera il messaggio aggiornato per restituirlo
	var m model.Message
	var content, mediaURL sql.NullString
	var replyTo sql.NullInt64

	query := `SELECT id, chat_id, sender_id, type, content, media_url, status, timestamp, reply_to, is_forwarded
	          FROM messages WHERE id = ?`

	err = db.c.QueryRow(query, messageID).Scan(
		&m.ID, &m.ChatID, &m.SenderID, &m.Type, &content, &mediaURL, &m.Status, &m.Timestamp, &replyTo, &m.IsForwarded,
	)
	if err != nil {
		return model.Message{}, err
	}

	if content.Valid {
		m.Content = content.String
	}
	if mediaURL.Valid {
		m.MediaURL = mediaURL.String
	}
	if replyTo.Valid {
		id := int(replyTo.Int64)
		m.ReplyTo = &id
	}

	return m, nil
}
*/

// ReplyToMessage crea una risposta collegata a un messaggio padre.
func (db *appdbimpl) ReplyToMessage(senderID int, chatID int, parentMessageID int, req model.CreateMessageRequest) (model.Message, error) {
	// 1. Verifica esistenza messaggio padre
	var parentExists bool
	// Controllo con questa query che il messaggio a cui si vuole rispondere esista effettivamente ed è nella chat specificata
	err := db.c.QueryRow("SELECT EXISTS(SELECT 1 FROM messages WHERE id = ? AND chat_id = ?)", parentMessageID, chatID).Scan(&parentExists)
	if err != nil {
		return model.Message{}, err
	}
	if !parentExists {
		return model.Message{}, errors.New("parent message not found in this chat")
	}

	// 2. Verifica permessi
	var isMember bool
	// Per sicuerezza, controllo anche che l'utente sia membro della chat prima di permettergli di rispondere.
	err = db.c.QueryRow("SELECT EXISTS(SELECT 1 FROM chat_members WHERE chat_id = ? AND user_id = ?)", chatID, senderID).Scan(&isMember)
	if err != nil {
		return model.Message{}, err
	}
	if !isMember {
		return model.Message{}, errors.New("user not authorized")
	}

	// 3. Inserimento con reply_to popolato e is_forwarded=0
	query := `
		INSERT INTO messages (chat_id, sender_id, type, content, media_url, status, timestamp, reply_to, is_forwarded) 
		VALUES (?, ?, ?, NULLIF(?, ''), NULLIF(?, ''), 'sent', CURRENT_TIMESTAMP, ?, 0)
	`
	// A differenza di SendMessage, qui passo parentMessageID come valore per reply_to, e is_forwarded è sempre 0 perché è una risposta diretta.
	res, err := db.c.Exec(query, chatID, senderID, req.Type, req.Content, req.MediaURL, parentMessageID)
	if err != nil {
		return model.Message{}, fmt.Errorf("error inserting reply: %w", err)
	}

	msgID, err := res.LastInsertId()
	if err != nil {
		return model.Message{}, err
	}

	// Aggiorno la chat per portarla in cima alla lista
	_, _ = db.c.Exec("UPDATE chats SET updated_at = CURRENT_TIMESTAMP WHERE id = ?", chatID)

	// Costruzione risposta corretta
	return model.Message{
		ID:          int(msgID),
		ChatID:      chatID,
		SenderID:    senderID,
		Type:        req.Type,
		Content:     req.Content,
		MediaURL:    req.MediaURL,
		Status:      "sent",
		Timestamp:   time.Now().Format(time.RFC3339),
		ReplyTo:     &parentMessageID,
		IsForwarded: false,
	}, nil
}

// ForwardMessage inoltra un messaggio.
func (db *appdbimpl) ForwardMessage(senderID int, sourceChatID int, sourceMessageID int, targetChatIDs []int) ([]model.Message, error) {
	// Verifica chat sorgente
	var isSourceMember bool
	// La query controlla che si abbia il permesso di vedere il messaggio originale. Se non si è nella chat di origine, non puoi inoltrarlo.
	err := db.c.QueryRow("SELECT EXISTS(SELECT 1 FROM chat_members WHERE chat_id = ? AND user_id = ?)", sourceChatID, senderID).Scan(&isSourceMember)
	if err != nil {
		return nil, err
	}
	if !isSourceMember {
		return nil, errors.New("source chat not found or user not authorized")
	}

	// Recupera messaggio originale
	var originalMsg model.Message
	var content, mediaURL sql.NullString
	queryOrig := `SELECT type, content, media_url FROM messages WHERE id = ? AND chat_id = ?`
	err = db.c.QueryRow(queryOrig, sourceMessageID, sourceChatID).Scan(&originalMsg.Type, &content, &mediaURL)
	if err != nil {
		if errors.Is(err, sql.ErrNoRows) {
			return nil, errors.New("original message not found")
		}
		return nil, fmt.Errorf("error fetching original message: %w", err)
	}

	// Apro la Transazione:
	// Se l'inoltro fallisce alla terza chat su cinque, vogliamo che fallisca tutto o gestirlo in blocco.
	// Per questo motivo uso una transazione: se qualcosa va storto, posso fare rollback e mantenere il database in uno stato consistente.
	tx, err := db.c.Begin()
	if err != nil {
		return nil, err
	}
	defer func() {
		if err != nil {
			_ = tx.Rollback()
		}
	}()

	var forwardedMessages []model.Message

	// Per ogni chat bisogna:
	// 1. Controllare se si è membro della chat dove vuoi inoltrare. Non si può "spammare" in gruppi dove non sei presente.
	// 2. Inserire il clone del messaggio originale con is_forwarded = 1. Il campo reply_to sarà NULL perché non è una risposta, e il timestamp sarà quello dell'inoltro, non dell'originale.
	// 3. Aggiornare updated_at della chat di destinazione per portarla in cima alla lista.
	// 4. Costruire l'oggetto Message da restituire, che avrà un nuovo ID, il chat_id della chat di destinazione, sender_id uguale a chi inoltra, type/content/media_url uguali all'originale, status 'delivered', timestamp dell'inoltro, reply_to NULL e is_forwarded true.
	// 5. Aggiungere il messaggio inoltrato alla lista da restituire.
	for _, targetChatID := range targetChatIDs {
		// Verifica chat destinazione
		var isTargetMember bool
		// STEP 1: controllo che l'utente sia membro della chat di destinazione. Se non è membro, non può inoltrare lì.
		err = tx.QueryRow("SELECT EXISTS(SELECT 1 FROM chat_members WHERE chat_id = ? AND user_id = ?)", targetChatID, senderID).Scan(&isTargetMember)
		if err != nil {
			return nil, err
		}
		if !isTargetMember {
			return nil, fmt.Errorf("user not authorized to post in target chat %d", targetChatID)
		}
		// STEP 2: Inserimento del messaggio inoltrato con is_forwarded = 1. Il campo reply_to è NULL perché non è una risposta, e il timestamp sarà quello dell'inoltro (CURRENT_TIMESTAMP).
		// Inserimento con is_forwarded = 1
		queryInsert := `
			INSERT INTO messages (chat_id, sender_id, type, content, media_url, status, timestamp, reply_to, is_forwarded) 
			VALUES (?, ?, ?, ?, ?, 'delivered', CURRENT_TIMESTAMP, NULL, 1)
		`
		res, err := tx.Exec(queryInsert, targetChatID, senderID, originalMsg.Type, content, mediaURL)
		if err != nil {
			return nil, fmt.Errorf("error inserting forwarded message: %w", err)
		}

		newMsgID, err := res.LastInsertId()
		if err != nil {
			return nil, err
		}
		// STEP 3: aggiorno updated_at della chat di destinazione per portarla in cima alla lista. Anche se stiamo inoltrando un messaggio, dal punto di vista della chat è come se fosse un nuovo messaggio, quindi aggiorniamo updated_at.
		_, _ = tx.Exec("UPDATE chats SET updated_at = CURRENT_TIMESTAMP WHERE id = ?", targetChatID)

		// STEP 4: costruzione oggetto Message da restituire
		ts := time.Now().Format(time.RFC3339)
		newMsg := model.Message{
			ID:          int(newMsgID),
			ChatID:      targetChatID,
			SenderID:    senderID,
			Type:        originalMsg.Type,
			Status:      "delivered",
			Timestamp:   ts,
			ReplyTo:     nil,
			IsForwarded: true,
		}
		if content.Valid {
			newMsg.Content = content.String
		}
		if mediaURL.Valid {
			newMsg.MediaURL = mediaURL.String
		}

		// STEP 5: aggiungo alla lista dei messaggi inoltrati da restituire
		forwardedMessages = append(forwardedMessages, newMsg)
	}

	// Se si è arrivati fin qui, significa che tutto è andato bene, quindi commit della transazione.
	// Se qualcosa fosse andato storto, il defer si sarebbe occupato di fare rollback.
	if err = tx.Commit(); err != nil {
		return nil, err
	}

	return forwardedMessages, nil
}
