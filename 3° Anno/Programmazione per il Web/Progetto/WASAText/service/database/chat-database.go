package database

import (
	"database/sql"
	"errors"
	"fmt"

	"github.com/RomoloDef/WASAText/service/model"
)

var (
	ErrInvalidParticipant = errors.New("participant is invalid or does not exist")
	ErrChatExists         = errors.New("individual chat already exists between these users")
)

// CreateConversation crea una nuova chat.
func (db *appdbimpl) CreateConversation(creatorID int, req model.CreateChatRequest) (model.Chat, error) {
	// Inizia la transazione tramite il costrutto Begin/Commit/Rollback
	tx, err := db.c.Begin()
	if err != nil {
		return model.Chat{}, fmt.Errorf("error starting transaction: %w", err)
	}
	// Assicura che in caso di errore la transazione venga annullata tramite il costrutto Rollback
	defer func() {
		if err != nil {
			_ = tx.Rollback()
		}
	}()

	// 1. Verifica esistenza partecipanti
	// Poichè è all'interno di una transazione, utilizzo tx.QueryRow invece di db.c.QueryRow
	for _, participantID := range req.ParticipantsIDs {
		var exists bool
		err = tx.QueryRow(`SELECT EXISTS(SELECT 1 FROM users WHERE id = ?)`, participantID).Scan(&exists)
		if err != nil {
			return model.Chat{}, fmt.Errorf("error checking participant: %w", err)
		}
		if !exists {
			return model.Chat{}, ErrInvalidParticipant
		}
	}

	// 2. Verifica duplicati (Solo per Individuali)
	if req.Type == ChatTypeIndividual {
		p1 := req.ParticipantsIDs[0]
		p2 := req.ParticipantsIDs[1]
		if p1 > p2 {
			p1, p2 = p2, p1
		}
		var existingChatID int
		// Cerca se esiste già una chat individuale con questi due membri esatti
		checkQuery := `
            SELECT T1.chat_id 
            FROM chat_members AS T1
            JOIN chats AS T_CHAT ON T1.chat_id = T_CHAT.id
            WHERE T_CHAT.type = 'individual'
            AND T1.user_id IN (?, ?) 
            GROUP BY T1.chat_id 
            HAVING COUNT(T1.user_id) = 2
            AND (SELECT COUNT(*) FROM chat_members WHERE chat_id = T1.chat_id) = 2;
        `
		err = tx.QueryRow(checkQuery, p1, p2).Scan(&existingChatID)
		if err == nil {
			// Trovata! Restituisce errore speciale che l'handler gestirà
			return model.Chat{ID: existingChatID}, ErrChatExists
		} else if !errors.Is(err, sql.ErrNoRows) {
			return model.Chat{}, err
		}
	}

	// 3. Inserimento Chat
	var chatName, chatPhotoURL, chatDescription string

	// Solo i gruppi hanno nome e foto persistenti nel DB
	if req.Type == ChatTypeGroup {
		chatName = req.GroupName
		chatPhotoURL = req.GroupIcon
		chatDescription = req.Description
	}

	res, err := tx.Exec(
		`INSERT INTO chats (type, group_name, group_photo_url, group_description) VALUES (?, NULLIF(?, ''), NULLIF(?, ''), NULLIF(?, ''))`,
		req.Type, chatName, chatPhotoURL, chatDescription,
	)
	if err != nil {
		return model.Chat{}, fmt.Errorf("error inserting chat: %w", err)
	}

	newChatID, err := res.LastInsertId()
	if err != nil {
		return model.Chat{}, err
	}

	// 4. Inserimento Membri
	for _, participantID := range req.ParticipantsIDs {
		isAdmin := (req.Type == ChatTypeGroup && participantID == creatorID)
		_, err = tx.Exec(`INSERT INTO chat_members (chat_id, user_id, is_admin) VALUES (?, ?, ?)`, newChatID, participantID, isAdmin)
		if err != nil {
			return model.Chat{}, err
		}
	}

	// 5. Commit della transazione
	if err = tx.Commit(); err != nil {
		return model.Chat{}, err
	}

	// Ritorna la chat ricaricandola con la logica corretta
	return db.GetConversation(creatorID, int(newChatID))
}

