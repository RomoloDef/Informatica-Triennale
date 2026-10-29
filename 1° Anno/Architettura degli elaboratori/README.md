# 🏛️ Corso di Architettura degli Elaboratori (RISC-V)

Benvenuto nel repository principale dei materiali di studio, esercitazioni e preparazione d'esame per il corso universitario di **Architettura degli Elaboratori**, focalizzato sull'architettura e set di istruzioni **RISC-V**.

---

## 🗺️ Mappa e Struttura del Repository

La directory è strutturata in macro-aree tematiche che coprono la teoria, le esercitazioni pratiche di programmazione in Assembly RISC-V e la preparazione alle prove scritte e di laboratorio.

```
Architettura/
├── 📄 Capitolo 2 - Architettura.pdf     # Teoria: Set di istruzioni RISC-V (linguaggio macchina)
├── 📄 Capitolo 4 - Architettura.pdf     # Teoria: Il Processore (Ciclo Singolo, Pipeline, Hazard)
├── 📄 Capitolo 5 - Architettura.pdf     # Teoria: Gerarchia di memoria (Cache, Memoria Virtuale)
├── 📁 Esami/                            # Materiale per la prova scritta teorica/progettuale
│   ├── 📁 Completo/                     # Testi completi d'esame (Appelli 1-6)
│   ├── 📁 Esercizio1/                   # Prove pratiche: Cache L1/L2, AMAT e Paginazione
│   ├── 📁 Esercizio2/                   # Prove pratiche: CPU a Ciclo Singolo ed estensione Datapath
│   ├── 📁 Esercizio3/                   # Prove pratiche: CPU con Pipeline a 5 Stadi e Hazard
│   ├── 📄 GuidaEsercizio1.pdf           # Guida metodologica e formule per Esercizio 1 (Cache)
│   ├── 📄 GuidaEsercizio2.pdf           # Guida metodologica e risoluzioni Esercizio 2 (Ciclo Singolo)
│   ├── 📄 GuidaEsercizio3.pdf           # Guida metodologica e risoluzioni Esercizio 3 (Pipeline)
│   └── 📄 README.md                     # Guida dettagliata alla cartella Esami
├── 📁 Esercizi/                         # 10 Programmi didattici fondamentali in RISC-V (.s)
│   ├── 📄 AE-1.s ... AE-10.s            # Codici sorgenti commentati passo per passo
│   └── 📄 README.md                     # Scheda dettagliata e spiegazione di ogni esercizio
└── 📁 Sbarramento/                      # Preparazione alla prova pratica di sbarramento al calcolatore
    ├── 📁 A_Conversione_Basi/           # Esercizi su conversioni tra basi numeriche (47% prove)
    ├── 📁 B_Analisi_Stringhe/           # Esercizi su scansione, parsing e conteggio stringhe (33%)
    ├── 📁 C_Aritmetica_Binaria/         # Esercizi su somme e sottrazioni binarie inline (13%)
    ├── 📁 D_Matrici/                    # Esercizi su matrici bidimensionali in memoria (7%)
    ├── 📁 UlterioriProve/               # Archivio di test addizionali per categoria
    ├── 📄 analisi_esercizi_sbarramento.md # Studio statistico approfondito sui 15 temi d'esame
    └── 📄 README.md                     # Guida completa allo sbarramento e all'ambiente RARS
```

---

## 📚 1. Teoria e Dispense del Corso

I file PDF nella radice contengono i capitoli cardine del testo di riferimento (*Computer Organization and Design - RISC-V Edition*, Patterson & Hennessy):

