# 🟡 Categoria C — Aritmetica Binaria con Operatori Inline

Questa cartella raccoglie le prove d'esame in cui l'input è rappresentato da una sequenza di numeri binari separati da operatori aritmetici inline (`+` o `-`), con l'obiettivo di calcolare il risultato numerico complessivo e stamparlo in formato decimale (**13% dei temi d'esame analizzati**).

---

## 📂 Esercizi Contenuti in Questa Cartella

| Esercizio | Data Esame | Consegna Sintetica | Difficoltà | Cartella |
|---|---|---|:---:|---|
| **Sbarramento 10** | 09/05/2025 | Numeri binari separati da `+`, sommare tutti i termini e stampare il risultato decimale | ⭐⭐ | [Sbarramento10](file:///Users/romolodeffereria/Desktop/Architettura/Sbarramento/C_Aritmetica_Binaria/Sbarramento10) |
| **Sbarramento 15** | 14/09/2026 | Numeri binari separati da `-`, sottrarre progressivamente e stampare il risultato decimale | ⭐⭐⭐ | [Sbarramento15](file:///Users/romolodeffereria/Desktop/Architettura/Sbarramento/C_Aritmetica_Binaria/Sbarramento15) |

---

## 🧠 Analisi dei Temi e Pattern Risolutivi

### 1. Sbarramento 10: Somma Binaria con `+`
- **Esempio di Input:** `11+0000+1+0010`
- **Spiegazione:** $3 + 0 + 1 + 2 = 6$
- **Output:** `6`
- **Algoritmo:**
  - Scansiona la stringa un carattere alla volta.
  - Se il carattere è un bit binario (`'0'` o `'1'`), shifta l'accumulatore del numero corrente a sinistra (`slli t2, t2, 1`) e somma il bit.
  - Se il carattere è il separatore `+` (ASCII `43` / `0x2B`) o il terminatore di stringa (`\n` o `\0`):
    - Aggiunge il valore dell'accumulatore parziale al totale generale (`add s0, s0, t2`).
    - Azzera l'accumulatore parziale (`li t2, 0`).
  - Al termine, stampa il totale decimale con syscall `a7=1`.

### 2. Sbarramento 15: Sottrazione Binaria con `-`
- **Esempio di Input:** `11-0000-1-0010`
- **Spiegazione:** $3 - 0 - 1 - 2 = 0$
- **Esempio con risultato negativo:** `1-1001-11-0011-000` $\rightarrow$ $1 - 9 - 3 - 3 - 0 = -14$
- **Attenzione alle insidie:**
  - Il **primo numero** è positivo e non è preceduto da alcun operatore: va sommato al totale.
  - Tutti i numeri successivi al primo devono essere **sottratti** (`sub s0, s0, t2`).
  - Mantenere un flag o un contatore per distinguere il primo termine dai successivi.
  - La syscall di stampa intero (`li a7, 1; ecall`) gestisce nativamente i numeri negativi in complemento a due, stampando il segno `-` automaticamente.

---

## 🏃 Esecuzione dei Test
In ciascuna sottocartella:
```bash
./run.sh program01.asm
```
