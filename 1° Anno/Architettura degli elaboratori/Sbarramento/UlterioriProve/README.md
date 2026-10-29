# 📚 Ulteriori Prove di Laboratorio

Questa cartella raccoglie un vasto archivio di **38 esercizi di laboratorio supplementari** organizzati per categoria tematica.

È la risorsa perfetta per consolidare la preparazione in vista dello sbarramento, offrendo decine di varianti su tracce d'esame reali.

---

## 🗂️ Suddivisione delle Categorie

```
UlterioriProve/
├── 📁 Categoria_A_Conversione/    # 12 Esercizi sulle conversioni tra basi numeriche
├── 📁 Categoria_B_Stringhe/       # 14 Esercizi sull'analisi e manipolazione di stringhe
└── 📁 Categoria_C_Aritmetica/     # 12 Esercizi sull'aritmetica e calcoli sequenziali
```

---

## 🔹 Categoria A — Conversione Basi (12 Esercizi)
Esercizi dal numero `Esercizio_1` a `Esercizio_12`.
- **Argomenti trattati:**
  - Conversioni da Binario a Ottale con/senza separatori e con diverse politiche di scarto o padding.
  - Conversioni da Binario a Base 4 e Base 16.
  - Conversioni da Esadecimale a Decimale e Binario.
  - Parsing di formati numerici composti e applicazione di maschere logiche di bit (`and`, `or`, `slli`, `srli`).

---

## 🔹 Categoria B — Stringhe e Caratteri (14 Esercizi)
Esercizi dal numero `Esercizio_1` a `Esercizio_14`.
- **Argomenti trattati:**
  - Scansione e conteggio di specifici caratteri e terminatori.
  - Rilevamento di pattern ripetuti e coppie consecutive.
  - Analisi di parità e divisibilità su cifre numeriche.
  - Filtri su caratteri speciali e calcolo di somme progressive di cifre.

---

## 🔹 Categoria C — Aritmetica e Sequenze (12 Esercizi)
Esercizi dal numero `Esercizio_1` a `Esercizio_12`.
- **Argomenti trattati:**
  - Valutazione di espressioni aritmetiche binarie e decimali con operatori sequenziali (`+`, `-`).
  - Gestione del segno e numeri in complemento a due.
  - Calcoli di medie, conteggio positivi/negativi e somme parziali.

---

## 🛠️ Come Esercitarsi su Ciascuna Cartella

In ogni cartella di esercizio (`Esercizio_X/`) troverai:
- **`README.pdf`**: Il testo e i vincoli dell'esercizio.
- **`program01.asm`**: Il file sorgente da completare con la propria soluzione.

Per testare la soluzione, puoi copiare i file `run.sh`, `Makefile` e `rars1_6.jar` da una delle cartelle della directory genitore di sbarramento (es. `Sbarramento11/`) oppure aprire ed eseguire direttamente il codice tramite l'interfaccia grafica del simulatore RARS:
```bash
java -jar ../A_Conversione_Basi/Sbarramento11/rars1_6.jar &
```
