# Esercizi di Architettura dei Calcolatori - Assembly RISC-V (Istruzioni Base)

Questo repository contiene una raccolta di esercizi pratici scritti in **Assembly RISC-V (RV32I)**. 
Gli esercizi sono stati sviluppati per mettere in pratica i concetti fondamentali dell'architettura dei calcolatori e il set di istruzioni base della CPU.

## 📚 Argomenti Trattati

Gli script presenti in questa repository coprono le seguenti funzionalità base dell'Assembly RISC-V:

* **Gestione della Memoria:** Lettura e scrittura dalla memoria RAM (sezione `.data`) ai registri della CPU utilizzando istruzioni di Load/Store (`lw`, `sw`) e gestione degli indirizzi con gli offset.
* **Operazioni Aritmetiche e Logiche:** Somme, sottrazioni e utilizzo di operatori bit a bit (`and`, `xor`, shift logici) per la manipolazione dei dati e la creazione di maschere di bit (bitmask).
* **System Calls:** Utilizzo dell'istruzione `ecall` (tramite il simulatore RARS) per stampare risultati a schermo e terminare correttamente l'esecuzione dei programmi.

## 📝 Lista delle Tracce / Esercizi

Qui di seguito alcune delle tracce risolte in questa prima fase di studio:

1. Leggere tre valori dalla memoria, sommare i primi due, sottrarre il terzo e salvare il risultato finale in una nuova locazione di memoria. I dati da inserire sono: 15, 25, 10
2. Dato un array di 4 numeri, sovrascrivre il terzo numero con la somma del primo e del secondo numero
3.  Verificare che un anno precaricato in un registro è divisibile per 4. Usa un'operazione logica (andi) per controllare i due bit meno significativi. Se è divisibile per 4, imposta il registro t1 a 1, altrimenti impostalo a 0 usando un salto condizionato. Inizializza un registro t0 con il valore dell'anno (es. 2024)
4. Effettuare la media aritmetica di 5 numeri positivi definiti in memoria e stampare il risultato a schermo
5. Scrivere un programma che dati due numerin (word) che indicano spazio e tempo, calcolare la velocità in $t0
6. Scrivere un programma che converta un valore da scala Celsius a scala Fahrenheit. Riportare il risultato in $t0

## 🛠️ Strumenti Utilizzati

Tutto il codice è stato scritto e testato utilizzando **RARS** (RISC-V Assembler and Runtime Simulator).

### Come eseguire il codice:
1. Scarica il file `.jar` di RARS.
2. Apri uno dei file `.s` o `.asm` presenti in questa repository.
3. Vai su `Run` -> `Assemble` (oppure premi F3).
4. Vai su `Run` -> `Go` (oppure premi F5) per eseguire il programma e visualizzare l'output nel terminale di RARS.