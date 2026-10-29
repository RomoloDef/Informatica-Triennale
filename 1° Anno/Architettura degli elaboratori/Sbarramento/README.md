# 🎯 Prove Pratiche di Sbarramento — RISC-V Assembly

Questa cartella è dedicata alla preparazione della **prova pratica di programmazione al calcolatore (prova di "Sbarramento")** per il corso di Architettura degli Elaboratori.

La prova richiede di scrivere un programma completo o una procedura/funzione in linguaggio assembly **RISC-V (RV32I)** che soddisfi le specifiche della traccia e superi una suite di test automatici di input/output.

---

## 📊 Analisi Statistica e Classificazione dei Temi d'Esame

Sulla base dell'analisi condotta sui **15 temi d'esame ufficiali** (disponibile in versione integrale nel documento **[analisi_esercizi_sbarramento.md](file:///Users/romolodeffereria/Desktop/Architettura/Sbarramento/analisi_esercizi_sbarramento.md)**), le prove d'esame si raggruppano in 4 macro-categorie:

| Categoria | Argomento Principale | Frequenza | Cartelle Esercizi | Priorità |
|---|---|---|---|---|
| **[A_Conversione_Basi](file:///Users/romolodeffereria/Desktop/Architettura/Sbarramento/A_Conversione_Basi/README.md)** | Conversioni tra basi (Binario, Ottale, Base 4, Hex, Dec) | **47%** (7/15) | `Sbarramento 5, 7, 8, 9, 11, 12, 14` | 🔴 **Massima** |
| **[B_Analisi_Stringhe](file:///Users/romolodeffereria/Desktop/Architettura/Sbarramento/B_Analisi_Stringhe/README.md)** | Scansione stringhe, parità, conteggio caratteri/coppie | **33%** (5/15) | `Sbarramento 1, 3, 4, 6, 13` | 🟠 **Alta** |
| **[C_Aritmetica_Binaria](file:///Users/romolodeffereria/Desktop/Architettura/Sbarramento/C_Aritmetica_Binaria/README.md)** | Operazioni binarie inline con separatori `+` e `-` | **13%** (2/15) | `Sbarramento 10, 15` | 🟡 **Media** |
| **[D_Matrici](file:///Users/romolodeffereria/Desktop/Architettura/Sbarramento/D_Matrici/README.md)** | Accesso e somme su matrici bidimensionali $N \times N$ | **7%** (1/15) | `Sbarramento 2` | 🟢 **Bassa** |
| **[UlterioriProve](file:///Users/romolodeffereria/Desktop/Architettura/Sbarramento/UlterioriProve/README.md)** | Batterie aggiuntive di esercizi raggruppati per categoria | — | `Categoria_A`, `Categoria_B`, `Categoria_C` | 🔵 **Pratica extra** |

---

## 🛠️ Come è Strutturata Ogni Cartella di Sbarramento

Ogni cartella d'esercizio (es. `Sbarramento11/`) costituisce un ambiente di lavoro autonomo e pronto all'uso, composto da:

- **`README.pdf`**: Il testo ufficiale della traccia d'esame con specifiche, formati di I/O, esempi ed eventuali indicazioni su procedure/convenzioni di chiamata.
- **`AE - Uso del computer...pdf`**: Vademecum con le regole e l'ambiente di laboratorio d'esame.
- **`program01.asm`**: Il file sorgente principale dove scrivere la soluzione.
- **`program01.vuoto.asm`**: Il template iniziale di partenza fornito ai candidati.
- **`rars1_6.jar`**: Il simulatore RISC-V Assembler & Runtime.
- **`test-*.in`** e **`test-*.expt`**: File di test (input e output atteso) usati per la validazione automatica.
- **`run.sh`** e **`Makefile`**: Script per lanciare la suite di test e confrontare i risultati.

---

## 🚀 Guida ai Comandi per Testare il Proprio Codice

Posizionandoti nella cartella dell'esercizio prescelto:

### 1. Test Automatico con lo Script `run.sh`
Per eseguire tutti i test case con un solo comando:
```bash
./run.sh program01.asm
```
Lo script eseguirà ogni `test-*.in`, salverà l'output prodotto e lo confronterà tramite `diff` con il rispettivo file `test-*.expt`, segnalando `OK` o le differenze riscontrate.

### 2. Test Tramite `make`
Se è presente il Makefile:
```bash
make
# oppure
make test
```

### 3. Debug Manuale con Simulatore Grafico (GUI)
Per analizzare passo-passo registro per registro con RARS:
```bash
java -jar rars1_6.jar &
```
Poi carica il file `program01.asm`, imposta i breakpoint e avvia l'esecuzione.

### 4. Esecuzione da Riga di Comando (CLI)
Per eseguire un singolo test case manualmente:
```bash
java -jar rars1_6.jar nc sm program01.asm < test-01.in
```

---

## 💡 Consigli Chiave per Superare la Prova

1. **Gestione del newline `\n` e del terminatore `\0`:** I test case leggono le stringhe spesso terminate da `\n` (`0x0A`) prima del byte zero (`0x00`). Verifica sempre entrambi i terminatori.
2. **Attenzione a scarto vs padding:** Nelle conversioni (es. binario $\rightarrow$ ottale), controlla scrupolosamente se i bit residui in eccesso devono essere **scartati** (come in Sbarramento 8 o 5) oppure **completati con zeri (padding)** (come in Sbarramento 7).
3. **Preservazione dei registri callee-saved:** Se la traccia richiede di definire una funzione separata, rispetta scrupolosamente l'ABI: salva `ra` e i registri `s0-s11` sullo stack se li modifichi.
