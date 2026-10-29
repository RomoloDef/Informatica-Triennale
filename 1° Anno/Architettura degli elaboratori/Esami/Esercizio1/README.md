# 🗄️ Esercizio 1: Gerarchia di Memoria, Cache L1/L2 e Paginazione

Questa cartella raccoglie le tracce e i testi d'esame in formato immagine relativi al **primo esercizio** della prova scritta di Architettura degli Elaboratori.

---

## 📌 Contenuto della Cartella

La cartella contiene le immagini ad alta risoluzione dei testi dei vari appelli:
- [Esercizio 1-1.png](file:///Users/romolodeffereria/Desktop/Architettura/Esami/Esercizio1/Esercizio%201-1.png): Traccia Appello 1
- [Esercizio 1-2.png](file:///Users/romolodeffereria/Desktop/Architettura/Esami/Esercizio1/Esercizio%201-2.png): Traccia Appello 2
- [Esercizio 1-3.png](file:///Users/romolodeffereria/Desktop/Architettura/Esami/Esercizio1/Esercizio%201-3.png): Traccia Appello 3
- [Esercizio 1-4.png](file:///Users/romolodeffereria/Desktop/Architettura/Esami/Esercizio1/Esercizio%201-4.png): Traccia Appello 4
- [Esercizio 1-5.png](file:///Users/romolodeffereria/Desktop/Architettura/Esami/Esercizio1/Esercizio%201-5.png): Traccia Appello 5
- [Esercizio 1-6.png](file:///Users/romolodeffereria/Desktop/Architettura/Esami/Esercizio1/Esercizio%201-6.png): Traccia Appello 6

---

## 📐 Schema Tipico della Prova e Formule Fondamentali

L'esercizio richiede di tracciare la tabella di esecuzione per una sequenza di accessi a memoria (indirizzi a 32 bit):

### 1. Scomposizione dell'Indirizzo
- $\text{Dimensione Blocco (byte)} = \text{Num Parole} \times 4$
- $\text{Block} = \lfloor \text{Indirizzo} / \text{Dimensione Blocco} \rfloor$
- $\text{Index} = \text{Block} \pmod{\text{Num Set}}$
- $\text{Tag} = \lfloor \text{Block} / \text{Num Set} \rfloor$

### 2. Tabella di Stato della Cache
Per ogni indirizzo fornito dalla sequenza:
- Verifica se il $\text{Tag}$ è già presente nel set indicato da $\text{Index}$ con bit di validità a 1 $\rightarrow$ **HIT**.
- Se non è presente $\rightarrow$ **MISS**. In caso di set pieno, applicare la politica di sostituzione **LRU** (Least Recently Used).
- Determinare la tipologia di miss:
  - **Compulsory (Cold Miss):** Il blocco di memoria non era mai stato caricato prima.
  - **Capacity Miss:** Si verifica se l'intera cache è satura (tutti i set e tutte le vie sono occupati).
  - **Conflict Miss:** Il set specifico è pieno ma esistono altri set con vie libere nella cache.

### 3. Prestazioni e Memoria Virtuale
- **AMAT (Average Memory Access Time):**
  $$\text{AMAT} = \text{Hit Time} + (\text{Miss Rate} \times \text{Miss Penalty})$$
- **Numero di Istruzioni Eseguite:**
  $$\text{Num Istruzioni} = \text{Tempo Medio} \times \frac{\text{Frequenza}}{\text{CPI}}$$
- **Offset e Memoria Virtuale:**
  - $\text{Offset} = \text{Indirizzo} \pmod{\text{Dimensione Blocco}}$
  - $\text{Word Offset} = \lfloor \text{Offset} / 4 \rfloor$
  - $\text{Numero Pagina Virtuale} = \lfloor \text{Indirizzo} / \text{Dimensione Pagina} \rfloor$

---

## 📖 Guida Consigliata
Per una spiegazione passo per passo ed esempi guidati, fare riferimento a:  
👉 **[GuidaEsercizio1.pdf](file:///Users/romolodeffereria/Desktop/Architettura/Esami/GuidaEsercizio1.pdf)**