// GetMyConversations recupera la lista delle conversazioni.
func (db *appdbimpl) GetMyConversations(userID int) ([]model.Chat, error) {
	var chats []model.Chat

	// 1. Query principale: recupera le chat dell'utente
	query := `
		SELECT c.id, c.type, c.group_name, c.group_photo_url
		FROM chats c
		JOIN chat_members cm ON c.id = cm.chat_id
		WHERE cm.user_id = ?
		ORDER BY c.updated_at DESC
	`

	rows, err := db.c.Query(query, userID)
	if err != nil {
		return nil, fmt.Errorf("error querying user chats: %w", err)
	}
	defer rows.Close()

	for rows.Next() {
		var c model.Chat
		var groupName, groupPhoto sql.NullString

		if err := rows.Scan(&c.ID, &c.Type, &groupName, &groupPhoto); err != nil {
			return nil, err
		}

		// Assegniamo i dati del database
		if groupName.Valid {
			c.Name = groupName.String
		}
		if groupPhoto.Valid {
			c.PhotoURL = groupPhoto.String
		}

		// 2. RECUPERO MEMBRI CHAT
		membersRows, err := db.c.Query(`
			SELECT u.id, u.name, u.photo_url 
			FROM users u 
			JOIN chat_members cm ON u.id = cm.user_id 
			WHERE cm.chat_id = ?`, c.ID)

		if err == nil {
			for membersRows.Next() {
				var u model.User
				var ph sql.NullString
				if err := membersRows.Scan(&u.ID, &u.Name, &ph); err == nil {
					if ph.Valid {
						u.PhotoURL = ph.String
					}
					c.Members = append(c.Members, u)
				}
			}

			if err := membersRows.Err(); err != nil {
				membersRows.Close()
				return nil, fmt.Errorf("error iterating chat members: %w", err)
			}
			membersRows.Close()
		}

		// 3. RECUPERO ANTEPRIMA ULTIMO MESSAGGIO
		var lastMsg model.LastMessagePreview
		var content sql.NullString

		msgQuery := `
			SELECT type, content, timestamp 
			FROM messages 
			WHERE chat_id = ? 
			ORDER BY timestamp DESC, id DESC 
			LIMIT 1
		`
		err = db.c.QueryRow(msgQuery, c.ID).Scan(&lastMsg.Type, &content, &lastMsg.Timestamp)

		if err == nil {
			if content.Valid {
				lastMsg.Content = content.String
			} else {
				lastMsg.Content = ""
			}
			c.LastMessage = &lastMsg
		}

		chats = append(chats, c)
	}

	if err = rows.Err(); err != nil {
		return nil, err
	}

	return chats, nil
}

