<script>
import api from '../services/api.js';

export default {
    data() {
        return {
            gameId: null,
            guessInput: "",
            lastResult: null,
            history: [],
            errormsg: null,
            gameOver: false
        }
    },
    methods: {
        async makeGuess() {
            if (!this.guessInput) return;
            this.errormsg = null;

            try {
                // Converto in numero per sicurezza
                let val = parseInt(this.guessInput);
                let response = await api.makeGuess(this.gameId, val);
                
                this.lastResult = response.data;
                this.history.unshift(response.data); // Aggiunge in cima alla lista

                // Controllo vittoria/sconfitta
                if (this.lastResult.GuessOutcome === 'correct') {
                    this.gameOver = true;
                } else if (this.lastResult.GuessCount >= 10) { 
                     this.gameOver = true;
                     this.lastResult.GuessOutcome = "Hai perso (max tentativi)";
                }

                this.guessInput = ""; // Pulisce l'input
            } catch (e) {
                // Se il backend risponde 403 o 404
                this.errormsg = "Errore o Partita finita/inesistente.";
                this.gameOver = true;
            }
        }
    },
    mounted() {
        // Leggo l'ID dall'URL (es: /play/5 -> gameId = 5)
        this.gameId = this.$route.params.id;
    }
}
</script>

<template>
    <div class="container mt-4">
        <h2>Gioca partita #{{ gameId }}</h2>
        
        <RouterLink to="/" class="btn btn-sm btn-secondary mb-3">Indietro</RouterLink>

        <div v-if="!gameOver" class="card p-4">
            <label>Indovina il numero (0-100):</label>
            <div class="d-flex gap-2 mt-2">
                <input type="number" class="form-control" v-model="guessInput" @keyup.enter="makeGuess">
                <button class="btn btn-success" @click="makeGuess">Invia</button>
            </div>
        </div>

        <div v-else class="alert mt-3" :class="lastResult?.GuessOutcome === 'correct' ? 'alert-success' : 'alert-danger'">
            <h4 v-if="lastResult?.GuessOutcome === 'correct'">Vittoria! Hai indovinato!</h4>
            <h4 v-else>Partita Terminata.</h4>
        </div>

        <div v-if="errormsg" class="alert alert-danger mt-3">{{ errormsg }}</div>

        <div v-if="lastResult && !gameOver" class="alert alert-info mt-3">
            Il numero {{ lastResult.GuessValue }} è... 
            <strong>
                {{ lastResult.GuessOutcome === 'hi' ? 'TROPPO ALTO' : '' }}
                {{ lastResult.GuessOutcome === 'lo' ? 'TROPPO BASSO' : '' }}
            </strong>
        </div>

        <ul class="list-group mt-3" v-if="history.length > 0">
            <li class="list-group-item" v-for="(h, index) in history" :key="index">
                Tentativo {{ h.GuessCount }}: <strong>{{ h.GuessValue }}</strong> - {{ h.GuessOutcome }}
            </li>
        </ul>
    </div>
</template>