1. **[Capitolo 2 - Architettura.pdf](file:///Users/romolodeffereria/Desktop/Architettura/Capitolo%202%20-%20Architettura.pdf)**:
   - Istruzioni: il linguaggio del calcolatore.
   - Formati di istruzione RISC-V (R, I, S, B, U, J).
   - Operazioni aritmetico-logiche, salti condizionati, gestione della memoria e convenzioni di chiamata (ABI, registri `a0-a7`, `t0-t6`, `s0-s11`, stack pointer `sp`).
2. **[Capitolo 4 - Architettura.pdf](file:///Users/romolodeffereria/Desktop/Architettura/Capitolo%204%20-%20Architettura.pdf)**:
   - Il Processore: architettura a ciclo singolo.
   - Progettazione del Datapath (PC, Instruction Memory, Register File, ALU, Data Memory).
   - Unità di controllo e generazione dei segnali.
   - Architettura con **Pipeline a 5 stadi** (IF, ID, EX, MEM, WB).
   - Risoluzione dei conflitti (Hazard): strutturali, sui dati (con stalli o unità di Forwarding) e sul controllo (branch prediction, flush/bolle).
3. **[Capitolo 5 - Architettura.pdf](file:///Users/romolodeffereria/Desktop/Architettura/Capitolo%205%20-%20Architettura.pdf)**:
   - Gerarchia di memoria: principio di località temporale e spaziale.
   - Cache memory: diretta, a N vie set-associative, completamente associativa.
   - Politiche di rimpiazzo (LRU, FIFO) e di scrittura (Write-Through vs Write-Back).
   - Calcolo delle prestazioni (AMAT, Miss Penalty).
   - Memoria Virtuale, TLB (Translation Lookaside Buffer) e paginazione.

---

## 🎯 2. Macro-Aree del Repository

### 📝 [Esami](file:///Users/romolodeffereria/Desktop/Architettura/Esami)
Dedicata alla preparazione della **prova d'esame scritta teorico-progettuale**. Comprende:
- **Guide analitiche passo-passo** per le tre domande canoniche del compito d'esame (`GuidaEsercizio1.pdf`, `GuidaEsercizio2.pdf`, `GuidaEsercizio3.pdf`).
- Cartelle dedicate con tracce divise per esercizio (`Esercizio1/`, `Esercizio2/`, `Esercizio3/`).
- Raccolta di appelli completi d'esame (`Completo/`).
👉 Per tutti i dettagli, consulta il [README della cartella Esami](file:///Users/romolodeffereria/Desktop/Architettura/Esami/README.md).

### 💻 [Esercizi](file:///Users/romolodeffereria/Desktop/Architettura/Esercizi)
Contiene 10 programmi didattici fondamentali (`AE-1.s` a `AE-10.s`) scritti in assembly RISC-V commentati riga per riga. Sono il punto di partenza ideale per apprendere:
- Operazioni di base e syscall I/O (`ecall`).
- Indirizzamento della memoria e vincoli di allineamento a 32 bit (`lw`, `sw`).
- Cicli iterativi e diramazioni (`blt`, `bge`, `beq`, `bne`, `j`).
- Algoritmi classici: ricerca massimo, somme pari/dispari, filtraggio con soglia, manipolazione stringhe ASCII e maiuscolo/minuscolo.
👉 Per visualizzare ogni esercizio spiegato nel dettaglio, consulta il [README della cartella Esercizi](file:///Users/romolodeffereria/Desktop/Architettura/Esercizi/README.md).

### 🚀 [Sbarramento](file:///Users/romolodeffereria/Desktop/Architettura/Sbarramento)
Dedicata alla **prova pratica preliminare di programmazione al calcolatore (Sbarramento)**.
- Raccoglie 15 tracce d'esame reali suddivise in 4 macro-categorie statistiche:
  - **A: Conversione tra Basi** (47% delle prove: Binario $\leftrightarrow$ Ottale/Base 4/Hex/Decimale).
  - **B: Analisi e Conteggio su Stringhe** (33% delle prove: scansione char, parità, conteggio coppie).
  - **C: Aritmetica Binaria con Operatori Inline** (13% delle prove: espressioni binarie con `+` e `-`).
  - **D: Operazioni su Matrici** (7% delle prove: scansione array bidimensionali N×N in memoria).
- Ogni cartella contiene l'ambiente di test autonomo con simulatore **RARS**, script di correzione automatica `run.sh`, `Makefile` e file di test I/O.
- Include un'ampia sezione di prove supplementari (`UlterioriProve/`).
👉 Per consultare la guida metodologica, pattern e test suite, apri il [README della cartella Sbarramento](file:///Users/romolodeffereria/Desktop/Architettura/Sbarramento/README.md) e l'[Analisi Statistica Completa](file:///Users/romolodeffereria/Desktop/Architettura/Sbarramento/analisi_esercizi_sbarramento.md).

---

## 🛠️ Strumenti Consigliati

Per eseguire, testare ed effettuare il debug dei programmi assembly in questo repository:
- **[RARS (RISC-V Assembler and Runtime Simulator)](https://github.com/TheThirdOne/rars)**: il simulatore didattico ufficiale per RISC-V. Un archivio eseguibile `rars1_6.jar` è già presente all'interno dei test di sbarramento.
- **Esecuzione con interfaccia grafica:**
  ```bash
  java -jar rars1_6.jar
  ```
- **Esecuzione automatizzata da terminale:**
  ```bash
  java -jar rars1_6.jar nc sm program01.asm < test-01.in
  ```
- **Script automatico per sbarramento:**
  ```bash
  ./run.sh program01.asm
  ```
