# Esercitazione preparatoria - Simulazione dello scorso anno (canale M-Z)

Questa prova di simulazione dello scorso anno serve a familiarizzare con la struttura della prova, con l'implementazione delle funzioni in Python e con la correzione automatica.

## 1. Preparazione

Scaricate lo ZIP da Classroom ed estraetelo in una cartella. La struttura deve essere:

```text
Simulazione01/
  program.py
  grade.py
  testlib.py
  README.md
```

- **program.py**: contiene le consegne e le sei funzioni da completare. **E' l'unico file da modificare.**
- **grade.py**: esegue i test automatici e calcola il punteggio.
- **testlib.py**: contiene le funzioni di supporto necessarie al correttore.
- **README.md**: queste istruzioni.

Non rinominate i file e non modificate `grade.py` o `testlib.py`.

## 2. Aprire i file nell'ambiente Python preferito

Potete usare **VS Code, PyCharm, Spyder o un altro ambiente di sviluppo Python**.

1. Aprite la cartella estratta oppure il file `program.py` nel vostro ambiente di sviluppo. 
2. All'inizio di `program.py`, sostituite i segnaposto `NOME`, `COGNOME` e `MATRICOLA` con i vostri dati.
3. Scrivete e salvate le soluzioni **sempre in `program.py`**, lasciandolo nella stessa cartella di `grade.py` e `testlib.py`.

Se usate VS Code potete aprire la cartella con **File > Open Folder**. In PyCharm potete aprire la cartella come progetto; in Spyder potete aprire `program.py` nell'editor. 

## 3. Scrivere le soluzioni

Leggete la consegna di ogni esercizio e implementate il corpo della funzione corrispondente al posto di `pass`.

Per esempio, una definizione come:

```python
def func1(a_dict: dict[str, list[str]], word: str) -> int:
    pass
```

contiene annotazioni di tipo: `a_dict` e' un dizionario con chiavi stringa e valori costituiti da liste di stringhe, `word` e' una stringa e `-> int` indica che il risultato atteso e' un intero. Le annotazioni non richiedono modifiche.

Potete affrontare gli esercizi nell'ordine che preferite. Salvate `program.py` dopo ogni modifica.

## 4. Eseguire i test automatici

Aprite un **terminale nella cartella `Simulazione01`** (per esempio il terminale integrato del vostro ambiente di sviluppo oppure il terminale del sistema operativo). Assicuratevi che la directory di lavoro sia quella in cui si trovano `program.py`, `grade.py` e `testlib.py`.

Eseguite:

```bash
python3 grade.py
```

Se il comando Python del vostro ambiente e' `python`, utilizzate invece:

```bash
python grade.py
```

Il correttore importa `program.py`, esegue **quattro test per ciascuna delle sei funzioni** (24 test complessivi) e confronta i risultati ottenuti con quelli attesi. 

I test non si limitano agli esempi riportati nelle consegne, ma verificano il comportamento delle funzioni anche con altri input, inclusi eventuali casi particolari o casi limite (ad esempio, liste o dizionari vuoti, elementi ripetuti o valori estremi, a seconda dell'esercizio).

L'obiettivo è scrivere una soluzione generale, che rispetti tutti i requisiti della consegna, e non una soluzione che funzioni soltanto con gli esempi forniti.

**Potete eseguire `grade.py` tutte le volte che volete**, anche quando avete completato una sola funzione. E' consigliabile eseguirlo dopo ogni funzione completata e dopo ogni correzione. Ogni volta, salvate prima `program.py`.

Potete anche avviare `grade.py` dal vostro ambiente di sviluppo, purche' la directory di lavoro sia quella della simulazione.

N.B. Non e' necessario avviare i test singolarmente e non dovete eseguire direttamente `testlib.py`.

## 5. Leggere i risultati

Nel terminale compariranno messaggi simili a questi:

```text
Running test_func1_1
[OK]: 1 point(s)

Running test_func1_2
error: 0 points

...
Total score: 6.0
```

- **[OK]**: il test e' stato superato e assegna i punti indicati.
- **error / 0 points**: il test non e' stato superato oppure si e' verificata un'eccezione.
- **Not implemented**: in alcuni test il risultato `None` segnala che la funzione non e' ancora implementata.
- **Total score**: somma dei punti ottenuti nei test.

Il punteggio massimo degli esercizi e' **30 punti**; nelle istruzioni della simulazione la soglia indicata e' **18 punti**. Ogni esercizio ha piu' test e puo' quindi assegnare punti parziali.

Il correttore genera inoltre `grade.csv`, contenente il punteggio dei singoli test. Non dovete modificarlo.

## 6. Correggere gli errori

Se un test non viene superato, rileggete la consegna e controllate che:

- la funzione restituisca il risultato e il tipo di dato richiesti;
- gli ordinamenti e le condizioni siano corretti;
- siano considerati anche i casi particolari;
- liste e dizionari siano modificati soltanto quando richiesto.

Potete inserire temporaneamente istruzioni `print()` **nel vostro `program.py`** per osservare i valori delle variabili. Poi correggete il codice, salvate il file ed eseguite nuovamente `grade.py`.

**Non modificate i test per farli risultare corretti.** Il vostro lavoro va svolto soltanto in `program.py`.

## 7. Consigli

Prima di scrivere codice, individuate input, output e passaggi necessari. Risolvete un sottoproblema alla volta e controllate il comportamento con esempi diversi.

Superare i test forniti e' utile per verificare la soluzione, ma non garantisce che funzioni con tutti i possibili input.

Buon lavoro!
