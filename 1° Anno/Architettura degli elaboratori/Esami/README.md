# 📝 Prove d'Esame — Architettura degli Elaboratori

Questa directory contiene l'intero archivio di preparazione per la **prova scritta teorico-progettuale** dell'esame di Architettura degli Elaboratori (RISC-V).

L'esame standard è strutturato in **3 macro-esercizi**, ognuno focalizzato su una specifica area tematica fondamentale dell'architettura hardware.

---

## 🗂️ Struttura della Cartella

```
Esami/
├── 📄 README.md               # Questa guida introduttiva
├── 📄 GuidaEsercizio1.pdf     # Metodologia e prontuario formule per l'Esercizio 1 (Cache)
├── 📄 GuidaEsercizio2.pdf     # Guida alla CPU a ciclo singolo e nuove istruzioni (Esercizio 2)
├── 📄 GuidaEsercizio3.pdf     # Guida alla Pipeline RISC-V a 5 stadi e Hazard (Esercizio 3)
├── 📁 Completo/               # Tracce complete degli appelli (Appelli 1-6)
├── 📁 Esercizio1/             # Tracce e schermate per l'Esercizio 1 (Cache L1/L2, AMAT)
├── 📁 Esercizio2/             # Tracce e schemi per l'Esercizio 2 (Ciclo Singolo, Datapath)
└── 📁 Esercizio3/             # Tracce e diagrammi per l'Esercizio 3 (Pipeline & Forwarding)
```

---

## 🔍 I 3 Esercizi d'Esame nel Dettaglio

