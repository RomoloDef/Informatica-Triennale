<script>
import LoadingButton from '../components/LoadingButton.vue';

export default {
    components: { LoadingButton},
    // Definisco le variabili reattive per gestire lo stato dell'utente, la visualizzazione dei modali, la ricerca degli utenti e la creazione di chat/gruppi
	data() {
		return {
            // Recupero il nome e l'ID dell'utente dallo storage del browser per mostrarli nella dashboard e per usarli nelle chiamate al backend.
			myUsername: localStorage.getItem('username') || 'Utente',
            myUserId: parseInt(localStorage.getItem('userId')),
            
            showChatModal: false,
            showGroupModal: false,

            searchQuery: '',
            searchResults: [],
            loadingSearch: false,
            
            // Variabili Gruppo
            groupName: '',
            groupPhoto: '', 
            selectedUsers: [],
            creating: false,   
            feedback: null 
		}
	},
	methods: {
        handleUserUpdate(event) {
            if (event.detail && event.detail.username) {
                this.myUsername = event.detail.username;
            }
        },

        async searchUsers() {
            // Per ricercare un utente il nome deve avere almeno 2 caratteri per evitare troppe richieste al backend. 
            if (this.searchQuery.length < 2) {
                this.searchResults = [];
                return;
            }
            this.loadingSearch = true;
            // Invia una richiesta GET al backend per cercare utenti che corrispondono alla query di ricerca.
            try {
                let res = await this.$axios.get('/users/search', {
                    params: { username: this.searchQuery }
                });
                // Filtro i risultati per escludere me stesso e gli utenti già selezionati (nel caso di creazione gruppo)
                this.searchResults = res.data.filter(u => 
                    u.id !== this.myUserId && 
                    !this.selectedUsers.find(sel => sel.id === u.id)
                );
            } catch (e) {
                console.error(e);
            } finally {
                this.loadingSearch = false;
            }
        },

        // Backend: createConversation (POST /chats)
        async createConversation(otherUser) {
            this.creating = true;
            // Invia una richiesta POST al backend per creare una nuova chat individuale con l'utente selezionato.
            try {
                let res = await this.$axios.post('/chats', {
                    type: 'individual',
                    participants: [otherUser.id]
                });
                this.closeModals();
                this.$router.push('/chat/' + res.data.id);
                // Il polling di App.vue e ChatView farà il resto
            } catch (e) {
                this.feedback = "Errore creazione chat: " + (e.response?.data?.message || e.message);
            } finally {
                this.creating = false;
            }
        },

        // --- CREAZIONE GRUPPO ---
        async createGroupConversation() {
            // Validazione semplice: il gruppo deve avere un nome e almeno 2 partecipanti (oltre a me) per essere creato.
            if (!this.groupName || this.selectedUsers.length < 2) {
                this.feedback = "Inserisci un nome e seleziona almeno 2 utenti.";
                return;
            }
            this.creating = true;
            try {
                // Preparo l'array degli ID dei partecipanti da inviare al backend. Il backend aggiungerà automaticamente me stesso come partecipante.
                const participantIds = this.selectedUsers.map(u => u.id);
                // Invia una richiesta POST al backend per creare una nuova chat di gruppo con i dati forniti (nome, foto e partecipanti).
                let res = await this.$axios.post('/chats', {
                    type: 'group',
                    group_name: this.groupName,
                    group_icon: this.groupPhoto, 
                    participants: participantIds
                });
                
                this.closeModals();
                this.$router.push('/chat/' + res.data.id);

            } catch (e) {
                this.feedback = "Errore: " + (e.response?.data?.message || e.message);
            } finally {
                this.creating = false;
            }
        },

        // Funzione per aggiungere un utente alla lista dei partecipanti del gruppo durante la creazione, aggiorna anche la UI resettando la ricerca
        addToGroupUI(user) {
            this.selectedUsers.push(user);
            this.searchQuery = ''; 
            this.searchResults = [];
        },
        // Funzione per rimuovere un utente dalla lista dei partecipanti del gruppo durante la creazione, aggiorna anche la UI
        removeUserFromGroupUI(userId) {
            this.selectedUsers = this.selectedUsers.filter(u => u.id !== userId);
        },
        
        // Funzioni per gestire l'apertura e chiusura dei modali di creazione chat/gruppo e per resettare i form quando si aprono
        openChatModal() { this.showChatModal = true; this.resetForm(); },
        openGroupModal() { this.showGroupModal = true; this.resetForm(); },
        closeModals() { this.showChatModal = false; this.showGroupModal = false; },
        resetForm() {
            this.searchQuery = '';
            this.searchResults = [];
            this.groupName = '';
            this.groupPhoto = ''; 
            this.selectedUsers = [];
            this.feedback = null;
        }
	},
	mounted() {
        // Se l'utente cambia nome, viene aggiornato anche qui
		window.addEventListener('user-updated', this.handleUserUpdate);
	},
    unmounted() {
        window.removeEventListener('user-updated', this.handleUserUpdate);
    }
}
</script>

