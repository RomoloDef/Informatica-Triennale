import axios from './axios'; // Importa l'istanza axios già configurata nel tuo progetto

export default {
    // Ottieni la lista di tutte le partite
    getAllGames() {
        return axios.get('/games');
    },

    // Crea una nuova partita
    createGame() {
        return axios.post('/games');
    },

    // Fai un tentativo (Guess)
    // Nota: usiamo params per inviare ?guess=valore come richiesto dal tuo backend Go
    makeGuess(gameId, guessValue) {
        return axios.post(`/games/${gameId}`, null, {
            params: {
                guess: guessValue
            }
        });
    }
}