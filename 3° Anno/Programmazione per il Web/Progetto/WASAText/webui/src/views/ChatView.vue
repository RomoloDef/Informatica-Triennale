<script>
import LoadingButton from '../components/LoadingButton.vue';
import LoadingSpinner from '../components/LoadingSpinner.vue';
import ChatToolbar from '../components/ChatToolbar.vue';
import MessageReactions from '../components/MessageReactions.vue'; 

export default {
    // Importo i componenti necessari: LoadingButton per i pulsanti con stato di caricamento, LoadingSpinner per mostrare un indicatore durante il caricamento dei messaggi, ChatToolbar per le azioni sulla chat (es. modifica nome/foto gruppo) e MessageReactions per gestire le reazioni ai messaggi.
    components: { LoadingButton, LoadingSpinner, ChatToolbar, MessageReactions },
    // Definisco le variabili reattive per gestire lo stato della chat, i messaggi, l'input dell'utente, i file allegati, i modali e gli stati di caricamento.
    data() {
        return {
            chatId: null,
            myUserId: parseInt(localStorage.getItem('userId')),
            
            chatInfo: { name: '', photo_url: null, type: '', description: '', members: [] },
            messages: [],
            myChats: [], 
            
            newMessage: '',
            replyingTo: null, 
            
            selectedFile: null,
            previewUrl: null,

            loading: true,
            sending: false,
            loadingAction: false,
            pollingInterval: null,
            
            showForwardModal: false,
            msgIdToForward: null,
            selectedForwardChatIds: [],
            forwarding: false,

            showAddMemberModal: false,
            searchQuery: '',
            searchResults: [],
            selectedUsersToAdd: [],
            addingMember: false
        }
    },
    watch: {
        '$route.params.id': {
            immediate: true,
            handler(newId) {
                if (newId) {
                    this.chatId = newId;
                    this.initChat();
                }
            }
        }
    },
    methods: {
        // Stesso metodo di LoginView per costruire l'URL completo per le risorse media (foto profilo, immagini nei messaggi) gestendo sia URL assoluti che relativi forniti dal backend.
        getMediaUrl(url) {
            if (!url) return '';
            if (url.startsWith('http') || url.startsWith('blob:')) return url;
            return `http://${window.location.hostname}:3000${url}`;
        },

        // Funzione principale per inizializzare la chat: carica le informazioni della chat e i messaggi,
        // imposta un intervallo di polling per aggiornare periodicamente i dati e gestisce lo stato di caricamento.
        async initChat() {
            this.loading = true;
            this.messages = [];
            if (this.pollingInterval) clearInterval(this.pollingInterval);

            // Caricamento iniziale
            await this.getConversation();
            await this.getMessages();
            
            this.loading = false;
            this.scrollToBottom();

            // --- POLLING ---
            // Aggiorna sia i messaggi (per leggere e segnare come letto)
            // SIA le info chat (per vedere se cambia nome/foto gruppo)
            this.pollingInterval = setInterval(async () => {
                await this.getMessages();
                await this.getConversation(); 
            }, 2500);
        },

        // Funzione per caricare le informazioni della chat dal backend, come nome, foto, tipo, descrizione e membri.
        async getConversation() {
            try {
                // Invia una richiesta GET al backend per ottenere le informazioni della chat corrente usando l'ID della chat (this.chatId) ottenuto dai parametri della route.
                let res = await this.$axios.get(`/chats/${this.chatId}`);
                this.chatInfo = res.data;
            } catch (e) {
                // Gestione 404 se vengo rimosso dalla chat
                if (e.response && e.response.status === 404) this.$router.push('/');
            }
        },

        // Funzione per caricare i messaggi della chat dal backend, ordina i messaggi dal più vecchio al più recente e li memorizza nella variabile reattiva "messages" per essere visualizzati nell'interfaccia.
        async getMessages() {
            try {
                // Invia una richiesta GET al backend per ottenere i messaggi della chat corrente usando l'ID della chat (this.chatId). 
                // La risposta è un array di messaggi che viene memorizzato nella variabile reattiva "messages" dopo essere stato invertito per mostrare i messaggi dal più vecchio al più recente.
                let res = await this.$axios.get(`/chats/${this.chatId}/messages`);
                // L'ordine è dal basso verso l'alto
                this.messages = res.data.reverse();
            } catch (e) {
                console.error("Errore messaggi:", e);
            }
        },

        // Funzione per ottenere il nome del mittente di un messaggio, utilizzata principalmente nelle chat di gruppo per mostrare chi ha inviato ogni messaggio.
        getSenderName(senderId) {
            if (senderId === this.myUserId) return "Tu";
            if (this.chatInfo.members) {
                const member = this.chatInfo.members.find(u => u.id === senderId);
                if (member) return member.name;
            }
            return "User " + senderId; 
        },

        // Funzione per ottenere il nome di una chat, utilizzata principalmente nella modale di inoltro 
        // per mostrare il nome della chat a cui si sta inoltrando un messaggio. 
        // Gestisce sia chat di gruppo che chat 1-1.
        getChatName(chat) {
            if (chat.type === 'group') return chat.name || 'Gruppo';
            if (chat.members && chat.members.length > 0) {
                const other = chat.members.find(u => u.id !== this.myUserId);
                if (other) return other.name;
            }
            return chat.name || 'Chat';
        },

        // --- GESTIONE FILE UPLOAD ---
        triggerFileUpload() {
            this.$refs.fileInput.click();
        },
        handleFileSelect(event) {
            const file = event.target.files[0];
            if (!file) return;
            if (!file.type.startsWith('image/')) {
                alert("Puoi inviare solo immagini.");
                return;
            }
            this.selectedFile = file;
            this.previewUrl = URL.createObjectURL(file);
        },
        clearFile() {
            this.selectedFile = null;
            if (this.previewUrl) URL.revokeObjectURL(this.previewUrl);
            this.previewUrl = null;
            if (this.$refs.fileInput) this.$refs.fileInput.value = '';
        },

        // Funzione per inviare un nuovo messaggio: gestisce sia messaggi di testo che messaggi con allegati (immagini), 
        // supporta la funzionalità di risposta a un messaggio specifico e 
        // aggiorna la lista dei messaggi dopo l'invio.
        async sendMessage() {
            if (!this.newMessage.trim() && !this.selectedFile) return;
            
            this.sending = true;
            try {
                let payload;
                // Se è stato selezionato un file, creo un oggetto FormData per inviare sia il testo che il file al backend.
                if (this.selectedFile) {
                    payload = new FormData();
                    payload.append('content', this.newMessage);
                    payload.append('file', this.selectedFile);
                    payload.append('type', 'image');
                } else {
                    payload = { type: 'text', content: this.newMessage };
                }
                // Se sto rispondendo a un messaggio specifico, invio la richiesta al backend usando l'endpoint di risposta (POST /chats/:chatId/messages/:messageId/reply), 
                // altrimenti uso l'endpoint standard per inviare un nuovo messaggio (POST /chats/:chatId/messages).
                if (this.replyingTo) {
                    await this.$axios.post(`/chats/${this.chatId}/messages/${this.replyingTo.id}/reply`, payload);
                } else {
                    await this.$axios.post(`/chats/${this.chatId}/messages`, payload);
                }

                this.newMessage = '';
                this.replyingTo = null;
                this.clearFile(); 

                // Dopo aver inviato il messaggio, ricarico la lista dei messaggi per mostrare il nuovo messaggio inviato 
                await this.getMessages();
                this.scrollToBottom();
            } catch (e) {
                alert("Errore invio: " + (e.response?.data?.message || e.message));
            } finally {
                this.sending = false;
            }
        },

        // Funzione per eliminare un messaggio inviato da me
        async deleteMessage(messageId) {
            if (!confirm("Eliminare questo messaggio?")) return;
            // Invia una richiesta DELETE al backend per eliminare un messaggio specifico usando l'ID del messaggio e l'ID della chat.
            try {
                await this.$axios.delete(`/chats/${this.chatId}/messages/${messageId}`);
                await this.getMessages(); 
            } catch (e) { alert("Errore eliminazione: " + e.message); }
        },

        // Funzione per preparare la risposta a un messaggio specifico: 
        // memorizza il messaggio a cui si sta rispondendo nella variabile reattiva "replyingTo" e 
        // mette a fuoco l'input del messaggio per iniziare a scrivere la risposta.
        prepareReply(msg) {
            this.replyingTo = msg;
            this.$nextTick(() => document.getElementById('chatInput').focus());
        },
        cancelReply() { this.replyingTo = null; },

        async openForwardModal(messageId) {
            this.msgIdToForward = messageId;
            this.selectedForwardChatIds = [];
            this.showForwardModal = true;
            try {
                let res = await this.$axios.get('/chats'); 
                this.myChats = res.data.filter(c => c.id != this.chatId) || [];
            } catch (e) { console.error(e); }
        },

        // Funzione per la gestione dell'inoltro di un messaggio a una o più chat selezionate
        async forwardMessage() {
            if (this.selectedForwardChatIds.length === 0) return;
            this.forwarding = true;
            try {
                // Invia una richiesta POST al backend per inoltrare un messaggio specifico (this.msgIdToForward) 
                // a una o più chat selezionate (this.selectedForwardChatIds)
                // usando l'endpoint di inoltro (POST /chats/:chatId/messages/:messageId/forward).
                await this.$axios.post(`/chats/${this.chatId}/messages/${this.msgIdToForward}/forward`, {
                    target_chat_ids: this.selectedForwardChatIds
                });
                alert("Messaggio inoltrato!");
                this.showForwardModal = false;
                this.msgIdToForward = null;
                this.selectedForwardChatIds = [];
            } catch (e) { alert("Errore inoltro: " + e.message); } finally { this.forwarding = false; }
        },

        openAddMemberModal() {
            this.showAddMemberModal = true;
            this.searchQuery = '';
            this.searchResults = [];
            this.selectedUsersToAdd = [];
        },

        // Funzione per la gestione della ricerca degli utenti da aggiungere a un gruppo
        async searchUsersToAdd() {
            // Controllo sulla ricerca come fatto in HomeView per evitare chiamate al backend con query troppo corte.
            if (this.searchQuery.length < 2) {
                this.searchResults = [];
                return;
            }
            try {
                // Invia una richiesta GET al backend per cercare utenti in base alla query di ricerca (this.searchQuery) usando l'endpoint di ricerca utenti (GET /users/search).
                let res = await this.$axios.get('/users/search', {
                    params: { username: this.searchQuery }
                });
                // Filtro i risultati per escludere gli utenti che sono già membri del gruppo (this.chatInfo.members) e quelli già selezionati per l'aggiunta (this.selectedUsersToAdd) per evitare di mostrare utenti non validi nella lista dei risultati della ricerca.
                const currentMemberIds = this.chatInfo.members.map(m => m.id);
                
                this.searchResults = res.data.filter(u => 
                    !currentMemberIds.includes(u.id) && 
                    !this.selectedUsersToAdd.includes(u.id)
                );
            } catch (e) {
                console.error(e);
            }
        },

        // Funzione per aggiungere i membri selezionati a un gruppo: invia una richiesta al backend con gli ID degli utenti da aggiungere e aggiorna la chat dopo l'aggiunta.
        async addMembersToGroup() {
            if (this.selectedUsersToAdd.length === 0) return;
            this.addingMember = true;
            try {
                // Chiamata all'API (POST /chats/:id/participants)
                await this.$axios.post(`/chats/${this.chatId}/participants`, {
                    user_ids: this.selectedUsersToAdd
                });
                
                alert("Membri aggiunti con successo!");
                this.showAddMemberModal = false;
                
                // Ricarica la chat per vedere i nuovi membri
                await this.getConversation(); 
                
            } catch (e) {
                // Messaggio di errore generico sui permessi
                if (e.response && e.response.status === 403) {
                    alert("Non hai i permessi per aggiungere membri (devi essere parte del gruppo).");
                } else {
                    alert("Errore: " + (e.response?.data?.message || e.message));
                }
            } finally {
                this.addingMember = false;
            }
        },

        // Funzione per impostare il nuovo nome del gruppo: Viene mostrato un prompt per inserire il nuovo nome
        async setGroupName() {
            let newName = prompt("Nuovo nome del gruppo:", this.chatInfo.name);
            if (!newName) return;
            
            this.loadingAction = true;
            try {
                // Invia una richiesta PUT al backend per aggiornare il nome del gruppo usando l'endpoint di modifica chat (PUT /chats/:id) con il nuovo nome.
                let res = await this.$axios.put(`/chats/${this.chatId}`, { group_name: newName });
                this.chatInfo = res.data; 
            } catch (e) { 
                alert(e.message); 
            } finally { 
                this.loadingAction = false; 
            }
        },
        async setGroupPhoto() {
            // Usa input file nascosto se presente nel template padre.
            this.$refs.groupPhotoInput.click();
        },
        
        async uploadGroupPhoto(event) {
            const file = event.target.files[0];
            if (!file) return;
            this.loadingAction = true;
            try {
                const formData = new FormData();
                formData.append('file', file);
                let res = await this.$axios.put(`/chats/${this.chatId}/photo`, formData);
                this.chatInfo = res.data; 
                this.$refs.groupPhotoInput.value = '';
            } catch (e) {
                alert("Errore upload: " + (e.response?.data?.message || e.message));
            } finally {
                this.loadingAction = false;
            }
        },

        // Funzione con stessa logica di setGroupName per modificare la descrizione del gruppo
        async setGroupDescription() {
            let newDesc = prompt("Nuova descrizione:", this.chatInfo.description || "");
            if (newDesc === null) return; 
            
            this.loadingAction = true;
            try {
                let res = await this.$axios.put(`/chats/${this.chatId}/description`, { description: newDesc });
                this.chatInfo = res.data; 
            } catch (e) { 
                alert(e.message); 
            } finally { 
                this.loadingAction = false; 
            }
        },

        // Funzione per lasciare un gruppo. Per fare ciò viene chiesta una conferma all'utente
        async leaveGroup() {
            if (!confirm("Lasciare il gruppo?")) return;
            this.loadingAction = true;
            // A seguito viene inviata una richesta DELETE al backend per rimuovere me stesso dai partecipanti della chat usando l'endpoint di rimozione partecipante (DELETE /chats/:id/participants/me).
            try { await this.$axios.delete(`/chats/${this.chatId}/participants/me`); this.$router.push('/'); } 
            catch (e) { alert("Errore"); } finally { this.loadingAction = false; }
        },

        // Funzione per cancellare una conversazione. Ha la stessa logica di leaveGroup ma invia una richiesta DELETE all'endpoint di eliminazione chat (DELETE /chats/:id) per eliminare completamente la chat. 
        async deleteConversation() {
            if (!confirm("Eliminare la chat?")) return;
            this.loadingAction = true;
            try { await this.$axios.delete(`/chats/${this.chatId}`); this.$router.push('/'); } 
            catch (e) { alert("Errore"); } finally { this.loadingAction = false; }
        },

        // Funzione per scrollare automaticamente la vista dei messaggi verso il basso ogni volta che i messaggi vengono aggiornati o viene inviato un nuovo messaggio, in modo da mostrare sempre l'ultimo messaggio.
        scrollToBottom() {
            this.$nextTick(() => {
                const container = this.$refs.msgContainer;
                if (container) container.scrollTop = container.scrollHeight;
            });
        },

        // Funzione per formattare la data/ora di un messaggio in un formato leggibile (es. "14:35") da mostrare nell'interfaccia accanto a ogni messaggio.
        formatTime(timestamp) {
            if (!timestamp) return '';
            return new Date(timestamp).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
        }
    },
    
    // Quando il componente viene distrutto (es. quando si chiude la chat), è importante pulire l'intervallo di polling per evitare chiamate al backend non necessarie e potenziali memory leak.
    unmounted() {
        if (this.pollingInterval) clearInterval(this.pollingInterval);
    }
}
</script>

