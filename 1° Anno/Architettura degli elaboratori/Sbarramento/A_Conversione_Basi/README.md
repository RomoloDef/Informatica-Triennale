# 🔵 Categoria A — Conversione tra Basi Numeriche

Questa cartella raccoglie tutte le prove d'esame appartenenti alla categoria più frequente e decisiva dello sbarramento: **la conversione tra basi numeriche** (**47% dei temi d'esame analizzati**).

Padroneggiare queste prove è prerequisito essenziale per superare la prova di laboratorio.

---

## 📂 Esercizi Contenuti in Questa Cartella

| Esercizio | Data Esame | Consegna Sintetica | Difficoltà | Cartella |
|---|---|---|:---:|---|
| **Sbarramento 8** | 09/05/2025 | Binario $\rightarrow$ **Ottale** (gruppi di 3 bit), separatore `/`, scartare bit extra in coda | ⭐⭐ | [Sbarramento8](file:///Users/romolodeffereria/Desktop/Architettura/Sbarramento/A_Conversione_Basi/Sbarramento8) |
| **Sbarramento 9** | 09/05/2025 | Binario $\rightarrow$ **Base 4** (gruppi di 2 bit), separatore `/`, scartare bit extra | ⭐⭐ | [Sbarramento9](file:///Users/romolodeffereria/Desktop/Architettura/Sbarramento/A_Conversione_Basi/Sbarramento9) |
| **Sbarramento 5** | 24/01/2023 | Binario $\rightarrow$ **Ottale** (senza separatore), scartare bit residui, output su 3 righe + funzione `codificaOttale` | ⭐⭐⭐ | [Sbarramento5](file:///Users/romolodeffereria/Desktop/Architettura/Sbarramento/A_Conversione_Basi/Sbarramento5) |
| **Sbarramento 7** | 30/01/2023 | Binario $\rightarrow$ **Ottale** (senza separatore), padding bit mancanti con 0, output su 3 righe + funzione `codificaOttale` | ⭐⭐⭐ | [Sbarramento7](file:///Users/romolodeffereria/Desktop/Architettura/Sbarramento/A_Conversione_Basi/Sbarramento7) |
| **Sbarramento 11** | 11/09/2025 | **Esadecimale** $\rightarrow$ Decimale, separatore `/`, solo numeri terminati da `/` | ⭐⭐⭐ | [Sbarramento11](file:///Users/romolodeffereria/Desktop/Architettura/Sbarramento/A_Conversione_Basi/Sbarramento11) |
| **Sbarramento 12** | 29/10/2025 | **Esadecimale** $\rightarrow$ Binario e stampa bit singoli (reverse dei bit hex) | ⭐⭐⭐ | [Sbarramento12](file:///Users/romolodeffereria/Desktop/Architettura/Sbarramento/A_Conversione_Basi/Sbarramento12) |
| **Sbarramento 14** | 18/02/2026 | **Esadecimale** $\rightarrow$ Stampa hex + seleziona bit per posizione (maschera di bit) | ⭐⭐⭐⭐ | [Sbarramento14](file:///Users/romolodeffereria/Desktop/Architettura/Sbarramento/A_Conversione_Basi/Sbarramento14) |

---

## 🧠 Pattern e Concetti Algoritmici Fondamentali

### 1. Binario $\rightarrow$ Ottale (Gruppi di 3 bit)
Ogni cifra ottale $[0 \dots 7]$ è formata da 3 bit binari.  
- Accumulo tramite shift a sinistra:
  ```asm
  addi t1, t1, -48    # Da char ASCII '0'/'1' a intero 0/1
  slli t2, t2, 1      # Moltiplica accumulatore parziale per 2
  or   t2, t2, t1     # Inserisci il bit corrente
  ```
- Quando il contatore bit raggiunge 3:
  - Converti il valore in carattere ASCII: `addi t2, t2, 48`.
  - Salva nel buffer di output con `sb` e azzera accumulatore e contatore.

### 2. Gestione Bit Residui: Scarto vs Padding
- **Scarto (es. Sbarramento 8 e 5):** Se alla fine della sequenza o al separatore `/` rimangono 1 o 2 bit, non formano una cifra completa e vengono ignorati.
- **Padding con Zeri (es. Sbarramento 7):** Se rimangono bit non allineati, si shiftano a sinistra aggiungendo zeri fino a completare i 3 bit (es. `01` diventa `010` = 2).

### 3. Parsing Esadecimale (Cifre '0'-'9' e 'A'-'F')
Per convertire un carattere esadecimale in valore numerico:
```asm
lb t1, 0(t0)
li t3, 58           # Codice ASCII successivo al '9'
blt t1, t3, cifra
# È una lettera 'A'-'F' (ASCII 65-70)
addi t1, t1, -55    # 'A' (65) - 55 = 10
j accumula
cifra:
addi t1, t1, -48    # '0' (48) - 48 = 0
accumula:
slli t2, t2, 4      # Accumulatore *= 16
add  t2, t2, t1     # Aggiunge cifra esadecimale
```

---

## 🏃 Esecuzione dei Test
In qualsiasi cartella di sbarramento:
```bash
./run.sh program01.asm
```
