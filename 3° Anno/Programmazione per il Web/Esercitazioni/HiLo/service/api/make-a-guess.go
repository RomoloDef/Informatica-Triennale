package api

import (
	"github.com/julienschmidt/httprouter"
	"net/http"
	"encoding/json"
	"strconv"
)





// Try to guess the secret number; return hi, lo, or correct, 
// plus the guess count.
func (rt *_router) makeAGuess(w http.ResponseWriter, r *http.Request, ps httprouter.Params) {
	w.Header().Set("content-type", "application/json")
    
	id, err := strconv.Atoi(ps.ByName("id"))
	if err != nil {
		w.WriteHeader(http.StatusBadRequest)
		return
	}
	if id < 0 || id >= len(Games) {
		w.WriteHeader(http.StatusNotFound)
		return
	}
	if Games[id].Guesses == 10 || Games[id].Outcome != ""{
		w.WriteHeader(http.StatusForbidden)
		return
	}
	guessString := r.URL.Query().Get("guess")
	guessValue, err := strconv.Atoi(guessString)
	if err != nil {
		w.WriteHeader(http.StatusBadRequest)
		return
	}
	if guessValue < 0 || guessValue > 100 {
		w.WriteHeader(http.StatusNotAcceptable)
		return
	}

	Games[id].Guesses++
	newGuess := Guess{
		GuessCount: Games[id].Guesses,
		GuessOutcome: "",
		GuessValue: guessValue,
	}

	if guessValue == Games[id].secret {
		Games[id].Outcome = "win"
		newGuess.GuessOutcome = "correct"
		json.NewEncoder(w).Encode(newGuess)
	} else if guessValue > Games[id].secret {
		newGuess.GuessOutcome = "hi"
		if newGuess.GuessCount == 10 {
			Games[id].Outcome = "lose"
		}
		json.NewEncoder(w).Encode(newGuess)
	} else {
		newGuess.GuessOutcome = "lo"
		if newGuess.GuessCount == 10 {
			Games[id].Outcome = "lose"
		}
		json.NewEncoder(w).Encode(newGuess)
	}
	gamesGuesses[id] = append(gamesGuesses[id],newGuess)
}
