// Le istruzioni js sono comandi che dicono al browser cosa fare
// Ognuna termina con un punto e virgola ;

// La sintassi la si trova nella slides

/* 
JavaScript può accedere e modificare il Document Object Model (DOM). 
Il browser trasforma il tuo codice HTML
in una struttura ad albero (oggetti) che JavaScript può leggere e manipolare
*/

// --- MODIFICA CONTENUTO HTML ---
// Seleziona il primo H1 e cambia il testo
const titoloPrincipale = document.querySelector("h1");
titoloPrincipale.innerHTML = "JavaScript è attivo!"; 

// --- MODIFICA STILE CSS ---
// Cambia il colore di sfondo del body
document.querySelector("body").style.backgroundColor = "#fff8e1"; // Giallo crema

// --- MODIFICA ATTRIBUTI ---
// Carica l'immagine nel tag img che era vuoto
const miaImmagine = document.querySelector("img");
miaImmagine.src = "https://upload.wikimedia.org/wikipedia/commons/6/6a/JavaScript-logo.png";
miaImmagine.style.width = "150px"; // Rimpicciolisci un po' l'immagine

// --- INTERAZIONE ---
// Cliccando sul primo paragrafo, questo diventa rosso
const primoParagrafo = document.querySelector("p");

primoParagrafo.onclick = function() {
    primoParagrafo.style.color = "red";
    primoParagrafo.innerHTML = "Hai cliccato qui! Il testo è diventato rosso.";
}

console.log("Tutte le modifiche sono state applicate!");