// GetConversation recupera dettaglio singola chat
func (db *appdbimpl) GetConversation(userID int, chatID int) (model.Chat, error) {
	var c model.Chat

	// 1. Info Chat di base
	query := `
		SELECT c.id, c.type, c.group_name, c.group_photo_url, c.group_description
		FROM chats c
		JOIN chat_members cm ON c.id = cm.chat_id
		WHERE c.id = ? AND cm.user_id = ?
	`
	var groupName, groupPhoto, groupDesc sql.NullString

	// Esegue la query
	err := db.c.QueryRow(query, chatID, userID).Scan(&c.ID, &c.Type, &groupName, &groupPhoto, &groupDesc)
	if err != nil {
		if errors.Is(err, sql.ErrNoRows) {
			return model.Chat{}, errors.New(ErrMsgChatNotFound)
		}
		return model.Chat{}, err
	}

	// Assegna i valori se presenti (devono essere validi)
	if groupName.Valid {
		c.Name = groupName.String
	}
	if groupPhoto.Valid {
		c.PhotoURL = groupPhoto.String
	}
	if groupDesc.Valid {
		c.Description = groupDesc.String
	}

	// 2. Recupera Membri
	mQuery := `SELECT u.id, u.name, u.photo_url FROM users u JOIN chat_members cm ON u.id = cm.user_id WHERE cm.chat_id = ?`
	rows, err := db.c.Query(mQuery, chatID)
	if err != nil {
		return model.Chat{}, err
	}
	defer rows.Close()

	for rows.Next() {
		var u model.User
		var ph sql.NullString
		if err := rows.Scan(&u.ID, &u.Name, &ph); err == nil {
			if ph.Valid {
				u.PhotoURL = ph.String
			}
			c.Members = append(c.Members, u)
		}
	}

	if err := rows.Err(); err != nil {
		return model.Chat{}, fmt.Errorf("error iterating chat members: %w", err)
	}

	// 3. Logica Swap Nome (per chat individuali)
	// Se è una chat a due, sovrascrive nome e foto con quelli dell'altro utente
	if c.Type == ChatTypeIndividual {
		for _, member := range c.Members {
			if member.ID != userID {
				c.Name = member.Name
				c.PhotoURL = member.PhotoURL
				break
			}
		}
	}

	return c, nil
}

func (db *appdbimpl) SetGroupName(userID int, chatID int, newName string) (model.Chat, error) {
	_, err := db.c.Exec("UPDATE chats SET group_name = ? WHERE id = ?", newName, chatID)
	if err != nil {
		return model.Chat{}, err
	}
	return db.GetConversation(userID, chatID)
}

func (db *appdbimpl) SetGroupPhoto(userID int, chatID int, photoURL string) (model.Chat, error) {
	_, err := db.c.Exec("UPDATE chats SET group_photo_url = NULLIF(?, '') WHERE id = ?", photoURL, chatID)
	if err != nil {
		return model.Chat{}, err
	}
	return db.GetConversation(userID, chatID)
}

func (db *appdbimpl) DeleteConversation(userID int, chatID int) error {
	res, err := db.c.Exec("DELETE FROM chats WHERE id = ?", chatID)
	if err != nil {
		return err
	}
	if n, _ := res.RowsAffected(); n == 0 {
		return errors.New(ErrMsgChatNotFound)
	}
	return nil
}

func (db *appdbimpl) IsGroupAdmin(chatID int, userID int) (bool, error) {
	var isAdmin bool
	err := db.c.QueryRow("SELECT is_admin FROM chat_members WHERE chat_id = ? AND user_id = ?", chatID, userID).Scan(&isAdmin)
	if err != nil {
		if errors.Is(err, sql.ErrNoRows) {
			return false, nil
		}
		return false, err
	}
	return isAdmin, nil
}

func (db *appdbimpl) AddToGroup(chatID int, userIDs []int) error {
	for _, uid := range userIDs {
		_, err := db.c.Exec("INSERT OR IGNORE INTO chat_members (chat_id, user_id, is_admin) VALUES (?, ?, 0)", chatID, uid)
		if err != nil {
			return err
		}
	}
	return nil
}

func (db *appdbimpl) LeaveGroup(chatID int, userID int) error {
	res, err := db.c.Exec("DELETE FROM chat_members WHERE chat_id = ? AND user_id = ?", chatID, userID)
	if err != nil {
		return err
	}
	if n, _ := res.RowsAffected(); n == 0 {
		return errors.New("error leaving group")
	}
	return nil
}

// SetGroupDescription aggiorna la descrizione del gruppo
func (db *appdbimpl) SetGroupDescription(userID int, chatID int, description string) (model.Chat, error) {
	// Verifica che sia un gruppo e che l'utente sia membro
	// Aggiorna solo se l'utente è membro
	// Si permette a tutti i membri di cambiare descrizione

	_, err := db.c.Exec("UPDATE chats SET group_description = NULLIF(?, '') WHERE id = ?", description, chatID)
	if err != nil {
		return model.Chat{}, fmt.Errorf("error updating description: %w", err)
	}
	return db.GetConversation(userID, chatID)
}
