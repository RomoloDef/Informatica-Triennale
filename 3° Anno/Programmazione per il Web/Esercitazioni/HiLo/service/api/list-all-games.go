package api

import (
	"github.com/julienschmidt/httprouter"
	"net/http"
	"encoding/json"
)

type Game struct {
	Id int
	secret int
	Outcome string
	Guesses int
}

var Games = []Game{
	Game{
		Id: 0,
		secret: 7,
		Outcome: "win",
		Guesses: 5,
	},
}

type Guess struct {
	GuessCount int
	GuessOutcome string
	GuessValue int
}

var gamesGuesses = [][]Guess{
	[]Guess{
		Guess{
			GuessCount: 1,
			GuessOutcome: "hi",
			GuessValue: 50,
		},
		Guess{
			GuessCount: 2,
			GuessOutcome: "hi",
			GuessValue: 25,
		},
		Guess{
			GuessCount: 1,
			GuessOutcome: "hi",
			GuessValue: 12,
		},
		Guess{
			GuessCount: 1,
			GuessOutcome: "lo",
			GuessValue: 6,
		},
		Guess{
			GuessCount: 1,
			GuessOutcome: "correct",
			GuessValue: 7,
		},
	},
}

// Obtain the list of all games, with the final result (win/lose) 
// and the number of guesses
func (rt *_router) listAllGames(w http.ResponseWriter, r *http.Request, ps httprouter.Params) {
	w.Header().Set("content-type", "application/json")
	json.NewEncoder(w).Encode(Games)
}
