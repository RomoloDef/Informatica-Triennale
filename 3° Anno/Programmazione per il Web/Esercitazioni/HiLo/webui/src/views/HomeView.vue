<script>
import api from '../services/api.js'; 

export default {
    data() {
        return {
            games: [],
            loading: false,
            errormsg: null
        }
    },
    methods: {
        async refresh() {
            this.loading = true;
            this.errormsg = null;
            try {
                let response = await api.getAllGames();
                // Assicuriamoci che games sia un array anche se il backend manda null
                this.games = response.data || [];
            } catch (e) {
                this.errormsg = e.toString();
            }
            this.loading = false;
        },
        async startNewGame() {
            try {
                let response = await api.createGame();
                // Il backend restituisce solo l'ID (un numero intero)
                let newGameId = response.data;
                // Andiamo alla pagina di gioco
                this.$router.push({ name: 'play', params: { id: newGameId } });
            } catch (e) {
                this.errormsg = "Errore creazione: " + e.toString();
            }
        }
    },
    mounted() {
        this.refresh();
    }
}
</script>

<template>
    <div class="container mt-4">
        <h1>Partite Hi-Lo</h1>
        
        <button class="btn btn-primary my-3" @click="startNewGame">
            Nuova Partita
        </button>

        <div v-if="errormsg" class="alert alert-danger">{{ errormsg }}</div>

        <table class="table table-bordered table-striped" v-if="games.length > 0">
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Stato</th>
                    <th>Tentativi</th>
                    <th>Azione</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="game in games" :key="game.Id">
                    <td>{{ game.Id }}</td>
                    <td>{{ game.Outcome === '' ? 'In corso' : game.Outcome }}</td>
                    <td>{{ game.Guesses }}</td>
                    <td>
                        <RouterLink 
                            v-if="game.Outcome === ''"
                            :to="{ name: 'play', params: { id: game.Id }}" 
                            class="btn btn-sm btn-outline-success">
                            Gioca
                        </RouterLink>
                        <span v-else class="text-muted">Finita</span>
                    </td>
                </tr>
            </tbody>
        </table>
        
        <div v-else class="text-muted">Nessuna partita trovata.</div>
    </div>
</template>