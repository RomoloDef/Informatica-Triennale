# 🟣 Categoria D — Operazioni su Matrici

Questa cartella raccoglie le prove d'esame incentrate sulla manipolazione di matrici bidimensionali memorizzate linearmente in memoria (**7% dei temi d'esame analizzati**).

---

## 📂 Esercizi Contenuti in Questa Cartella

| Esercizio | Data Esame | Consegna Sintetica | Difficoltà | Cartella |
|---|---|---|:---:|---|
| **Sbarramento 2** | 14/02/2025 | Matrice $N \times N$: calcolare e stampare la somma dei primi 2 elementi di ogni riga | ⭐⭐⭐ | [Sbarramento2](file:///Users/romolodeffereria/Desktop/Architettura/Sbarramento/D_Matrici/Sbarramento2) |

---

## 🧠 Analisi e Dettagli di Sbarramento 2

### Consegna
Data una matrice quadrata di dimensione $N \times N$ di interi a 32 bit allocata linearmente in memoria:
- Calcolare la somma del primo e del secondo elemento di ciascuna riga.
- **Gestione dei Casi Particolari:**
  - Se $N = 0$: il programma deve restituire `0`.
  - Se $N = 1$: ogni riga ha un solo elemento, quindi si somma unicamente il primo elemento.
  - Se $N \ge 2$: si sommano esattamente i primi due elementi di ogni riga.

### Rappresentazione in Memoria e Parametri Ricevuti
A differenza degli esercizi sulle stringhe, l'input viene gestito direttamente dal template:
- `a0`: Indirizzo base della matrice in memoria.
- `a1`: Indirizzo in memoria in cui è salvata la dimensione $N$.

### Indirizzamento dell'Array Bidimensionale Linearizzato
In memoria, una matrice $N \times N$ è memorizzata per righe (*row-major order*). L'elemento alla riga $r$ e colonna $c$ ha offset:
$$\text{Offset}(r, c) = (r \times N + c) \times 4 \quad \text{byte}$$

- **Primo elemento della riga $r$ ($c=0$):**  
  $\text{Offset} = (r \times N) \times 4$
- **Secondo elemento della riga $r$ ($c=1$):**  
  $\text{Offset} = (r \times N + 1) \times 4$
- **Avanzamento alla riga successiva:**  
  Aggiungere $N \times 4$ byte all'indirizzo base della riga corrente (`slli t5, s1, 2; add t0, t0, t5`).

---

## 🏃 Esecuzione dei Test
Posizionandosi nella cartella [Sbarramento2](file:///Users/romolodeffereria/Desktop/Architettura/Sbarramento/D_Matrici/Sbarramento2):
```bash
./run.sh program01.asm
```
