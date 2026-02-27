package api

import (
	"github.com/julienschmidt/httprouter"
	"net/http"
	"encoding/json"
	"math/rand"
)





// Start a new game generating the secret number 
// and return the created game id
func (rt *_router) startNewGame(w http.ResponseWriter, r *http.Request, ps httprouter.Params) {
	w.Header().Set("content-type", "application/json")
    
	id := len(Games)

	Games = append(Games,Game{
		Id: id,
		secret: rand.Intn(100),
		Outcome: "",
		Guesses: 0,
	})

	gamesGuesses = append(gamesGuesses,[]Guess{})

	json.NewEncoder(w).Encode(id)
}
