<script>
import LoadingButton from '../components/LoadingButton.vue';
import LoadingSpinner from '../components/LoadingSpinner.vue';

export default {
    components: { LoadingButton, LoadingSpinner },
    // Definisco le variabili reattive per gestire i dati dell'utente, i nuovi input, gli stati di caricamento e i messaggi di feedback
    data() {
        return {
            user: { id: null, name: '', photoUrl: '' },
            newName: '',
            newPhotoUrl: '',
            loadingData: true,
            loadingName: false,
            loadingPhoto: false,
            loadingDelete: false,
            msg: null 
        }
    },
    methods: {
        // Backend: getMyProfile (GET /users/me)
        async getMyProfile() {
            this.loadingData = true;
            // Invio una richiesta GET al backend per ottenere i dati del profilo dell'utente attualmente loggato.
            try {
                let res = await this.$axios.get('/users/me');
                this.user = res.data;
                this.newName = this.user.name; 
            // Gestione degli errori: se la richiesta fallisce (es. token scaduto), mostro un messaggio
            } catch (e) {
                console.error("Errore profilo", e);
            } finally {
                this.loadingData = false;
            }
        },

        // Backend: setMyUserName (PUT /users/me/name)
        async setMyUserName() {
            // Validazione semplice: il nome deve avere almeno 3 caratteri
            if (this.newName.length < 3) return;
            this.loadingName = true;
            this.msg = null;
            // Invio una richiesta PUT al backend per aggiornare il nome visualizzato dell'utente.
            try {
                let res = await this.$axios.put('/users/me/name', { name: this.newName });
                this.user = res.data;
                // Aggiorno il nome anche nel localStorage e notifico l'app del cambiamento (es. per aggiornare la navbar)
                localStorage.setItem('username', this.user.name);
                window.dispatchEvent(new CustomEvent('user-updated', { detail: { username: this.user.name } }));
                this.showFeedback('success', 'Nome aggiornato con successo!');
            // Gestione degli errori specifici e generici:
            } catch (e) {
                if (e.response && e.response.status === 409) {
                    this.showFeedback('danger', 'Questo nome è già in uso.');
                } else if (e.response && e.response.data && e.response.data.message) {
                    this.showFeedback('danger', 'Errore: ' + e.response.data.message);
                } else {
                    this.showFeedback('danger', 'Errore generico: ' + e.message);
                }
            } finally {
                this.loadingName = false;
            }
        },

        // Backend: setMyPhoto (PUT /users/me/photo)
        async setMyPhoto() {
            // Validazione semplice: controllo che l'input non sia vuoto (ulteriori validazioni potrebbero essere fatte lato backend)
            if (!this.newPhotoUrl) return;
            this.loadingPhoto = true;
            this.msg = null;
            // Invio una richiesta PUT al backend per aggiornare la foto del profilo dell'utente.
            try {
                let res = await this.$axios.put('/users/me/photo', { photo_url: this.newPhotoUrl });
                this.user = res.data;
                this.newPhotoUrl = ''; 
                this.showFeedback('success', 'Foto aggiornata!');
            } catch (e) {
                this.showFeedback('danger', 'URL non valido o errore server.');
            } finally {
                this.loadingPhoto = false;
            }
        },

        // Backend: deleteMyAccount (DELETE /users/me)
        async deleteMyAccount() {
            // Prima di procedere con l'eliminazione, chiedo conferma all'utente perché è un'azione irreversibile
            if (!confirm("Sei sicuro? Questa azione è irreversibile.")) return;
            
            this.loadingDelete = true;
            // Invio una richiesta DELETE al backend per eliminare l'account dell'utente. Se ha chat attive, il backend potrebbe rifiutare la richiesta.
            try {
                await this.$axios.delete('/users/me');
                this.doLogout();
            // Gestione degli errori: se l'eliminazione fallisce (es. chat attive), mostro un messaggio di errore
            } catch (e) {
                this.showFeedback('danger', 'Impossibile eliminare l\'account (forse hai chat attive?)');
                this.loadingDelete = false;
            }
        },

        // Funzione per gestire il logout: pulisce lo storage, rimuove l'header di autenticazione e reindirizza alla pagina di login
        doLogout() {
            localStorage.clear();
            delete this.$axios.defaults.headers.common['Authorization'];
            this.$router.push('/login');
        },

        // Funzione per mostrare messaggi di feedback all'utente (successo o errore) che scompaiono dopo 4 secondi
        showFeedback(type, text) {
            this.msg = { type, text };
            setTimeout(() => this.msg = null, 4000);
        }
    },
    mounted() {
        // Chiamata a funzione per ottenere il profilo utente
        this.getMyProfile();
    }
}
</script>

