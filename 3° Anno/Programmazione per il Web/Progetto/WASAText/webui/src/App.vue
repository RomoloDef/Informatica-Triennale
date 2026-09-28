<script>
export default {
    // Definisco le variabili reattive principali: lista conversazioni, ID utente, stato di caricamento e intervallo di polling
    data() {
        return {
            conversations: [], 
            myUserId: null, 
            loading: false,
            pollingInterval: null
        }
    },
    // Computed property per identificare se siamo nella pagina di login, così da nascondere la sidebar e header
    computed: {
        isLoginPage() { return this.$route.name === 'Login'; }
    },
    // Definisco i metodi principali per gestire le conversazioni, il logout e formattare le informazioni visualizzate
    methods: {
        // Funzione helper per l'URL immagine
        // Se l'URL che arriva dal backend (database) è già completo (http o blob), lo restituisce così com'è, altrimenti lo costruisce con l'host corrente
        getMediaUrl(url) {
            if (!url) return null;
            if (url.startsWith('http') || url.startsWith('blob:')) return url;
            return `http://${window.location.hostname}:3000${url}`;
        },

        async getMyConversations() {
            // La funzione rilegge l'ID direttamente dallo storage che era stato scritto durante il login 
            // tramite localStorage, così da essere sicuri di avere sempre l'ID aggiornato anche se il login è avvenuto in un'altra scheda o finestra del browser.
            const storedId = localStorage.getItem('userId');
            
            // Se non c'è login, resetta tutto e si fermo
            if (!storedId) {
                this.conversations = [];
                this.myUserId = null;
                return;
            }

            // Aggiorna l'ID reattivo
            this.myUserId = parseInt(storedId);

            // Caricamento visibile solo se la lista è vuota (primo avvio)
            if (this.conversations.length === 0) {
                this.loading = true;
            }

            try {
                // Il Polling qui fa due cose:
                // 1. Scarica nuove chat
                // 2. Scarica aggiornamenti nomi/foto (se nel backend le join vanno a buon fine)
                let response = await this.$axios.get('/chats');
                this.conversations = response.data || [];
            } catch (e) {
                if (this.loading) console.error("Errore caricamento chat", e);
            } finally {
                this.loading = false;
            }
        },
        
        logout() {
            // 1. Pulisce lo storage: cancella tutte le chiavi (incluso userId e username) e rimuove l'header di autorizzazione per sicurezza
            localStorage.clear();
            delete this.$axios.defaults.headers.common['Authorization'];
            
            // 2. Resetta lo stato locale IMMEDIATAMENTE affinchè si aggiorni l'interfaccia per sicurezza
            this.conversations = [];
            this.myUserId = null;
            
            // 3. Reindirizza alla pagina di login
            this.$router.push('/login');
        },
        
        getChatName(chat) {
            // Se la chat è di tipo group, mostra il nome e la foto del gruppo
            if (chat.type === 'group') return chat.name || 'Gruppo';
            // Se è una chat 1-1, mostra il nome e la foto dell'altro utente (se presenti)
            if (chat.members && chat.members.length > 0) {
                const other = chat.members.find(u => u.id !== this.myUserId);
                if (other) return other.name;
            }
            return 'Chat';
        },

        getChatPhoto(chat) {
            // Se la chat è di tipo group, mostra il nome e la foto del gruppo
            if (chat.type === 'group') return this.getMediaUrl(chat.photo_url);
            // Se è una chat 1-1, mostra il nome e la foto dell'altro utente (se presenti)
            if (chat.members && chat.members.length > 0) {
                const other = chat.members.find(u => u.id !== this.myUserId);
                if (other) return this.getMediaUrl(other.photo_url);
            }
            return null;
        },
        
        // metodo per formattare la data/ora dei messaggi: se è di oggi mostra solo l'ora, altrimenti mostra la data
        formatTime(isoString) {
            if (!isoString) return '';
            const date = new Date(isoString);
            const now = new Date();
            if (date.toDateString() === now.toDateString()) {
                return date.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
            }
            return date.toLocaleDateString([], { day: '2-digit', month: '2-digit' });
        }
    },
    mounted() {
        // Qui viene avviato il polling globale: controlla aggiornamenti ogni 2 secondi
        this.getMyConversations();
        // Salva l'intervallo in una variabile reattiva così da poterlo pulire quando il componente viene distrutto
        this.pollingInterval = setInterval(() => {
            if (!this.isLoginPage) {
                this.getMyConversations();
            }
        }, 2000); // 2 secondi 
    },
    unmounted() {
        if (this.pollingInterval) clearInterval(this.pollingInterval);
    }
}
</script>