<template>
	<div class="welcome-container">
        <div class="welcome-content text-center fade-in">
            <div class="icon-circle mb-4">
                <svg xmlns="http://www.w3.org/2000/svg" width="64" height="64" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path></svg>
            </div>
            <h1 class="display-5 fw-bold mb-3">Welcome in WasaText</h1>
            <p class="lead text-muted mb-4">Ciao <strong>{{ myUsername }}</strong>, benvenuto nella tua dashboard.</p>
            <p class="text-secondary mb-4">
                👈 Seleziona una chat dalla sidebar o inizia subito da qui:
            </p>
            <div class="d-flex gap-3 justify-content-center">
                <button class="btn btn-primary btn-lg shadow-sm" @click="openChatModal">
                    <span class="me-2">💬</span> Nuova Chat
                </button>
                <button class="btn btn-outline-primary btn-lg shadow-sm" @click="openGroupModal">
                    <span class="me-2">👥</span> Nuovo Gruppo
                </button>
            </div>
        </div>

        <div v-if="showChatModal" class="modal-overlay" @click.self="closeModals">
            <div class="modal-card">
                <div class="d-flex justify-content-between align-items-center mb-3">
                    <h5 class="fw-bold mb-0">Inizia una Conversazione</h5>
                    <button class="btn-close" @click="closeModals"></button>
                </div>
                <input type="text" class="form-control mb-3" placeholder="Cerca utente..." v-model="searchQuery" @input="searchUsers" autofocus>
                <div class="list-group user-list">
                    <div v-if="loadingSearch" class="text-center p-2 text-muted">Cercando...</div>
                    <button v-for="user in searchResults" :key="user.id" class="list-group-item list-group-item-action d-flex align-items-center gap-2" @click="createConversation(user)" :disabled="creating">
                        <div class="avatar-small">{{ user.name.charAt(0).toUpperCase() }}</div>
                        <span>{{ user.name }}</span>
                    </button>
                    <div v-if="!loadingSearch && searchResults.length === 0 && searchQuery.length > 1" class="text-muted text-center p-2">Nessun utente trovato.</div>
                </div>
                <div v-if="feedback" class="alert alert-danger mt-3 py-2 small">{{ feedback }}</div>
            </div>
        </div>

        <div v-if="showGroupModal" class="modal-overlay" @click.self="closeModals">
            <div class="modal-card">
                <div class="d-flex justify-content-between align-items-center mb-3">
                    <h5 class="fw-bold mb-0">Crea un Gruppo</h5>
                    <button class="btn-close" @click="closeModals"></button>
                </div>

                <div class="mb-2">
                    <label class="form-label small text-muted text-uppercase fw-bold mb-1">Nome Gruppo</label>
                    <input type="text" class="form-control" v-model="groupName" placeholder="Es. Calcetto">
                </div>

                <div class="mb-3">
                    <label class="form-label small text-muted text-uppercase fw-bold mb-1">Foto Gruppo (URL)</label>
                    <input type="text" class="form-control" v-model="groupPhoto" placeholder="https://...">
                </div>

                <div class="mb-3">
                    <label class="form-label small text-muted text-uppercase fw-bold mb-1">Partecipanti ({{ selectedUsers.length }})</label>
                    <div class="selected-users-area d-flex gap-2 flex-wrap mb-2">
                        <span v-for="u in selectedUsers" :key="u.id" class="badge bg-primary d-flex align-items-center gap-2 py-2 px-3 rounded-pill">
                            {{ u.name }}
                            <span class="cursor-pointer text-white-50 fw-bold" @click="removeUserFromGroupUI(u.id)">×</span>
                        </span>
                        <span v-if="selectedUsers.length === 0" class="text-muted small fst-italic">Nessuno selezionato</span>
                    </div>

                    <input type="text" class="form-control form-control-sm" placeholder="Cerca e aggiungi..." v-model="searchQuery" @input="searchUsers">
                    
                    <div v-if="searchResults.length > 0" class="list-group mt-1 position-absolute w-100 shadow" style="max-height: 150px; overflow-y: auto; z-index: 10;">
                        <button v-for="user in searchResults" :key="user.id" class="list-group-item list-group-item-action d-flex align-items-center gap-2" @click="addToGroupUI(user)">
                            <div class="avatar-small">{{ user.name.charAt(0).toUpperCase() }}</div>
                            {{ user.name }}
                        </button>
                    </div>
                </div>

                <div v-if="feedback" class="alert alert-danger mt-2 py-2 small">{{ feedback }}</div>

                <LoadingButton variant="success" class="w-100 mt-2" :loading="creating" @click="createGroupConversation" :disabled="!groupName || selectedUsers.length < 2">
                    Crea Gruppo
                </LoadingButton>
            </div>
        </div>

    </div>
</template>

<style scoped>
.welcome-container { height: 100%; display: flex; align-items: center; justify-content: center; padding: 2rem; position: relative; }
.icon-circle { background: linear-gradient(135deg, #0d6efd, #0a58ca); width: 100px; height: 100px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto; box-shadow: 0 10px 20px rgba(13, 110, 253, 0.3); }
.modal-overlay { position: fixed; top: 0; left: 0; right: 0; bottom: 0; background: rgba(0,0,0,0.5); backdrop-filter: blur(2px); display: flex; align-items: center; justify-content: center; z-index: 1050; animation: fadeIn 0.2s; }
.modal-card { background: white; width: 90%; max-width: 400px; padding: 20px; border-radius: 12px; box-shadow: 0 10px 30px rgba(0,0,0,0.2); position: relative; animation: slideUp 0.3s; }
.user-list { max-height: 200px; overflow-y: auto; }
.avatar-small { width: 30px; height: 30px; background: #eee; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: bold; color: #555; font-size: 0.8rem; }
.cursor-pointer { cursor: pointer; }
@keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }
@keyframes slideUp { from { transform: translateY(20px); opacity: 0; } to { transform: translateY(0); opacity: 1; } }
</style>