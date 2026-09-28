<script>
export default {
    // Questi sono i dati in ingresso e vengono passati dal componente genitore (ChatView.vue) quando viene usato il componente <MessageReactions>.
    props: {
        messageId: { type: Number, required: true },
        chatId: { type: Number, required: true },
        reactions: { type: Array, default: () => [] }, 
        myUserId: { type: Number, required: true }
    },
    // Questo componente emette un evento "reaction-changed" al genitore ogni volta che l'utente aggiunge o rimuove una reazione, 
    // in modo che il genitore possa aggiornare la lista delle reazioni (es. facendo una nuova richiesta al backend).
    emits: ['reaction-changed'],
    // Defunuisco le variabili reattive per gestire la visibilità del picker di emoji e la lista delle emoji disponibili da mostrare nel picker.
    data() {
        return {
            showPicker: false,
            availableEmojis: ['👍', '❤️', '😂', '😮', '😢', '😡']
        }
    },
    computed: {
        // Questa computed property raggruppa le reazioni per emoji, contando quante volte ogni emoji è stata usata e se l'utente attuale ha reagito con quell'emoji.
        groupedReactions() {
            const groups = {};
            this.reactions.forEach(r => {
                // Se non esiste ancora un gruppo per questa emoji, lo creo con le proprietà iniziali (emoji, count, me, names)
                if (!groups[r.emoji_code]) {
                    // Si aumenta il contatore di quella emoji e si aggiunge il nome dell'utente che ha reagito
                    groups[r.emoji_code] = { 
                        emoji: r.emoji_code, 
                        count: 0, 
                        me: false,
                        names: [] 
                    };
                }
                
                groups[r.emoji_code].count++;
                
                // Qui avviene la gestione dei nomi degli utenti che hanno reagito: se è presente il nome, viene aggiunto alla lista dei nomi per quella emoji.
                if (r.user_name) {
                    // Se l'utente è quello personale viene scritto "Tu" invece del nome utente
                    if (r.user_id === this.myUserId) {
                        groups[r.emoji_code].names.push("Tu");
                    } else {
                        groups[r.emoji_code].names.push(r.user_name);
                    }
                }

                if (r.user_id === this.myUserId) {
                    groups[r.emoji_code].me = true;
                }
            });
            return Object.values(groups);
        }
    },
    methods: {
        // Questa funzione viene chiamata quando l'utente clicca su una reazione: se ha già reagito con quell'emoji, viene rimossa la reazione, altrimenti viene aggiunta.
        async toggleReaction(emoji, hasReacted) {
            if (hasReacted) {
                await this.uncommentMessage(emoji);
            } else {
                await this.commentMessage(emoji);
            }
        },

        // Funzione per aggiungere una reazione a un messaggio. 
        async commentMessage(emoji) {
            this.showPicker = false;
            try {
                // Viene inviata una richiesta POST al backend all'endpoint di aggiunta reazione (POST /chats/:chatId/messages/:messageId/reaction) con il codice dell'emoji selezionata.
                await this.$axios.post(`/chats/${this.chatId}/messages/${this.messageId}/reaction`, {
                    emoji_code: emoji
                });
                this.$emit('reaction-changed');
            } catch (e) {
                console.error("Errore aggiunta reazione", e);
            }
        },

        // Funzione per rimuovere una reazione da un messaggio.
        async uncommentMessage(emoji) {
            try {
                // Viene inviata una richiesta DELETE al backend all'endpoint di rimozione reazione (DELETE /chats/:chatId/messages/:messageId/reaction) per rimuovere la reazione dell'utente attuale a quel messaggio.
                await this.$axios.delete(`/chats/${this.chatId}/messages/${this.messageId}/reaction`);
                this.$emit('reaction-changed');
            } catch (e) {
                console.error("Errore rimozione reazione", e);
            }
        }
    }
}
</script>

<template>
    <div class="reactions-wrapper">
        <div class="chips-container">
            <button 
                v-for="group in groupedReactions" 
                :key="group.emoji"
                class="reaction-chip"
                :class="{ 'active': group.me }"
                @click.stop="toggleReaction(group.emoji, group.me)"
            >
                <span class="emoji">{{ group.emoji }}</span>
                <span class="count ms-1">{{ group.count }}</span>
                
                <span class="authors-text" v-if="group.names.length > 0">
                    {{ group.names.join(', ') }}
                </span>
            </button>

            <div class="add-reaction-container">
                <button class="add-btn" @click.stop="showPicker = !showPicker">
                    ☺<span class="plus">+</span>
                </button>

                <div v-if="showPicker" class="emoji-picker shadow-sm">
                    <span 
                        v-for="emoji in availableEmojis" 
                        :key="emoji" 
                        class="emoji-option"
                        @click.stop="commentMessage(emoji)"
                    >
                        {{ emoji }}
                    </span>
                </div>
            </div>
        </div>
        <div v-if="showPicker" class="picker-overlay" @click="showPicker = false"></div>
    </div>
</template>

<style scoped>
.reactions-wrapper { margin-top: 4px; display: flex; flex-wrap: wrap; gap: 4px; position: relative; }
.chips-container { display: flex; flex-wrap: wrap; gap: 6px; align-items: center; }

.reaction-chip {
    background-color: rgba(0, 0, 0, 0.05);
    border: 1px solid transparent;
    border-radius: 12px;
    padding: 2px 8px; 
    font-size: 0.75rem;
    cursor: pointer;
    display: flex;
    align-items: center;
    transition: all 0.2s;
    color: #555;
    max-width: 100%; 
}

.reaction-chip:hover { background-color: rgba(0, 0, 0, 0.1); }
.reaction-chip.active { background-color: #e7f1ff; border-color: #0d6efd; color: #0d6efd; }

.emoji { font-size: 0.9rem; }
.count { font-weight: bold; font-size: 0.75rem; }

.authors-text {
    margin-left: 6px;
    font-size: 0.7rem;
    color: inherit;    
    opacity: 0.8;
    font-weight: normal;
    
    max-width: 120px;   
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    display: inline-block;
    vertical-align: middle;
}

.add-btn { background: transparent; border: none; color: #aaa; cursor: pointer; font-size: 1rem; padding: 0 4px; line-height: 1; display: flex; opacity: 0.6; transition: opacity 0.2s; }
.add-btn:hover { opacity: 1; color: #555; }
.plus { font-size: 0.7rem; vertical-align: top; }
.add-reaction-container { position: relative; }
.emoji-picker { position: absolute; bottom: 120%; left: 0; background: white; border: 1px solid #ddd; border-radius: 20px; padding: 5px 8px; display: flex; gap: 8px; z-index: 100; white-space: nowrap; }
.emoji-option { cursor: pointer; font-size: 1.2rem; transition: transform 0.1s; }
.emoji-option:hover { transform: scale(1.3); }
.picker-overlay { position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; z-index: 99; cursor: default; }
</style>