<template>
    <div class="container py-4">
        <div class="d-flex align-items-center justify-content-between mb-4">
            <div>
                <h2 class="fw-bold mb-0">Il tuo Profilo</h2>
                <p class="text-muted">Gestisci le tue informazioni</p>
            </div>
            <RouterLink to="/" class="btn btn-outline-secondary rounded-pill px-4">
                ← Home
            </RouterLink>
        </div>

        <div v-if="msg" :class="['alert', 'alert-' + msg.type, 'shadow-sm']">
            {{ msg.text }}
        </div>

        <LoadingSpinner :loading="loadingData">
            
            <div class="row g-4">
                <div class="col-md-4">
                    <div class="card border-0 shadow-sm h-100 p-3 text-center profile-card">
                        <div class="card-body">
                            <div class="avatar-wrapper mb-3 mx-auto">
                                <img v-if="user.photoUrl" :src="user.photoUrl" class="avatar-img">
                                <div v-else class="avatar-placeholder">{{ user.name ? user.name.charAt(0).toUpperCase() : '?' }}</div>
                            </div>
                            
                            <h5 class="fw-bold">{{ user.name }}</h5>
                            <p class="text-muted small mb-4">ID: {{ user.id }}</p>
                            
                            <hr class="text-muted opacity-25">

                            <div class="text-start mt-4">
                                <label class="form-label small fw-bold text-muted text-uppercase">Nuova Foto (URL)</label>
                                <input type="text" v-model="newPhotoUrl" class="form-control mb-3" placeholder="https://...">
                                <LoadingButton 
                                    variant="primary" 
                                    class="w-100" 
                                    :loading="loadingPhoto" 
                                    :disabled="!newPhotoUrl"
                                    @click="setMyPhoto"
                                >
                                    Aggiorna Foto
                                </LoadingButton>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="col-md-8">
                    <div class="card border-0 shadow-sm mb-4">
                        <div class="card-body p-4">
                            <h5 class="card-title fw-bold mb-4">Dati Personali</h5>
                            
                            <label class="form-label text-muted">Nome Visualizzato</label>
                            <div class="d-flex gap-2">
                                <input type="text" v-model="newName" class="form-control form-control-lg">
                                <LoadingButton 
                                    variant="success" 
                                    :loading="loadingName" 
                                    :disabled="newName === user.name || newName.length < 3"
                                    @click="setMyUserName"
                                >
                                    Salva
                                </LoadingButton>
                            </div>
                            <div class="form-text mt-2">Il nome deve essere unico.</div>
                        </div>
                    </div>

                    <div class="card border-0 shadow-sm border-start border-danger border-4 bg-white">
                        <div class="card-body p-4">
                            <div class="d-flex justify-content-between align-items-center mb-3">
                                <div>
                                    <h5 class="text-danger fw-bold mb-1">Zona Pericolosa</h5>
                                    <p class="text-muted mb-0 small">Azioni irreversibili per il tuo account.</p>
                                </div>
                            </div>
                            <div class="d-flex gap-3">
                                <button class="btn btn-outline-secondary" @click="doLogout">
                                    Disconnetti (Logout)
                                </button>
                                <LoadingButton 
                                    variant="danger" 
                                    :loading="loadingDelete" 
                                    @click="deleteMyAccount"
                                >
                                    Elimina Account
                                </LoadingButton>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

        </LoadingSpinner>
    </div>
</template>

<style scoped>
.profile-card { border-radius: 16px; background: white; }
.avatar-wrapper { width: 130px; height: 130px; border-radius: 50%; overflow: hidden; border: 4px solid #f8f9fa; box-shadow: 0 4px 15px rgba(0,0,0,0.1); }
.avatar-img { width: 100%; height: 100%; object-fit: cover; }
.avatar-placeholder { width: 100%; height: 100%; background: linear-gradient(135deg, #e9ecef, #dee2e6); display: flex; align-items: center; justify-content: center; font-size: 3rem; font-weight: bold; color: #6c757d; }
</style>