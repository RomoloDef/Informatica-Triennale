<script>
import LoadingButton from '../components/LoadingButton.vue';

export default {
    components: { LoadingButton },
    // Definisco le variabili reattive per gestire l'input dell'username, lo stato di caricamento e eventuali errori
    data() {
        return {
            username: '',
            loading: false,
            error: null
        }
    },
    methods: {
        // Funzione principale per gestire il login: valida l'input, invia la richiesta al backend e gestisce la risposta
        async doLogin() {
            // Validazione semplice: il nome deve avere almeno 3 caratteri
            if (this.username.length < 3) {
                this.error = "Il nome deve avere almeno 3 caratteri.";
                return;
            }

            this.loading = true;
            this.error = null;
            // Invia una richiesta POST al backend per creare o autenticare l'utente con il nome fornito
            // Tramite il costrutto await, il codice si ferma qui finché non riceve una risposta dal backend.  
            try {
                let response = await this.$axios.post('/users', { name: this.username });
                const user = response.data;
                
                // Salvo l'ID e il nome dell'utente nello storage del browser per poterli usare in altre parti dell'app (es. App.vue) 
                // e per mantenere lo stato di login anche dopo un refresh della pagina
                localStorage.setItem('userId', user.id);
                localStorage.setItem('username', user.name);

                // Configuro Axios per inviare immediatamente questo ID in tutte le chiamate future. 
                // Senza questa riga, la chiamata successiva per scaricare le chat fallirebbe (401 Unauthorized) perché App.vue 
                // legge il localStorage solo al riavvio, non "al volo".
                this.$axios.defaults.headers.common['Authorization'] = 'Bearer ' + user.id;

                // reindirizzo alla pagina principale dell'app dopo il login, dove App.vue caricherà le chat e mostrerà l'interfaccia principale
                this.$router.push('/');
            
            // Gestione degli errori:
            } catch (e) {
                if (e.response && e.response.status === 400) {
                    this.error = "Nome utente non valido.";
                } else {
                    this.error = "Errore di connessione. Riprova.";
                }
            } finally {
                this.loading = false;
            }
        }
    }
}
</script>

<template>
    <div class="login-wrapper">
        <div class="login-card fade-in">
            <div class="icon-circle mb-4">
                <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path></svg>
            </div>
            
            <h2 class="mb-2 fw-bold text-dark">Benvenuto</h2>
            <p class="text-muted mb-4">Entra in WasaText</p>

            <div class="mb-3 text-start">
                <label class="form-label small fw-bold text-uppercase text-muted">Username</label>
                <input 
                    v-model="username" 
                    type="text" 
                    class="form-control form-control-lg" 
                    placeholder="Es. Romolo"
                    @keyup.enter="doLogin"
                >
                <small v-if="error" class="text-danger mt-1 d-block">{{ error }}</small>
            </div>

            <LoadingButton 
                variant="primary" 
                class="w-100 btn-lg" 
                :loading="loading" 
                @click="doLogin"
            >
                Entra
            </LoadingButton>
        </div>
    </div>
</template>

<style scoped>
.login-wrapper { height: 100vh; display: flex; align-items: center; justify-content: center; background-color: #f0f2f5; }
.login-card { background: white; padding: 3rem; border-radius: 16px; box-shadow: 0 10px 40px rgba(0,0,0,0.08); width: 100%; max-width: 420px; text-align: center; }
.icon-circle { background: linear-gradient(135deg, #0d6efd, #0043a8); width: 64px; height: 64px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto; box-shadow: 0 4px 10px rgba(13, 110, 253, 0.3); }
.fade-in { animation: fadeIn 0.5s ease-out; }
@keyframes fadeIn { from { opacity: 0; transform: translateY(20px); } to { opacity: 1; transform: translateY(0); } }
</style>