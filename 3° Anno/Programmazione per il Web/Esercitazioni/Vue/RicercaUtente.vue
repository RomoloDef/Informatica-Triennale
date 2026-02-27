<template>
  <div class="profile-card">
    <h2>Ricerca Utente ID: {{ userId }}</h2>

    <input type="number" v-model="userId" min="1">

    <div v-if="loading">Caricamento in corso...</div>

    <div v-else>
      <h3>Nome Completo: {{ fullName }}</h3>
      
      <p>Email: {{ userData.email }}</p>
      
      <button @click="resetUser">Resetta a Utente 1</button>
      
      <button @click="forceUpdateName">Aggiungi 'Super' al nome</button>
    </div>
  </div>
</template>

<script>
export default {
  // 1. STATO REATTIVO (DATA) 
  // Tutte le variabili che vogliamo siano "vive" devono essere qui.
  data() {
    return {
      userId: 1,
      userData: {
        first: 'Mario',
        last: 'Rossi',
        email: 'mario@test.com'
      },
      loading: false
    }
  },

  // 2. COMPUTED PROPERTIES
  // Queste vengono ricalcolate AUTOMATICAMENTE se cambia userData.first o userData.last.
  // Se 'userId' cambia ma il nome resta uguale, questa funzione NON viene rieseguita (Caching).
  computed: {
    fullName() {
      console.log("Calcolo fullName in corso..."); // Vedrai questo log solo se il nome cambia davvero
      return this.userData.first + ' ' + this.userData.last;
    }
  },

  // 3. WATCHERS
  // Qui "osserviamo" la variabile 'userId'.
  // Appena cambia (grazie all'input sopra), eseguiamo questa funzione.
  watch: {
    userId(newId, oldId) {
      console.log(`L'ID è cambiato da ${oldId} a ${newId}`);
      // I watchers sono perfetti per operazioni asincrone (simuliamo una chiamata API) 
      this.fetchNewData(newId);
    }
  },

  // 4. METODI 
  // Funzioni che cambiano lo stato o gestiscono eventi.
  // A differenza delle computed, vengono eseguite ogni volta che le chiami. 
  methods: {
    async fetchNewData(id) {
      this.loading = true;
      
      // Simuliamo un'attesa di rete (API)
      setTimeout(() => {
        // Modifichiamo lo stato reattivo usando 'this' 
        this.userData = {
          first: 'Utente',
          last: 'Numero ' + id,
          email: `user${id}@test.com`
        };
        this.loading = false;
        
        // NEXT TICK [cite: 83, 91]
        // Se volessimo fare qualcosa SUBITO dopo che il DOM si è aggiornato con i nuovi dati
        // dovremmo usare this.$nextTick(() => { ... })
      }, 1000);
    },

    resetUser() {
      this.userId = 1; // Questo farà scattare di nuovo il watcher di 'userId'!
    },
    
    forceUpdateName() {
        this.userData.first = "Super " + this.userData.first;
        // Modificando 'first', la computed 'fullName' si accorgerà del cambio e si aggiornerà.
    }
  },

  // 5. LIFECYCLE HOOKS 
  // mounted() viene chiamato appena il componente appare a schermo.
  mounted() {
    console.log("Il componente è montato e visibile! [cite: 219]");
    // È buona norma caricare i dati iniziali qui 
    this.fetchNewData(this.userId);
  },
  
  // Esempio di un altro hook
  beforeUnmount() {
      console.log("Il componente sta per essere distrutto. Pulizia in corso... ");
  }
}
</script>