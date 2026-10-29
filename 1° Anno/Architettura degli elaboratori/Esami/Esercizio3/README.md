# ⏱️ Esercizio 3: CPU RISC-V con Pipeline a 5 Stadi e Gestione degli Hazard

Questa cartella raccoglie le tracce e i testi d'esame relativi al **terzo esercizio** della prova scritta di Architettura degli Elaboratori.

---

## 📌 Contenuto della Cartella

- [Esercizio 3-1.pdf](file:///Users/romolodeffereria/Desktop/Architettura/Esami/Esercizio3/Esercizio%203-1.pdf): Traccia Appello 1
- [Esercizio 3-2.pdf](file:///Users/romolodeffereria/Desktop/Architettura/Esami/Esercizio3/Esercizio%203-2.pdf): Traccia Appello 2
- [Esercizio 3-3.pdf](file:///Users/romolodeffereria/Desktop/Architettura/Esami/Esercizio3/Esercizio%203-3.pdf): Traccia Appello 3
- [Esercizio 3-4.pdf](file:///Users/romolodeffereria/Desktop/Architettura/Esami/Esercizio3/Esercizio%203-4.pdf): Traccia Appello 4
- [Esercizio 3-5.pdf](file:///Users/romolodeffereria/Desktop/Architettura/Esami/Esercizio3/Esercizio%203-5.pdf): Traccia Appello 5
- [Esercizio 3-6.pdf](file:///Users/romolodeffereria/Desktop/Architettura/Esami/Esercizio3/Esercizio%203-6.pdf): Traccia Appello 6
- [Esercizio 3-7.png](file:///Users/romolodeffereria/Desktop/Architettura/Esami/Esercizio3/Esercizio%203-7.png): Traccia/schema grafico integrativo

---

## 🔄 I 5 Stadi della Pipeline RISC-V

$$\text{IF (Fetch)} \longrightarrow \text{ID (Decode)} \longrightarrow \text{EX (Execute)} \longrightarrow \text{MEM (Memory)} \longrightarrow \text{WB (Write Back)}$$

1. **IF (Instruction Fetch):** Prelievo dell'istruzione dalla Instruction Memory puntata dal PC e aggiornamento $PC \leftarrow PC + 4$.
2. **ID (Instruction Decode):** Decodifica dell'istruzione, lettura dei registri sorgente dal Register File ed estensione del segno dell'eventuale immediato.
3. **EX (Execute):** Calcolo dell'ALU (operazione aritmetico-logica, indirizzo di memoria per lw/sw, o confronto per branch).
4. **MEM (Memory Access):** Lettura o scrittura nella memoria dati (Data Memory).
5. **WB (Write Back):** Scrittura del risultato nel registro destinazione all'interno del Register File.

---

## ⚠️ Tipologie di Hazard e Regole di Risoluzione

### 1. Data Hazard (RAW - Read After Write)
Si verifica quando un'istruzione tenta di leggere un registro sorgente (`rs1` o `rs2`) che non è ancora stato scritto dall'istruzione precedente (`rd`).

- **Senza Unità di Forwarding:**
  - Il dato scritto nello stadio **WB** diventa disponibile per la lettura nello stadio **ID** solo al ciclo successivo (o nella seconda metà del ciclo se il Register File è a doppia porta).
  - Distanza 1 (istruzione adiacente): **2 cicli di stallo** (bolle in ID).
  - Distanza 2: **1 ciclo di stallo**.
  - Distanza $\ge 3$: **Nessuno stallo**.

- **Con Unità di Forwarding:**
  - La Forwarding Unit inoltra il dato calcolato dallo stadio **EX** o **MEM** direttamente agli ingressi dell'ALU nello stadio **EX**.
  - **Istruzioni R-type / aritmetiche:** **0 cicli di stallo** (il dato viene inoltrato in tempo zero).
  - **Hazard Load-Use (lw seguita da uso del dato):** Il dato caricato dalla memoria è disponibile solo alla fine dello stadio **MEM** $\rightarrow$ **1 ciclo di stallo inevitabile** anche con forwarding.

### 2. Control Hazard (Branch e Salti Condizionati)
- In caso di salto condizionato (`beq`, `bne`, `blt`), se il branch viene preso (*taken*), le istruzioni già prelevate negli stadi precedenti devono essere cancellate (**flush**), introducendo 1 o 2 bolle di penalità.

---

## 📊 Calcolo dei Cicli di Clock Totali

Per calcolare il tempo totale di esecuzione:
1. **Pre-ciclo:** Conteggio delle istruzioni iniziali di setup prima dell'inizio del ciclo iterativo.
2. **Ciclo (Loop):** Moltiplicare il numero di cicli di clock per iterazione per il numero totale di iterazioni $N$.
3. **Post-ciclo:** Conteggio delle istruzioni eseguite dopo l'uscita dal ciclo.
4. **Svuotamento Pipeline:** Aggiungere i cicli necessari per far uscire l'ultima istruzione dalla pipeline (4 cicli aggiuntivi dopo l'IF dell'ultima istruzione).

---

## 📖 Guida Consigliata
Per tabelle riassuntive, diagrammi temporali ed esempi pratici completi:  
👉 **[GuidaEsercizio3.pdf](file:///Users/romolodeffereria/Desktop/Architettura/Esami/GuidaEsercizio3.pdf)**
