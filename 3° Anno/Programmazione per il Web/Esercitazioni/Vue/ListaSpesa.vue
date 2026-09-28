<template>
  <div id="app">
  
    <h1>{{ titolo.toUpperCase() }}</h1>

    <div class="input-group">
      <input 
        type="text" 
        v-model="nuovoProdotto" 
        placeholder="Cosa devi comprare?"
      >

      <button 
        :disabled="nuovoProdotto.length === 0" 
        @click="aggiungi"
      >
        Aggiungi
      </button>
    </div>

    <p v-if="listaSpesa.length === 0">
      Non hai nulla da comprare!
    </p>

    <p v-show="listaSpesa.length > 5">
      Wow, hai un sacco di cose da comprare oggi!
    </p>

    <ul>
      <li v-for="oggetto in listaSpesa">
        
        {{ oggetto }}
        
        <button @click="rimuovi(oggetto)">X</button>
      </li>
    </ul>

  </div>
</template>

<script>
// La parte <script> definisce il VIEWMODEL e il MODEL dell'applicazione
export default {
  // DATA: Qui definiamo lo STATO iniziale dell'app (il Model) 
  // Tutte le variabili qui dentro sono "reattive": se cambiano, l'HTML si aggiorna.
  data() {
    return {
      titolo: "La mia spesa",
      nuovoProdotto: "", // Questa stringa vuota è collegata all'input sopra col v-model
      listaSpesa: []     // Questo array vuoto si riempirà man mano
    }
  },
  
  // METHODS: Qui mettiamo le funzioni (logica) che rispondono agli eventi dell'utente
  methods: {
    aggiungi() {
      // 'this' serve per accedere alle variabili definite in data()
      this.listaSpesa.push(this.nuovoProdotto);
      
      // Resettiamo l'input. Grazie al v-model, anche la casella di testo si svuoterà!
      this.nuovoProdotto = ""; 
    },
    
    rimuovi(daCancellare) {
      // Filtriamo l'array per rimuovere l'oggetto cliccato
      this.listaSpesa = this.listaSpesa.filter(item => item !== daCancellare);
    }
  }
}
</script>

<style scoped>
/* Lo stile scoped si applica SOLO a questo componente */
.input-group {
  margin: 20px 0;
}
</style>