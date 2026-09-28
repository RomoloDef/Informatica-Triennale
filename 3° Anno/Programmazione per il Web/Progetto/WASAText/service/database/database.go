/*
Package database is the middleware between the app database and the code. All data (de)serialization (save/load) from a
persistent database are handled here. Database specific logic should never escape this package.

To use this package you need to apply migrations to the database if needed/wanted, connect to it (using the database
data source name from config), and then initialize an instance of AppDatabase from the DB connection.

For example, this code adds a parameter in `webapi` executable for the database data source name (add it to the
main.WebAPIConfiguration structure):

	DB struct {
		Filename string `conf:""`
	}

This is an example on how to migrate the DB and connect to it:

	// Start Database
	logger.Println("initializing database support")
	db, err := sql.Open("sqlite3", "./foo.db")
	if err != nil {
		logger.WithError(err).Error("error opening SQLite DB")
		return fmt.Errorf("opening SQLite: %w", err)
	}
	defer func() {
		logger.Debug("database stopping")
		_ = db.Close()
	}()

Then you can initialize the AppDatabase and pass it to the api package.
*/
package database

import (
	"database/sql"
	"errors"
	"fmt"

	"github.com/RomoloDef/WASAText/service/model"
)

const (
	ChatTypeGroup      = "group"
	ChatTypeIndividual = "individual"
	ErrMsgChatNotFound = "chat not found or user not authorized"
)

// AppDatabase is the high level interface for the DB
type AppDatabase interface {
	// SEZIONE 1 - Utenti
	DoLogin(name string) (model.User, error)
	GetUserById(id int) (model.User, error)
	UpdateUserName(userID int, newName string) error
	UpdateUserPhoto(userID int, photoURL string) error
	SearchUsers(query string) ([]model.User, error)
	DeleteUserPhoto(userID int) error
	DeleteUser(userID int) error
	// SEZIONE 2 - Chat
	CreateConversation(creatorID int, req model.CreateChatRequest) (model.Chat, error)
	GetMyConversations(userID int) ([]model.Chat, error)
	GetConversation(userID int, chatID int) (model.Chat, error)
	SetGroupName(userID int, chatID int, newName string) (model.Chat, error)
	SetGroupPhoto(userID int, chatID int, photoURL string) (model.Chat, error)
	SetGroupDescription(userID int, chatID int, description string) (model.Chat, error)
	DeleteConversation(userID int, chatID int) error
	IsGroupAdmin(chatID int, userID int) (bool, error)
	AddToGroup(chatID int, userIDs []int) error
	LeaveGroup(chatID int, userID int) error
	// SEZIONE 3 - Messaggi
	SendMessage(senderID int, chatID int, req model.CreateMessageRequest) (model.Message, error)
	GetMessages(userID int, chatID int) ([]model.Message, error)
	DeleteMessage(userID int, chatID int, messageID int) error
	// UpdateMessageStatus(userID int, chatID int, messageID int, newStatus string) (model.Message, error)
	ReplyToMessage(senderID int, chatID int, parentMessageID int, req model.CreateMessageRequest) (model.Message, error)
	ForwardMessage(senderID int, sourceChatID int, sourceMessageID int, targetChatIDs []int) ([]model.Message, error)
	// SEZIONE 4 - Reazioni
	CommentMessage(userID int, chatID int, messageID int, emojiCode string) (model.Reaction, error)
	UncommentMessage(userID int, chatID int, messageID int) error

	Ping() error
}

type appdbimpl struct {
	c *sql.DB
}

// New returns a new instance of AppDatabase based on the SQLite connection `db`.
// `db` is required - an error will be returned if `db` is `nil`.
func New(db *sql.DB) (AppDatabase, error) {
	if db == nil {
		return nil, errors.New("database is required when building a AppDatabase")
	}

	// QUERY DI CREAZIONE TABELLE
	// TABELLA UTENTI
	usersTableSQL := `
	CREATE TABLE IF NOT EXISTS users (
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		name TEXT NOT NULL,
		photo_url TEXT
	);`

	// TABELLA CHAT
	chatsTableSQL := `
	CREATE TABLE IF NOT EXISTS chats (
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		name TEXT,
		type TEXT NOT NULL CHECK(type IN ('individual', 'group')),
		group_name TEXT,
		group_photo_url TEXT,
		group_description TEXT,
		created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
		updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
	);`

	// TABELLA PARTECIPANTI CHAT
	chatMembersTableSQL := `
	CREATE TABLE IF NOT EXISTS chat_members (
		chat_id INTEGER NOT NULL,
		user_id INTEGER NOT NULL,
		is_admin BOOLEAN NOT NULL DEFAULT FALSE,
		last_read_at DATETIME DEFAULT CURRENT_TIMESTAMP,
		PRIMARY KEY (chat_id, user_id),
		FOREIGN KEY (chat_id) REFERENCES chats(id) ON DELETE CASCADE,
		FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
	);`

	// TABELLA MESSAGGI
	messagesTableSQL := `
	CREATE TABLE IF NOT EXISTS messages (
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		chat_id INTEGER NOT NULL,
		sender_id INTEGER NOT NULL,
		type TEXT NOT NULL CHECK(type IN ('text', 'image', 'video', 'file')),
		content TEXT,
		media_url TEXT,
		reply_to INTEGER,
		timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
		status TEXT NOT NULL CHECK(status IN ('sent', 'delivered', 'read')),
		is_forwarded BOOLEAN DEFAULT FALSE,
		FOREIGN KEY (chat_id) REFERENCES chats(id) ON DELETE CASCADE,
		FOREIGN KEY (sender_id) REFERENCES users(id) ON DELETE CASCADE,
		FOREIGN KEY (reply_to) REFERENCES messages(id) ON DELETE SET NULL -- <--- E QUESTO VINCOLO
	);`

	// TABELLA REAZIONI
	reactionsTableSQL := `
	CREATE TABLE IF NOT EXISTS reactions (
		message_id INTEGER NOT NULL,
		user_id INTEGER NOT NULL,
		emoji_code TEXT NOT NULL,
		created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
		PRIMARY KEY (message_id, user_id),
		FOREIGN KEY (message_id) REFERENCES messages(id) ON DELETE CASCADE,
		FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
	);`

	// ESECUZIONE QUERY DI CREAZIONE TABELLE
	tables := []string{
		usersTableSQL,
		chatsTableSQL,
		chatMembersTableSQL,
		messagesTableSQL,
		reactionsTableSQL,
	}

	for _, sqlStmt := range tables {
		_, err := db.Exec(sqlStmt)
		if err != nil {
			return nil, fmt.Errorf("error creating database tables: %w", err)
		}
	}

	return &appdbimpl{c: db}, nil
}

func (db *appdbimpl) Ping() error {
	return db.c.Ping()
}
