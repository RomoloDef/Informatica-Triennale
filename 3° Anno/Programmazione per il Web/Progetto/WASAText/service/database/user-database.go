package database

import (
	"database/sql"
	"errors"
	"fmt"

	"github.com/RomoloDef/WASAText/service/model"
)

// DoLogin implementa la logica "find or create" per il Simplified Login.
// Se l'utente con quel 'name' esiste, lo restituisce; altrimenti, ne crea uno nuovo.

func (db *appdbimpl) DoLogin(name string) (model.User, error) {
	var user model.User

	// 1. Variabili per lo Scan: Uso sql.NullString per gestire la colonna photo_url che può essere NULL nel Database.
	var photoURL sql.NullString

	// 2. La funzione tenta di trovare l'utente per nome
	const selectQuery = "SELECT id, name, photo_url FROM users WHERE name = ?"
	// Variabile err per capire se la query ha trovato un utente o no
	err := db.c.QueryRow(selectQuery, name).
		Scan(&user.ID, &user.Name, &photoURL)
	// Se non c'è un utente con quel nome, allora posso usare la photoURL come stringa vuota per il nuovo utente,
	// altrimenti la popolo con il valore del DB.
	if err == nil {
		// Utente Trovato: Popola PhotoURL
		if photoURL.Valid {
			user.PhotoURL = photoURL.String
		} else {
			user.PhotoURL = ""
		}
		return user, nil
	}

	if errors.Is(err, sql.ErrNoRows) {
		// Utente NON Trovato: Esegui la registrazione (Insert)

		// 1. Inserisci il nuovo utente. photo_url sarà NULL.
		const insertQuery = "INSERT INTO users (name) VALUES (?)"
		res, err := db.c.Exec(insertQuery, name)
		if err != nil {
			// Questo gestisce eventuali errori di inserimento
			return user, fmt.Errorf("error creating user: %w", err)
		}

		// 2. Recupera l'ID generato da AUTOINCREMENT
		newID, err := res.LastInsertId()
		if err != nil {
			return user, fmt.Errorf("error retrieving new user ID: %w", err)
		}

		// 3. Popola l'oggetto utente da restituire
		newUser := model.User{
			ID:       int(newID),
			Name:     name,
			PhotoURL: "", // Nuovi utenti all'inizio non hanno una foto
		}

		return newUser, nil
	}

	// 4. Errore generico del database (es. connessione fallita)
	return user, fmt.Errorf("error during DoLogin database operation: %w", err)
}

// UpdateUserName gestisce la PUT /users/me/name.
// Controlla se il nome è già preso prima di aggiornare.
func (db *appdbimpl) UpdateUserName(userID int, newName string) error {
	// 1. Verifico se il nome è già preso da un altro utente
	var existingID int
	// Effettuo la query per cercare un utente con lo stesso nome. Se ne trova uno,
	// tramite il costrutto Scan, copio il suo ID in existingID.
	err := db.c.QueryRow("SELECT id FROM users WHERE name = ?", newName).Scan(&existingID)

	if err == nil && existingID != userID {
		// Nome trovato e appartiene a un altro utente
		return model.ErrConflict
	}
	if err != nil && !errors.Is(err, sql.ErrNoRows) {
		return fmt.Errorf("error checking existing name: %w", err)
	}

	// 2. Aggiorna il nome
	// Exec ritorna un Result che contiene il numero di righe affette dall'update, utile per verificare che l'utente esista.
	res, err := db.c.Exec("UPDATE users SET name = ? WHERE id = ?", newName, userID)
	if err != nil {
		return fmt.Errorf("error updating username: %w", err)
	}

	// Tramite il costrutto RowsAffected, che mi restituisce il numero di righe modificate dall'update,
	// posso verificare se l'utente esisteva o no
	rowsAffected, err := res.RowsAffected()
	if err != nil {
		return fmt.Errorf("error checking rows affected: %w", err)
	}
	if rowsAffected == 0 {
		return errors.New("user not found (should not happen if authenticated)")
	}

	return nil
}

