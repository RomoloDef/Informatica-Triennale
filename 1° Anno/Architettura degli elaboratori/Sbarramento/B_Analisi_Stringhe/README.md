# 🟢 Categoria B — Analisi e Conteggio su Stringhe

Questa cartella raccoglie le prove d'esame incentrate sulla scansione, filtraggio e conteggio statistico di cifre o caratteri all'interno di stringhe (**33% dei temi d'esame analizzati**).

---

## 📂 Esercizi Contenuti in Questa Cartella

| Esercizio | Data Esame | Consegna Sintetica | Difficoltà | Cartella |
|---|---|---|:---:|---|
| **Sbarramento 3** | 10/06/2022 | Contare occorrenze di `0` e di `1` in stringa binaria + funzione `contaOccorrenze` | ⭐ | [Sbarramento3](file:///Users/romolodeffereria/Desktop/Architettura/Sbarramento/B_Analisi_Stringhe/Sbarramento3) |
| **Sbarramento 4** | 22/09/2022 | Contare coppie consecutive identiche + somma cifre + funzione `contaOccorrenze` | ⭐⭐ | [Sbarramento4](file:///Users/romolodeffereria/Desktop/Architettura/Sbarramento/B_Analisi_Stringhe/Sbarramento4) |
| **Sbarramento 6** | 03/11/2022 | Somma valori presi a due a due (coppie decimali) + conteggio totale cifre | ⭐⭐ | [Sbarramento6](file:///Users/romolodeffereria/Desktop/Architettura/Sbarramento/B_Analisi_Stringhe/Sbarramento6) |
| **Sbarramento 1** | 12/02/2025 | Contare occorrenze pari/dispari (solo cifre 3-8), ignorare primo carattere e gestire `?` | ⭐⭐⭐ | [Sbarramento1](file:///Users/romolodeffereria/Desktop/Architettura/Sbarramento/B_Analisi_Stringhe/Sbarramento1) |
| **Sbarramento 13** | 20/01/2026 | Prendere cifre a coppie come numero decimale, ignorare se contiene `9`, contare divisibili per 4 | ⭐⭐⭐ | [Sbarramento13](file:///Users/romolodeffereria/Desktop/Architettura/Sbarramento/B_Analisi_Stringhe/Sbarramento13) |

---

## 🧠 Pattern e Concetti Algoritmici Fondamentali

### 1. Scansione Carattere per Carattere
```asm
loop_str:
    lb   t1, 0(t0)          # Carica byte corrente
    beqz t1, fine_str       # Arresto al terminatore nullo \0
    li   t2, 10             # Newline '\n'
    beq  t1, t2, fine_str   # Arresto all'eventuale newline
    addi t1, t1, -48        # Converte da ASCII a intero numerico
    # ... logica di elaborazione ...
    addi t0, t0, 1          # Avanza al carattere successivo
    j    loop_str
fine_str:
```

### 2. Confronto tra Carattere Corrente e Precedente (Coppie Identiche)
- Memorizzare il carattere dell'iterazione precedente in un registro dedicato (es. `t3`).
- Al primo carattere inizializzare `t3` con un valore sentinella non valido (es. `-1`).
- Per i caratteri successivi: `beq t1, t3, coppia_trovata`.

### 3. Raggruppamento Cifre a Coppie Decimali
Per formare numeri a due cifre $N = \text{cifra}_1 \times 10 + \text{cifra}_2$:
```asm
# t4 = registro accumulatore del numero a due cifre
# t5 = flag alternanza (0: decina, 1: unità)
beqz t5, decine
# È la seconda cifra (unità)
add  t4, t4, t1             # Somma le unità
li   t5, 0                  # Reimposta flag per la coppia successiva
j    elabora_coppia
decine:
li   t6, 10
mul  t4, t1, t6             # Moltiplica per 10 la prima cifra
li   t5, 1                  # Prossimo carattere sarà unità
```

### 4. Verifica Parità e Divisibilità
- **Controllo di parità:** `andi t2, t1, 1` (se 0 il numero è pari, se 1 è dispari).
- **Divisibilità per 4:** `andi t2, t1, 3` (se 0 il numero è divisibile per 4, equivalente a $N \pmod 4 == 0$).

---

## 🏃 Esecuzione dei Test
In qualsiasi cartella di sbarramento:
```bash
./run.sh program01.asm
```