<template>
    <div v-if="!isLoginPage">
        <header class="navbar navbar-dark sticky-top bg-dark flex-md-nowrap p-0 shadow">
            <a class="navbar-brand col-md-3 col-lg-2 me-0 px-3 fs-6" href="#/">WASAText</a>
        </header>

        <div class="container-fluid">
            <div class="row">
                <nav id="sidebarMenu" class="col-md-3 col-lg-2 d-md-block bg-light sidebar collapse p-0">
                    <div class="position-sticky pt-3 sidebar-sticky d-flex flex-column">
                        
                        <ul class="nav flex-column px-2">
                            <li class="nav-item">
                                <RouterLink to="/" class="nav-link rounded" active-class="active-link">
                                    <span class="me-2">🏠</span> Homepage
                                </RouterLink>
                            </li>
                        </ul>

                        <h6 class="sidebar-heading px-3 mt-4 mb-2 text-muted text-uppercase fw-bold small">
                            Conversazioni
                        </h6>
                        
                        <div class="list-group list-group-flush border-bottom scrollarea flex-grow-1">
                            
                            <div v-if="loading && conversations.length === 0" class="text-center p-3 text-muted small">
                                Caricamento...
                            </div>

                            <RouterLink 
                                v-for="chat in conversations" 
                                :key="chat.id" 
                                :to="'/chat/' + chat.id" 
                                class="list-group-item list-group-item-action py-3 lh-tight chat-item"
                                active-class="active-chat"
                            >
                                <div class="d-flex align-items-center w-100">
                                    
                                    <div class="chat-avatar me-3">
                                        <img v-if="getChatPhoto(chat)" :src="getChatPhoto(chat)" class="img-fit">
                                        <div v-else class="avatar-placeholder">
                                            {{ getChatName(chat).charAt(0).toUpperCase() }}
                                        </div>
                                    </div>

                                    <div class="flex-grow-1 min-width-0">
                                        <div class="d-flex justify-content-between align-items-baseline mb-1">
                                            
                                            <strong class="text-truncate d-block text-dark">
                                                {{ getChatName(chat) }}
                                            </strong>
                                            
                                            <small v-if="chat.last_message" class="text-muted ms-2 timestamp">
                                                {{ formatTime(chat.last_message.timestamp) }}
                                            </small>
                                        </div>
                                        
                                        <div class="text-muted small text-truncate snippet">
                                            <span v-if="!chat.last_message" class="fst-italic text-black-50">
                                                Nessun messaggio
                                            </span>
                                            <span v-else-if="chat.last_message.type === 'image'">
                                                📷 <em>Foto</em>
                                            </span>
                                            <span v-else>
                                                {{chat.last_message.content || chat.last_message.text}}
                                            </span>
                                        </div>
                                    </div>
                                </div>
                            </RouterLink>

                            <div v-if="!loading && conversations.length === 0" class="p-4 text-center text-muted small">
                                Nessuna chat attiva.
                            </div>
                        </div>

                        <div class="mt-auto p-3 border-top bg-white">
                            <h6 class="sidebar-heading text-muted text-uppercase small mb-2">Account</h6>
                            <ul class="nav flex-column">
                                <li class="nav-item">
                                    <RouterLink to="/settings" class="nav-link text-dark py-1 px-0">
                                        ⚙️ Impostazioni
                                    </RouterLink>
                                </li>
                                <li class="nav-item">
                                    <a class="nav-link text-danger py-1 px-0" href="#" @click.prevent="logout">
                                        🚪 Esci
                                    </a>
                                </li>
                            </ul>
                        </div>

                    </div>
                </nav>

                <main class="col-md-9 ms-sm-auto col-lg-10 px-0 main-content">
                    <RouterView />
                </main>
            </div>
        </div>
    </div>
    <div v-else class="login-container">
        <RouterView />
    </div>
</template>

<style>
/* CSS Sidebar */
.sidebar { position: fixed; top: 0; bottom: 0; left: 0; z-index: 100; padding: 48px 0 0; box-shadow: inset -1px 0 0 rgba(0, 0, 0, .1); height: 100vh; }
.sidebar-sticky { height: calc(100vh - 48px); overflow-x: hidden; overflow-y: auto; }

/* Avatar Style */
.chat-avatar { width: 48px; height: 48px; min-width: 48px; border-radius: 50%; overflow: hidden; background: #e9ecef; display: flex; align-items: center; justify-content: center; font-weight: bold; color: #6c757d; font-size: 1.2rem; }
.img-fit { width: 100%; height: 100%; object-fit: cover; }

/* Chat Item Style */
.chat-item { border: none; border-bottom: 1px solid #f0f0f0; transition: background 0.2s; }
.chat-item:hover { background-color: #f8f9fa; }
.active-chat { background-color: #e7f1ff !important; border-left: 4px solid #0d6efd; }
.active-link { background-color: #e9ecef; color: #0d6efd; font-weight: 600; }

.min-width-0 { min-width: 0; }
.timestamp { font-size: 0.75rem; }
.snippet { font-size: 0.85rem; }

.login-container { width: 100%; height: 100vh; display: flex; align-items: center; justify-content: center; background-color: #f4f6f8; }
</style>