### 1️⃣ [Esercizio 1: Gerarchia di Memoria e Cache](file:///Users/romolodeffereria/Desktop/Architettura/Esami/Esercizio1/README.md)
*Consultare la guida metodologica: [GuidaEsercizio1.pdf](file:///Users/romolodeffereria/Desktop/Architettura/Esami/GuidaEsercizio1.pdf)*

- **Obiettivo:** Analizzare una sequenza di accessi a memoria (indirizzi a 32 bit), determinare per ciascun accesso la suddivisione dei bit in **Tag, Index e Offset**, e tracciare lo stato della Cache (L1 ed eventuale L2).
- **Competenze richieste:**
  - Calcolo della dimensione dei blocchi e dei set:
    $$\text{Dimensione Blocco (byte)} = \text{Num Parole} \times 4$$
    $$\text{Block} = \left\lfloor \frac{\text{Indirizzo}}{\text{Dimensione Blocco}} \right\rfloor$$
    $$\text{Index} = \text{Block} \pmod{\text{Num Set}}$$
    $$\text{Tag} = \left\lfloor \frac{\text{Block}}{\text{Num Set}} \right\rfloor$$
  - Determinazione di **HIT** o **MISS** e classificazione del tipo di miss:
    - **Cold (Freddo):** Primo accesso assoluto al blocco.
    - **Capacity (Capacità):** La cache era completamente piena prima del rimpiazzo.
    - **Conflict (Conflitto):** Il set specifico era pieno, ma c'erano altri set liberi nella cache.
  - Politica di rimpiazzo **LRU** (Least Recently Used).
  - Calcolo del tempo medio di accesso alla memoria (**AMAT**):
    $$\text{AMAT} = \text{Hit Time} + (\text{Miss Rate} \times \text{Miss Penalty})$$
  - Calcolo dell'offset di parola e del numero di pagina virtuale.

---

### 2️⃣ [Esercizio 2: CPU RISC-V a Ciclo Singolo ed Estensione Datapath](file:///Users/romolodeffereria/Desktop/Architettura/Esami/Esercizio2/README.md)
*Consultare la guida metodologica: [GuidaEsercizio2.pdf](file:///Users/romolodeffereria/Desktop/Architettura/Esami/GuidaEsercizio2.pdf)*

- **Obiettivo:** Partendo dal Datapath canonico di una CPU RISC-V a ciclo singolo, progettare le modifiche hardware necessarie per implementare una **nuova istruzione inventata** dal docente.
- **Competenze richieste:**
  - **Modifica del Datapath:** Aggiunta di multiplexer, sommatori, estensori di segno o porte logiche, tracciando le nuove linee dati in ingresso/uscita verso l'ALU, i Registri o la Data Memory.
  - **Tabella dei Segnali di Controllo:** Assegnare i valori per la nuova istruzione (e verificare quelli standard):
    - `RegWrite`, `ALUSrc`, `MemRead`, `MemWrite`, `MemtoReg`, `Branch`, `ALUOp`.
  - **Codifica della Word a 32 bit:**
    - Identificare il formato RISC-V più appropriato (R, I, S, B, U, J).
    - Assegnare i campi di bit: `opcode` [6:0], `rd` [11:7], `funct3` [14:12], `rs1` [19:15], `rs2` [24:20], `funct7` [31:25] / `immediate`.
  - **Casi reali trattati nei 6 appelli:**
    - Appello 1: `lwig outreg, val1, val2_address`
    - Appello 2: `bltsafe rd, rs1, rs2`
    - Appello 3: `jalf rd, rs1, immediate`
    - Appello 4: `msum a, b, c, d, m`
    - Appello 5: `beqi rs1, immediate, offset`
    - Appello 6: `seq rd, rs1, rs2`

---

### 3️⃣ [Esercizio 3: CPU RISC-V con Pipeline a 5 Stadi e Hazard](file:///Users/romolodeffereria/Desktop/Architettura/Esami/Esercizio3/README.md)
*Consultare la guida metodologica: [GuidaEsercizio3.pdf](file:///Users/romolodeffereria/Desktop/Architettura/Esami/GuidaEsercizio3.pdf)*

- **Obiettivo:** Data una sequenza di codice assembly (con o senza loop), tracciare l'avanzamento delle istruzioni nei 5 stadi di pipeline:
  $$\text{IF (Instruction Fetch)} \rightarrow \text{ID (Instruction Decode)} \rightarrow \text{EX (Execute)} \rightarrow \text{MEM (Memory Access)} \rightarrow \text{WB (Write Back)}$$
- **Competenze richieste:**
  - **Data Hazard (Dipendenze di dato RAW):**
    - Riconoscere dipendenze tra registri di destinazione `rd` e registri sorgente `rs1`/`rs2`.
    - **Senza Forwarding:** Sono richiesti stalli (fino a 2 cicli di bolla in ID).
    - **Con Forwarding:** I dati calcolati dall'ALU (stadio EX) o caricati da memoria (stadio MEM) vengono inoltrati direttamente allo stadio EX dell'istruzione successiva (stallo solo nel caso critico *Load-Use* di 1 ciclo).
  - **Control Hazard (Diramazioni e Salti):**
    - Risoluzione del branch in ID o EX e relativo svuotamento della pipeline (*flush* / bolle di penalità).
  - **Calcolo delle Prestazioni:**
    - Numero complessivo di colpi di clock richiesti per completare il programma (pre-ciclo, iterazioni del ciclo, post-ciclo).
    - Calcolo del **CPI effettivo** ($\text{Cicli Totali} / \text{Istruzioni Totali}$) e confronto delle prestazioni (*Speedup*).

---

## 📂 [Completo: I 6 Appelli d'Esame](file:///Users/romolodeffereria/Desktop/Architettura/Esami/Completo/README.md)

Nella sottocartella `Completo/` sono presenti i PDF integrali di 6 appelli d'esame completi:
- [Appello 1.pdf](file:///Users/romolodeffereria/Desktop/Architettura/Esami/Completo/Appello1.pdf)
- [Appello 2.pdf](file:///Users/romolodeffereria/Desktop/Architettura/Esami/Completo/Appello2.pdf)
- [Appello 3.pdf](file:///Users/romolodeffereria/Desktop/Architettura/Esami/Completo/Appello3.pdf)
- [Appello 4.pdf](file:///Users/romolodeffereria/Desktop/Architettura/Esami/Completo/Appello4.pdf)
- [Appello 5.pdf](file:///Users/romolodeffereria/Desktop/Architettura/Esami/Completo/Appello5.pdf)
- [Appello 6.pdf](file:///Users/romolodeffereria/Desktop/Architettura/Esami/Completo/Appello6.pdf)