// UpdateUserPhoto gestisce la PUT /users/me/photo.
func (db *appdbimpl) UpdateUserPhoto(userID int, photoURL string) error {
	// Aggiorna la photo_url
	// Con il costrutto Exec, ottengo un result che mi permette di verificare se l'update ha modificato qualche riga, utile per capire se l'utente esiste o no.
	// Result è il numero di righe modificate dall'update, se è 0 significa che l'utente non esisteva (cosa che non dovrebbe succedere se è autenticato).
	res, err := db.c.Exec("UPDATE users SET photo_url = ? WHERE id = ?", photoURL, userID)
	if err != nil {
		return fmt.Errorf("error updating user photo: %w", err)
	}

	// Stessa logica di verifica dell'esistenza dell'utente tramite RowsAffected del result dell'update.
	rowsAffected, err := res.RowsAffected()
	if err != nil {
		return fmt.Errorf("error checking rows affected: %w", err)
	}
	if rowsAffected == 0 {
		return errors.New("user not found (should not happen if authenticated)")
	}

	return nil
}

// SearchUsers gestisce la GET /users/search.
// Cerca utenti il cui nome inizia con la query.
func (db *appdbimpl) SearchUsers(query string) ([]model.User, error) {
	// Uso LIKE ? || '%' per cercare nomi che iniziano con la query

	rows, err := db.c.Query("SELECT id, name, photo_url FROM users WHERE name LIKE ? || '%' LIMIT 20", query)
	if err != nil {
		return nil, fmt.Errorf("error querying users: %w", err)
	}
	defer rows.Close()

	var users []model.User
	for rows.Next() {
		var u model.User
		var photoURL sql.NullString

		err = rows.Scan(&u.ID, &u.Name, &photoURL)
		if err != nil {
			return nil, fmt.Errorf("error scanning user: %w", err)
		}

		if photoURL.Valid {
			u.PhotoURL = photoURL.String
		} else {
			u.PhotoURL = ""
		}

		users = append(users, u)
	}

	if err = rows.Err(); err != nil {
		return nil, fmt.Errorf("error during rows iteration: %w", err)
	}

	return users, nil
}

// DeleteUserPhoto gestisce la DELETE /users/me/photo, impostando photo_url a NULL
func (db *appdbimpl) DeleteUserPhoto(userID int) error {
	// 1. Aggiorna la colonna photo_url a NULL tramite la seguente query
	res, err := db.c.Exec("UPDATE users SET photo_url = NULL WHERE id = ?", userID)
	if err != nil {
		return fmt.Errorf("error deleting user photo URL: %w", err)
	}
	// 2. Verifica che l'update abbia modificato una riga, altrimenti l'utente non esisteva (cosa che non dovrebbe succedere se è autenticato)
	rowsAffected, err := res.RowsAffected()
	if err != nil {
		return fmt.Errorf("error checking rows affected: %w", err)
	}
	if rowsAffected == 0 {
		return errors.New("user not found (should not happen if authenticated)")
	}

	return nil
}

// DeleteUser gestisce la DELETE /users/me, eliminando l'utente.
func (db *appdbimpl) DeleteUser(userID int) error {
	// 1. Elimina l'utente
	res, err := db.c.Exec("DELETE FROM users WHERE id = ?", userID)
	if err != nil {
		return fmt.Errorf("error deleting user: %w", err)
	}

	rowsAffected, err := res.RowsAffected()
	if err != nil {
		return fmt.Errorf("error checking rows affected: %w", err)
	}
	if rowsAffected == 0 {
		return errors.New("user not found for deletion")
	}

	return nil
}

// GetUserById è una funzione di supporto per recuperare un utente per ID, usata ad esempio dopo l'aggiornamento del profilo.
func (db *appdbimpl) GetUserById(id int) (model.User, error) {
	var user model.User
	var photoURL sql.NullString

	// Query che cerca per ID
	err := db.c.QueryRow("SELECT id, name, photo_url FROM users WHERE id = ?", id).Scan(&user.ID, &user.Name, &photoURL)

	if err != nil {
		return model.User{}, err
	}

	if photoURL.Valid {
		user.PhotoURL = photoURL.String
	}
	return user, nil
}
