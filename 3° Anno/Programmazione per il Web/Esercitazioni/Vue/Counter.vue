<template>
    <div class = "Counter">
        <h1> Il conteggio è: {{ count }} </h1>
        <button @click="incrementa">Aumenta</button>
    </div>
</template>

<script>
// Options API: Definiamo la logica usando un oggetto di opzioni
export default {
  // data() restituisce lo stato reattivo.
  data() {
    return {
      count: 0 // Questo è il dato grezzo. Se cambia, la View si aggiorna da sola.
    }
  },
  
  methods: {
    // Logica di Business
    incrementa() {
      // Reattività: Modifichiamo solo la variabile JS.
      // Vue "osserva" questo cambiamento e aggiorna l'HTML automaticamente 
      this.count++; 
    }
  }
}
</script>

<style scoped>
.container {
  text-align: center;
  margin-top: 20px;
}
button {
  background-color: #42b983; /* Verde Vue */
  color: white;
  padding: 10px 20px;
  border: none;
  cursor: pointer;
}
</style>

