# 💻 Esercizi Pratici in Assembly RISC-V

Questa cartella raccoglie **10 programmi didattici fondamentali** (`AE-1.s` ... `AE-10.s`) scritti per l'architettura RISC-V (RV32I).  
Ogni esercizio è ampiamente commentato nel codice per illustrare i costrutti fondamentali del linguaggio assembly: dall'aritmetica di base alla gestione della memoria, dai cicli e array fino alla manipolazione delle stringhe ASCII.

---

## 📋 Tabella Riassuntiva degli Esercizi

| File | Titolo / Obiettivo | Istruzioni Chiave | Argomento Didattico |
|---|---|---|---|
| [AE-1.s](file:///Users/romolodeffereria/Desktop/Architettura/Esercizi/AE-1.s) | Calcolo di un'espressione aritmetica | `li`, `add`, `sub`, `mv`, `ecall` | Aritmetica di base, registri e syscall |
| [AE-2.s](file:///Users/romolodeffereria/Desktop/Architettura/Esercizi/AE-2.s) | Accesso a vettori con offset | `la`, `lw`, `sw`, `add` | Indirizzamento memoria, parole a 32 bit |
| [AE-3.s](file:///Users/romolodeffereria/Desktop/Architettura/Esercizi/AE-3.s) | Ricerca del massimo in un array | `blt`, `jal`, `or`, `sw` | Salti condizionati e aggiornamento massimo |
| [AE-4.s](file:///Users/romolodeffereria/Desktop/Architettura/Esercizi/AE-4.s) | Somme separate per indici pari e dispari | `bge`, `addi`, `slli`, `lw`, `sw` | Cicli con contatore, offset dinamico |
| [AE-5.s](file:///Users/romolodeffereria/Desktop/Architettura/Esercizi/AE-5.s) | Somma positivi e conteggio negativi | `bgtz`, `bltz`, `add`, `addi` | Diramazioni condizionate su segno |
| [AE-6.s](file:///Users/romolodeffereria/Desktop/Architettura/Esercizi/AE-6.s) | Filtraggio con soglia (azzeramento/raddoppio) | `blt`, `add`, `sw`, `addi` | Modifica in-place della memoria |
| [AE-7.s](file:///Users/romolodeffereria/Desktop/Architettura/Esercizi/AE-7.s) | Somma vettoriale $C[i] = A[i] + B[i]$ | `la`, `lw`, `add`, `sw`, `addi` | Gestione simultanea di 3 puntatori |
| [AE-8.s](file:///Users/romolodeffereria/Desktop/Architettura/Esercizi/AE-8.s) | Conteggio occorrenze di un carattere bersaglio | `lb`, `beqz`, `beq`, `addi` | Scansione stringhe ASCII con `\0` |
| [AE-9.s](file:///Users/romolodeffereria/Desktop/Architettura/Esercizi/AE-9.s) | Sostituzione spazi `' '` con underscore `'_'` | `lb`, `sb`, `li`, `beq` | Modifica caratteri in-place |
| [AE-10.s](file:///Users/romolodeffereria/Desktop/Architettura/Esercizi/AE-10.s) | Conversione minuscolo $\rightarrow$ MAIUSCOLO | `blt`, `bgt`, `addi`, `sb` | Verifica intervalli ASCII e case-conversion |

---

## 🔍 Descrizione Dettagliata dei Singoli Esercizi

### 🔹 [AE-1.s](file:///Users/romolodeffereria/Desktop/Architettura/Esercizi/AE-1.s) — Espressione Aritmetica Semplice
- **Consegna:** Calcolare $(b - c) + (d - e)$ con valori costanti e stampare il risultato a video.
- **Logica:**
  - Carica i valori immediati nei registri con `li`.
  - Esegue le differenze parziali con `sub`.
  - Somma i due risultati parziali con `add`.
  - Sposta il valore in `a0` con `mv a0, x14`, imposta la syscall di stampa intero (`li a7, 1`) ed esegue `ecall`.
  - Termina correttamente il programma con `li a7, 10; ecall`.

### 🔹 [AE-2.s](file:///Users/romolodeffereria/Desktop/Architettura/Esercizi/AE-2.s) — Traduzione di istruzione su Vettore
- **Consegna:** Tradurre in assembly l'istruzione C: `vector[12] = vector[6] + n`.
- **Logica:**
  - Carica l'indirizzo base dell'array `vector` nel registro con `la s5, vector`.
  - Rispetta il vincolo di allineamento a 32 bit (4 byte per word): `vector[6]` si trova all'offset $6 \times 4 = 24$, quindi `lw x9, 24(s5)`.
  - Somma il valore di `n` con `add x10, x9, t1`.
  - Salva il risultato nella posizione `vector[12]` all'offset $12 \times 4 = 48$ con `sw x10, 48(s5)`.

### 🔹 [AE-3.s](file:///Users/romolodeffereria/Desktop/Architettura/Esercizi/AE-3.s) — Ricerca del Massimo
- **Consegna:** Determinare il massimo tra 4 valori memorizzati in un array e salvarlo nella variabile `salvataggio`.
- **Logica:**
  - Carica il primo elemento e lo assume come massimo provvisorio in `t1`.
  - Esegue confronti sequenziali mediante `blt` (Branch if Less Than): se un elemento è maggiore del massimo corrente, salta alla relativa etichetta di aggiornamento (`or t1, zero, x_val`), altrimenti procede al controllo successivo.
  - Al termine, memorizza il massimo finale con `sw t1, salvataggio, s5`.

### 🔹 [AE-4.s](file:///Users/romolodeffereria/Desktop/Architettura/Esercizi/AE-4.s) — Somme Pari e Dispari
- **Consegna:** Dato un vettore di dimensione $N$, calcolare due somme distinte:
  1. Somma dei valori con indice dispari (1, 3, 5, ...).
  2. Somma dei valori con indice pari (0, 2, 4, ...).
- **Logica:**
  - Imposta un ciclo iterativo controllato da un registro contatore d'indice `i`.
  - Calcola l'offset a ogni passo con shift logico `slli t3, t0, 2` ($i \times 4$).
  - Utilizza l'operazione bitwise `andi` con 1 sul contatore per determinare se l'indice è pari o dispari e accumulare nel rispettivo registro.

### 🔹 [AE-5.s](file:///Users/romolodeffereria/Desktop/Architettura/Esercizi/AE-5.s) — Somma Positivi e Conteggio Negativi
- **Consegna:** Dato un array di dimensione $N$:
  1. Calcolare la somma di tutti gli elementi strettamente positivi ($>0$) e salvarla in `SommaPositivi`.
  2. Contare quanti sono gli elementi strettamente negativi ($<0$) e salvare il conteggio in `ContaNegativi`.
- **Logica:**
  - Scansione iterativa del vettore con `lw`.
  - Verifica del segno tramite pseudo-istruzioni `bgtz` (Branch if Greater Than Zero) e `bltz` (Branch if Less Than Zero), escludendo naturalmente lo zero da entrambi i rami.

### 🔹 [AE-6.s](file:///Users/romolodeffereria/Desktop/Architettura/Esercizi/AE-6.s) — Modifica In-Place con Soglia
- **Consegna:** Dato un vettore e un valore di soglia `Soglia`:
  - Se `vector[i] < Soglia` $\rightarrow$ sostituire con `0`.
  - Se `vector[i] >= Soglia` $\rightarrow$ raddoppiare il suo valore (`vector[i] = vector[i] * 2`).
- **Logica:**
  - Confronto dell'elemento con `blt t1, t2, Minore`.
  - Se minore: `sw zero, 0(s1)`.
  - Se maggiore o uguale: raddoppio con `add t1, t1, t1` e riscrittura con `sw t1, 0(s1)`.

### 🔹 [AE-7.s](file:///Users/romolodeffereria/Desktop/Architettura/Esercizi/AE-7.s) — Somma di due Vettori ($C = A + B$)
- **Consegna:** Eseguire elemento per elemento la somma $C[i] = A[i] + B[i]$ per $i = 0 \dots N-1$.
- **Logica:**
  - Mantiene tre puntatori contemporanei (`s1` per A, `s2` per B, `s3` per C).
  - A ogni iterazione: `lw` da A e B, `add`, `sw` in C.
  - Incremento parallelo di tutti e tre i puntatori di 4 byte (`addi s1, s1, 4`, etc.).

### 🔹 [AE-8.s](file:///Users/romolodeffereria/Desktop/Architettura/Esercizi/AE-8.s) — Conteggio Caratteri in Stringa
- **Consegna:** Data una stringa ASCII terminata dal byte nullo `\0` e un carattere bersaglio, contare quante volte compare.
- **Logica:**
  - Carica byte per byte con `lb t1, 0(s0)`.
  - Condizione di arresto del ciclo con `beqz t1, FineStringa`.
  - Confronta con il carattere cercato: se uguale (`beq`), incrementa il contatore `conteggio`.
  - Avanzamento del puntatore di 1 byte (`addi s0, s0, 1`).

### 🔹 [AE-9.s](file:///Users/romolodeffereria/Desktop/Architettura/Esercizi/AE-9.s) — Sostituzione Caratteri in Stringa
- **Consegna:** Sostituire in memoria ogni carattere spazio `' '` (`ASCII 32` / `0x20`) con il carattere underscore `'_'` (`ASCII 95` / `0x5F`).
- **Logica:**
  - Scansione con `lb`.
  - Se il byte letto è uguale allo spazio, scrive il nuovo byte nella medesima cella con `sb t3, 0(s0)`.
  - Avanzamento e arresto al terminatore `\0`.

### 🔹 [AE-10.s](file:///Users/romolodeffereria/Desktop/Architettura/Esercizi/AE-10.s) — Trasformazione in Maiuscolo (toUpper)
- **Consegna:** Trasformare tutte le lettere minuscole `'a'` - `'z'` nelle corrispondenti lettere MAIUSCOLE `'A'` - `'Z'`, lasciando invariati spazi, cifre e simboli.
- **Logica:**
  - Filtro sul codice ASCII del byte:
    - Se $byte < 97$ (`'a'`) $\rightarrow$ salta la modifica.
    - Se $byte > 122$ (`'z'`) $\rightarrow$ salta la modifica.
  - Se compreso nell'intervallo $[97, 122]$, converte in maiuscolo sottraendo 32: `addi t1, t1, -32`.
  - Riscrive il carattere modificato in memoria con `sb t1, 0(s0)`.

---

## 🚀 Come Eseguire i Programmi

Puoi aprire ed eseguire qualsiasi file `.s` utilizzando il simulatore **RARS**:

1. Avvia RARS in modalità grafica:
   ```bash
   java -jar ../Sbarramento/A_Conversione_Basi/Sbarramento11/rars1_6.jar &
   ```
2. Apri il file desiderato (`File -> Open -> AE-x.s`).
3. Clicca su **Assemble** (tasto con la chiave inglese/attrezzi o `F3`).
4. Esegui passo per passo (**Step**, `F7`) osservando il valore dei registri e la memoria, oppure esegui tutto (**Run**, `F5`).