<template>
    <div class="chat-layout">
        <input type="file" ref="groupPhotoInput" accept="image/*" style="display: none" @change="uploadGroupPhoto">

        <div class="chat-header px-4 py-2 border-bottom d-flex align-items-center justify-content-between">
            <div class="d-flex align-items-center gap-3 overflow-hidden">
                <div class="chat-avatar flex-shrink-0">
                    <img v-if="chatInfo.photo_url" :src="getMediaUrl(chatInfo.photo_url)" class="img-fit">
                    <div v-else class="avatar-placeholder">
                        {{ chatInfo.name ? chatInfo.name.charAt(0).toUpperCase() : '?' }}
                    </div>
                </div>
                <div class="min-width-0">
                    <h5 class="mb-0 fw-bold text-truncate">{{ chatInfo.name }}</h5>
                    <div class="d-flex flex-column">
                        <small class="text-muted" v-if="chatInfo.type === 'group'">Gruppo</small>
                        <small v-if="chatInfo.description" class="text-secondary text-truncate fst-italic" :title="chatInfo.description">
                            {{ chatInfo.description }}
                        </small>
                    </div>
                </div>
            </div>

            <div class="d-flex align-items-center gap-2">
                <button 
                    v-if="chatInfo.type === 'group'" 
                    class="btn btn-outline-primary btn-sm me-2" 
                    @click="openAddMemberModal"
                    title="Aggiungi partecipanti"
                >
                    ➕ Aggiungi
                </button>

                <ChatToolbar 
                    :is-group="chatInfo.type === 'group'"
                    :loading="loadingAction"
                    @set-group-name="setGroupName"
                    @set-group-photo="setGroupPhoto"
                    @set-group-desc="setGroupDescription"
                    @leave="leaveGroup"
                    @delete="deleteConversation"
                />
                <div class="vr mx-1"></div>
                <RouterLink to="/" class="btn btn-sm btn-secondary">Chiudi</RouterLink>
            </div>
        </div>

        <div class="chat-messages p-4" ref="msgContainer">
            <LoadingSpinner :loading="loading">
                <div v-if="messages.length === 0" class="text-center mt-5 text-muted">
                    <div class="mb-2">👋</div>
                    <p>Nessun messaggio.</p>
                </div>

                <div 
                    v-for="msg in messages" 
                    :key="msg.id" 
                    class="d-flex mb-3"
                    :class="msg.sender_id === myUserId ? 'justify-content-end' : 'justify-content-start'"
                >
                    <div 
                        class="message-bubble shadow-sm"
                        :class="msg.sender_id === myUserId ? 'bg-primary text-white my-msg' : 'bg-white text-dark other-msg'"
                    >
                        <div class="d-flex justify-content-between align-items-center mb-1 gap-2">
                            <div v-if="chatInfo.type === 'group' && msg.sender_id !== myUserId" class="sender-name">
                                {{ getSenderName(msg.sender_id) }}
                            </div>
                            <div v-else></div>

                            <div class="msg-actions">
                                <button class="btn btn-link btn-sm p-0 text-decoration-none text-white-50" @click="prepareReply(msg)">↩️</button>
                                <button class="btn btn-link btn-sm p-0 text-decoration-none text-white-50" @click="openForwardModal(msg.id)">↪️</button>
                                <button v-if="msg.sender_id === myUserId" class="btn btn-link btn-sm p-0 text-decoration-none text-danger" @click="deleteMessage(msg.id)">🗑️</button>
                            </div>
                        </div>

                        <div v-if="msg.is_forwarded" class="forwarded-label mb-1">
                            <small class="fst-italic text-white-50" v-if="msg.sender_id === myUserId">↪ Inoltrato</small>
                            <small class="fst-italic text-secondary" v-else>↪ Inoltrato</small>
                        </div>

                        <div v-if="msg.reply_to" class="reply-preview mb-2">
                            <small class="d-block fw-bold">In risposta a:</small>
                            <div class="d-flex align-items-center gap-1">
                                <span v-if="msg.reply_to.type === 'image'">📷</span>
                                <span class="text-truncate d-block fst-italic">
                                    {{ msg.reply_to.content || (msg.reply_to.type === 'image' ? 'Foto' : 'Messaggio') }}
                                </span>
                            </div>
                        </div>
                        
                        <div v-if="msg.type === 'image'" class="mb-1">
                            <img :src="getMediaUrl(msg.media_url)" class="img-fluid rounded" style="max-height: 300px;" alt="Immagine caricata">
                        </div>

                        <div v-if="msg.content" class="message-text">{{ msg.content }}</div>
                        
                        <MessageReactions 
                            :message-id="parseInt(msg.id)"
                            :chat-id="parseInt(chatId)"
                            :my-user-id="myUserId"
                            :reactions="msg.reactions || []" 
                            @reaction-changed="getMessages"
                        />

                        <div class="message-time" :class="msg.sender_id === myUserId ? 'text-white-50' : 'text-muted'">
                            {{ formatTime(msg.timestamp) }}
                            <span v-if="msg.sender_id === myUserId" class="ms-1 fw-bold" style="font-size: 0.8rem;">
                                <span v-if="msg.status === 'read'" class="text-info">✓✓</span> 
                                <span v-else-if="msg.status === 'delivered'">✓✓</span>      
                                <span v-else>✓</span>                                      
                            </span>
                        </div>

                    </div>
                </div>
            </LoadingSpinner>
        </div>

        <div class="chat-input px-4 py-3 border-top bg-light">
            
            <input type="file" ref="fileInput" accept="image/*" style="display: none" @change="handleFileSelect">

            <div v-if="replyingTo || selectedFile" class="reply-banner alert alert-secondary d-flex justify-content-between align-items-center py-2 px-3 mb-2">
                <div class="d-flex align-items-center gap-3 overflow-hidden">
                    
                    <div v-if="replyingTo" class="text-truncate">
                        <small class="fw-bold d-block">Rispondendo a:</small> 
                        <span v-if="replyingTo.type === 'image'">📷 Foto</span>
                        <span>{{ replyingTo.content }}</span>
                    </div>

                    <div v-if="selectedFile" class="d-flex align-items-center bg-white p-1 rounded border">
                        <img :src="previewUrl" height="40" width="40" class="rounded object-fit-cover me-2">
                        <small class="text-truncate" style="max-width: 150px;">{{ selectedFile.name }}</small>
                    </div>
                </div>

                <button type="button" class="btn-close small" @click="() => { cancelReply(); clearFile(); }"></button>
            </div>

            <div class="input-group gap-2">
                <button class="btn btn-light border rounded-circle" type="button" @click="triggerFileUpload" :disabled="loading || sending" title="Allega foto">
                    📷
                </button>

                <input id="chatInput" type="text" class="form-control form-control-lg border-0 shadow-sm rounded-pill" placeholder="Scrivi..." v-model="newMessage" @keyup.enter="sendMessage" :disabled="loading">
                
                <LoadingButton variant="primary" :loading="sending" @click="sendMessage" :disabled="(!newMessage.trim() && !selectedFile)" class="rounded-pill px-4">
                    Invia ➤
                </LoadingButton>
            </div>
        </div>

        <div v-if="showForwardModal" class="modal-overlay" @click.self="showForwardModal = false">
            <div class="modal-card">
                <h5 class="mb-3">Inoltra a...</h5>
                <div class="list-group mb-3" style="max-height: 300px; overflow-y: auto;">
                    <label v-for="chat in myChats" :key="chat.id" class="list-group-item d-flex gap-2 align-items-center pointer">
                        <input class="form-check-input flex-shrink-0" type="checkbox" :value="chat.id" v-model="selectedForwardChatIds">
                        <span>{{ getChatName(chat) }}</span>
                    </label>
                    <div v-if="myChats.length === 0" class="text-muted small">Nessuna altra chat disponibile.</div>
                </div>
                <div class="d-flex justify-content-end gap-2">
                    <button class="btn btn-secondary" @click="showForwardModal = false">Annulla</button>
                    <LoadingButton :loading="forwarding" @click="forwardMessage" :disabled="selectedForwardChatIds.length === 0">Inoltra</LoadingButton>
                </div>
            </div>
        </div>

        <div v-if="showAddMemberModal" class="modal-overlay" @click.self="showAddMemberModal = false">
            <div class="modal-card">
                <div class="d-flex justify-content-between align-items-center mb-3">
                    <h5 class="fw-bold mb-0">Aggiungi al Gruppo</h5>
                    <button class="btn-close" @click="showAddMemberModal = false"></button>
                </div>

                <input 
                    type="text" 
                    class="form-control mb-3" 
                    placeholder="Cerca username..." 
                    v-model="searchQuery" 
                    @input="searchUsersToAdd" 
                    autofocus
                >

                <div class="list-group mb-3" style="max-height: 200px; overflow-y: auto;">
                    <button 
                        v-for="user in searchResults" 
                        :key="user.id" 
                        class="list-group-item list-group-item-action d-flex align-items-center justify-content-between" 
                        @click="selectedUsersToAdd.push(user.id); searchQuery = ''; searchResults = []"
                    >
                        <span>{{ user.name }}</span>
                        <span class="badge bg-secondary">+</span>
                    </button>
                    <div v-if="searchResults.length === 0 && searchQuery.length > 1" class="text-muted small text-center p-2">
                        Nessun utente trovato (o già presente).
                    </div>
                </div>

                <div v-if="selectedUsersToAdd.length > 0" class="mb-3">
                    <small class="fw-bold text-muted">Da aggiungere:</small>
                    <div class="d-flex flex-wrap gap-1 mt-1">
                        <span v-for="uid in selectedUsersToAdd" :key="uid" class="badge bg-primary">
                            ID: {{ uid }} 
                            <span class="ms-1 cursor-pointer" style="cursor:pointer" @click="selectedUsersToAdd = selectedUsersToAdd.filter(id => id !== uid)">×</span>
                        </span>
                    </div>
                </div>

                <div class="d-flex justify-content-end gap-2">
                    <button class="btn btn-secondary" @click="showAddMemberModal = false">Annulla</button>
                    <LoadingButton 
                        variant="success" 
                        :loading="addingMember" 
                        @click="addMembersToGroup" 
                        :disabled="selectedUsersToAdd.length === 0"
                    >
                        Conferma Aggiunta
                    </LoadingButton>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
