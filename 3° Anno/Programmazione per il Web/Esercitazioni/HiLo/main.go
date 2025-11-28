/*

ESERCIZIO: BACKEND API per "Hilo"

Metodo.        Percorso.			Azione.     					    Risposta(JSON).
POST.          /games.				Avvia una nuova partita. 		    { "game_id": "ID_UNIVOCO_GIOCO"}

POST 		   /games/{id}/guess	Invia un tentativo.                 { "result": "hi"} (o "lo" o "correct")

GET			   /games/{id}			Ottieni lo stato della partita.     { "status": "in_progress", "attempts": NUMERO_TENTATIVI }

NOTE:

1. POST/GAMES
   - Genera un numero segreto (es rand.Intn(100) + 1)
   - Genera un ID univoco per la partita (es un contatore o fmt.Sprintf)
   - Creare la nuova GameState
   - Bloccare il Mutex
   - Salvare la nuova partita nella mappa games
   - Sbloccare il Mutex
   - Rispondere al client con il JSON contenente il game_id

2. POST/GAMES/{id}/GUESS
   - Ottenere {id} dal percorso (usando mux.Vars(r))
   - Leggere il JSON dal corpo (r.Body) per ottenere il tentativo del client
   - Bloccare il Mutex (o .mu.RLock() se si usa RWMutex)
   - Recuperare lo stato della partita (games[id])
   - Sbloccare il Mutex (o .mu.RUnlock() se si usa RWMutex)
   - Controllare se lo stato esiste (errore 404 se non esiste)
   - Confrontare il tentativo con SecretNumber e definire la risposta ("hi", "lo", "correct")
   - (Opezionale) Aggiornare lo stato con il nuovo tentativo della partita (richiederà mu.Lock())
   - Rispondere al client con il JSON contenente il risultato

*/

package main

func main() {

}