.chat-layout { display: flex; flex-direction: column; height: 100vh; background-color: #f0f2f5; }
.chat-header { background: white; height: auto; min-height: 70px; flex-shrink: 0; }
.chat-avatar { width: 45px; height: 45px; border-radius: 50%; overflow: hidden; background: #ddd; display: flex; align-items: center; justify-content: center; font-weight: bold; color: #555; }
.img-fit { width: 100%; height: 100%; object-fit: cover; }
.chat-messages { flex-grow: 1; overflow-y: auto; background-image: url('https://user-images.githubusercontent.com/15075759/28719144-86dc0f70-73b1-11e7-911d-60d70fcded21.png'); background-blend-mode: soft-light; }
.message-bubble { max-width: 65%; padding: 8px 12px; border-radius: 12px; position: relative; font-size: 0.95rem; }
.my-msg { border-top-right-radius: 0; }
.other-msg { border-top-left-radius: 0; }
.sender-name { font-size: 0.75rem; font-weight: bold; color: #d63384; margin-bottom: 2px; }
.message-time { font-size: 0.7rem; text-align: right; margin-top: 4px; display: flex; align-items: center; justify-content: flex-end; gap: 4px; }
.msg-actions { opacity: 0.6; transition: opacity 0.2s; display: flex; gap: 8px; font-size: 1.2rem; }
.message-bubble:hover .msg-actions { opacity: 1; }
.reply-preview { border-left: 4px solid rgba(0,0,0,0.2); padding-left: 8px; background: rgba(0,0,0,0.05); border-radius: 4px; padding: 4px; font-size: 0.85rem; }
.reply-banner { border-left: 4px solid #0d6efd; }
.modal-overlay { position: fixed; top: 0; left: 0; right: 0; bottom: 0; background: rgba(0,0,0,0.5); z-index: 1050; display: flex; align-items: center; justify-content: center; }
.modal-card { background: white; padding: 20px; border-radius: 8px; width: 90%; max-width: 400px; box-shadow: 0 4px 15px rgba(0,0,0,0.2); }
.pointer { cursor: pointer; }
.min-width-0 { min-width: 0; }
</style>