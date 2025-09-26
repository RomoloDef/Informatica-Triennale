import os

'''Ex1: 6 + 3 punti
Implementare la funzione ex2(dirin, words), ricorsiva o che utilizza funzioni 
o metodi ricorsivi, avendo come argomento:
    - dirin: il percorso di una directory esistente come stringa
    - words: una lista di parole

La funzione esaminerà dirin e tutte le sue sottocartelle (a qualsiasi
livello), e conterà le occorrenze delle parole di 'words' in tutti i
file di testo (cioè i file con estensione .txt) presenti in qualsiasi
cartella.  Le parole presenti in un file sono separate da uno o piu dei
seguenti caratteri: spazio, tabulazione o carattere newline.

(6 punti) La funzione restituisce una lista di tuple (parola, occ), in cui:
    - il primo valore di ogni coppia è una delle parola nella lista di input.
    - il secondo valore 'occ' della coppia è il numero di occorrenze
      di quella parola nei file di testo.

(+ 3 punti) La lista è ordinata in base al numero di occorrenze delle
parole (in ordine decrescente). Se due o più parole hanno lo
stesso numero di occorrenze, sono ordinate alfabeticamente (in
ordine crescente). Se una parola dell'elenco di input non si trova mai
nei file testuali, deve comunque essere restituita dalla funzione con
conteggio 0.

AVVISO 1: Si consiglia di utilizzare le funzioni os.listdir,
os.path.isfile e os.path.isdir e NON la funzione os.join in
Windows. Utilizzare la concatenazione tra stringhe con il carattere '/'.

AVVISO 2: è vietato utilizzare la funzione os.walk

Ad esempio, data la cartella "ex2/" e se words = ["gatto", "cane"]
la funzione restituisce: [("cane", 11), ("gatto", 6)].
'''


def ex1(dirin, words):
            
    pass

# %% --------------------------------------------------------------------#

"""
Ex2: 6 punti

Si scriva una funzione ricorsiva ex2(directory), o che al suo interno
usi una funzione ricorsiva, che prende in ingresso una stringa
'directory' che rappresenta il percorso ad una directory.
La funzione deve explorare ricorsivamente l'albero delle directory con
radice in 'directory' e restituire un dizionario.
Le chiavi del dizionario sono i percorsi delle sotto-directory di
'directory', sottoforma di stringa.
Il valore della chiave di una directory è un set di stringhe con i nomi
di quei file '.txt' presenti in 'directory' per i quali il primo carattere
del contenuto del file è uguale all'ultimo.
Se una directory non contiene nessun file .txt con tale caratteristica,
allora quella directory non appare nel dizionario.

Esempio: se la funzione è chiamata su 'ex2/A', ritorna:

{'ex2/A/B': {'b.txt'}, 'ex2/A/C': {'c.txt'}}

poiché ex2/A/B/b.txt e ex2/A/C/c.txt sono gli unici file in cui
il primo carattere del contenuto è uguale all'ultimo ('k' per il primo,
'a' per il secondo).

NOTA: è proibito usare la funzione os.walk. Si possono usare:
  os.listdir, os.path.isfile, os.path.exists, etc.  Per concatenare i
  path, si usi l'operazione di concatenazione con il carattere '/'

NOTA: consigliamo fortemente di dividere l'esercizio in sottoproblemi
  dividendo in funzioni per ogni sottoproblema.
"""

def ex2(root):
    risultato = {}
    for nome in os.listdir(root):
        if nome[0] in '._': continue
        fullname = root + '/' + nome
        if os.path.isdir(fullname):
            trovato = ex2(fullname)
            risultato.update(trovato)
        elif nome.endswith(".txt"):
            with open(fullname, mode = "r", encoding = "utf8") as F:
                testo = F.read()
                primo = testo[0]
                ultimo = testo[-1]
                if primo == ultimo:
                    risultato[fullname] = {nome}
    return risultato
    pass

# print(ex2('ex2/A'))

# %% --------------------------------------------------------------------#

"""
Ex3: 6 punti

Si scriva una funzione ricorsiva ex3(directory), o che al suo interno
usi una funzione ricorsiva, che prende in ingresso una stringa
'directory' che rappresenta il percorso ad una directory.  La funzione
deve esplorare ricorsivamente l'albero delle directory con radice in
'directory' e restituire una lista di tuple di due elementi.  Ciascuna
tupla contiene:
    - in prima posizione il percorso ad un file testuale il
      cui filename finisce per .txt;
    - in seconda posizione la lunghezza L della riga più lunga del
      suddetto file txt, escludendo il carattere di newline.
La lista è ordinata in maniera crescente in base ad L e, a partità di
lunghezza, in ordine alfabetico in base al percorso del file.

Se la funzione è chiamata su 'ex3/A', restituisce:

[('ex3/A/QBwXM/KVobU.txt', 19)]

infatti il file 'ex1/A/QBwXM/KVobU.txt' ha la riga di massima lunghezza
di 19 caratteri (escluso lo '\n' ed inclusi gli spazi).

NOTA: è proibito usare la funzione os.walk. Si possono usare:
  os.listdir, os.path.isfile, os.path.exists, etc.  Per concatenare i
  path, si usi l'operazione di concatenazione con il carattere '/'

NOTA: consigliamo fortemente di dividere l'esercizio in sottoproblemi
  dividendo in funzioni per ogni sottoproblema.
"""

def ex3(directory):
    risultato = []
    for nome in os.listdir(directory):
        if nome[0] in '._': 
            continue
        fullname = directory + '/' + nome 
        if os.path.isdir(fullname):
            risultato.extend(ex3(fullname))
        elif nome.endswith(".txt"):
            with open(fullname, mode="r", encoding="utf8") as F:
                righe = F.readlines()
                if righe:
                    massimo = max(len(riga.rstrip('\n')) for riga in righe)
                else:
                    massimo = 0
                risultato.append((fullname, massimo))
    ordinamento = lambda x: (x[1], x[0])
    return sorted(risultato, key=ordinamento)

# print(ex3('ex3/A'))

# %% --------------------------------------------------------------------#

'''
Ex4: 6 punti
Si definisca la funzione ex4(dirin, extensions), ricorsiva o che usa funzioni o metodi ricorsivi,
che riceve come argomenti:
  - dirin: il path di una directory
  - extensions: una lista di estensioni di file (stringhe)

La funzione esplora dirin e tutte le sue sottodirectory (a tutti i
livelli) e cerca tutti i file con una delle estensioni indicate.
La funzione ritorna un dizionario che ha come chiavi i path delle directory
e sottodirectory esplorate (con il separatore '/' che vale sia in Windows che Linux)
e come valori una coppia (min, max) in cui min e max sono le dimensioni
dei file con una di quelle estensioni più piccolo e più grande rispettivamente
presenti in quella directory.
Le directory che non contengono nessun file con le estensioni indicate non appaiono nel dizionario.

NOTA 1: potete usare le funzioni: os.listdir, os.path.isfile, os.path.isdir, os.path.getsize ...
NOTA 2: è proibito usare la funzione os.walk
NOTA 3: usate il carattere '/' come separatore dei path
(che funzione sia in Windows che su MacOS o Linux)

Esempio:
se il path dirin è "ex4/A" e le extensions = ["txt", "pdf", "png", "gif"]
la funzione ritorna: 
{'ex4/A': [29, 56], 'ex4/A/C': [29, 92], 'ex2/A/B': [25, 28]}
'''

def ex4(dirin, extensions):
    risultato = {}
    dimensioni = []
    for nome in os.listdir(dirin):
        if nome in '._': continue 
        fullname = dirin + '/' + nome
        if os.path.isdir(fullname):
            trovati = ex4(fullname, extensions)
            risultato.update(trovati)
        elif os.path.isfile(fullname) and (nome.endswith('.' + estensione) for estensione in extensions):
            dimensioni.append(os.path.getsize(fullname))
            
    if dimensioni:
        risultato[dirin] = [min(dimensioni), max(dimensioni)]
    return risultato
    pass

# print(ex4("ex4/A", ["txt", "pdf", "png", "gif"]))

# %% --------------------------------------------------------------------#

'''
Ex5: 6 punti

Si definisca una funzione ex5(target_folder), ricorsiva o che utilizzi almeno una
funzione ricorsiva, che prenda in input il percorso di una cartella di destinazione.
La funzione scandisce in modo ricorsivo la cartella target_folder e tutte
le sue sottocartelle, restituendo una lista di coppie (percorso, conteggio), in cui:
- il percorso è il percorso completo di una delle sottocartelle della cartella target_folder
(nidificate a qualsiasi livello >= 0 all'interno della cartella di destinazione;
la cartella di destinazione può essere considerata una sottocartella di se stessa,
per cui il livello=0);
- il conteggio è il numero di file di testo contenuti nella sottocartella
(i file di testo sono file il cui nome termina con ".txt").

La lista restituita è ordinata in base al valore del contatore dei file, in ordine decrescente;
se due o più cartelle contengono lo stesso numero di file, vengono ordinate in ordine alfabetico.

Le uniche due funzioni che possono essere importate nella soluzione sono: os.listdir e os.path.isdir.

Ad esempio, se la struttura della cartella è la seguente:

A
|-B
| |-C
| | |-c1.txt
| | |-c2.txt
| |
| |-b1.txt
| |-b2.txt
| |-b3.txt
|
|-D
| |-d1.txt
| |-d2.txt
|
|-E
| |-e1.txt
|
|-a1.txt
|-a2.txt
|-a3.txt

La funzione restituisce la lista:

[("A", 3), ("A/B", 3), ("A/B/C", 2), ("A/D", 2), ("A/E", 1)]

'''

def ex5(target_folder):
    risultato = []
    conteggio = 0
    for nome in os.listdir(target_folder):
        if nome in '._': continue
        fullname = target_folder + '/' + nome
        if os.path.isdir(fullname):
            risultato.extend(ex5(fullname))
        elif nome.endswith(".txt"):
            conteggio += 1
    risultato.append((target_folder, conteggio))
    return risultato
            
    pass

# print(ex5("ex5/A"))

# %% --------------------------------------------------------------------#

"""
Ex6: 6 punti
Si scriva una funzione ricorsiva ex1(root), o che al suo interno usi
una funzione ricorsiva, che prende in ingresso una stringa che punta ad una
directory e ricorsivamente esplori l'albero delle directory e restituisca un
dizionario. La chiave del dizionario e' il percorso assoluto a partire
dalla 'root', sottoforma di stringa.  Il valore corrisponde ad una
stringa così fatta: considerando una directory trovata, si prendano
soltanto i file in QUELLA directory con estensione ".txt", ordinati
in maniera alfabetica.  I file .txt sono file testuali dove su ogni
riga vi e' una serie di numeri interi seguiti solo da uno spazio. A
esempio 'ex1_A/XYCwdkCokL.txt' contiene:

75 84 84 73 83
76 74 76

Si legga sequenzialmente all'alto al basso, da sinistra a destra,
ciascun numero, lo si interpreti come valore Unicode, convertendolo
in un carattere e lo si concateni con il carattere successivo.

Ad esempio la sequenza suddetta e' convertita nella stringa "KTTISLJL".

Il valore nel dizionario e' la stringa che si ottiene
concatenando le stringhe generate per ogni file testuale per quella
directory, secondo l'ordine alfabetico dei file.txt.

Se la directory non contiene nessun file .txt allora quella directory
non appare nel dizionario.

Se la funzione e' chiamata su 'ex6_A', ritorna:

{'ex6_A/bkLbD': 'A\x9eŻĂĳŜǖ', 'ex6_A': 'KTTISLJL'}

NOTA: e' proibito usare la funzione os.walk. Si possono usare:
os.listdir, os.path.isfile, os.path.exists, etc.
Per concatenare i path, si usi l'operazione di concatenazione con il carattere '/'

NOTA: consigliamo fortemente di dividere l'esercizio in sottoproblemi
dividendo in funzioni per ogni sottoproblema.
"""

def ex6(root):
    risultato = {}
    for nome in os.listdir(root):
        if nome in '._': continue
        fullname = root + '/' + nome
        if os.path.isdir(fullname):
            trovato = ex6(fullname)
            risultato.update(trovato)
        elif nome.endswith('.txt'):
            with open(fullname, mode = "r", encoding = "utf8") as file:
                stringa = ''
                righe = file.readlines()
                for riga in righe:
                    numeri = riga.split()
                    for n in numeri:
                        stringa += chr(int(n))
    risultato[root] = stringa
    return risultato
        
    pass

print(ex6('ex6_A'))


# %% --------------------------------------------------------------------#

"""
Ex7: 6 punti

Si definisca la funzione ex7(dirin), ricorsiva o che utilizza funzioni 
o metodi ricorsivi, avendo come argomento una stringa che indica il
percorso di una directory esistente.

La funzione esaminerà dirin e tutte le sue sottocartelle (a qualsiasi
livello), e conterà il numero di caratteri numerici trovato nei
file con estensione '.txt' presenti in qualsiasi cartella.

La funzione restituisce una lista di stringhe rappresentanti i percorsi
relativi alla directory dirin dei file in cui sono stati trovati i
caratteri numerici.
La lista dei percorsi dei file è ordinata in ordine decrescente in base
al numero di caratteri numerici trovati nei vari file.
Se due o più file hanno lo stesso numero di caratteri numerici,
si deve usare l'ordine crescente della profondità del file all'interno
della directory dirin.
In caso di parità, si deve usare l'ordine alfabetico.
Un file '.txt' che non contiene caratteri numerici non viene inserito
nella lista ritornata.

AVVISO 1: Si consiglia di utilizzare le funzioni os.listdir,
os.path.isfile e os.path.isdir e NON la funzione os.join in
Windows. Utilizzare la concatenazione tra stringhe con il carattere '/'.

AVVISO 2: è vietato utilizzare la funzione os.walk

Ad esempio, la funzione ex7('ex7/A') deve restituire la lista
['ex7/A/B/3odd74B.txt', 'ex7/A/C/e3dd7Ag22.txt', 'ex7/A/3cmi4G3ev.txt',
   'ex7/A/gkfep28.txt', 'ex7/A/C/n3ks22.txt']
"""

def ex7(dirin):
    risultati = []

    # Esploro tutti i file e le sottodirectory
    for nome in os.listdir(dirin):
        if nome[0] in '._':  # ignora file speciali
            continue
        percorso = dirin + '/' + nome
    
        # Se è una directory, esploro ricorsivamente
        if os.path.isdir(percorso):
            risultati += ex7(percorso)
    
        # Se è un file .txt, conto i numeri
        elif nome.endswith('.txt') and os.path.isfile(percorso):
            conteggio_numeri = 0
            with open(percorso, "r", encoding="utf8") as f:
                for riga in f:
                    for c in riga:
                        if c.isdigit():
                            conteggio_numeri += 1
    
            if conteggio_numeri > 0:
                # calcolo la profondità relativa alla directory root
                profondità = percorso.count('/') - dirin.count('/')
                risultati.append((conteggio_numeri, profondità, percorso))
    
    # Solo alla chiamata principale ordino e restituisco solo i percorsi
    if dirin.count('/') == 0 or dirin == dirin.split('/')[0]:
        risultati.sort(key=lambda x: (-x[0], x[1], x[2]))  # ordina secondo i criteri
        risultati = [percorso for _, _, percorso in risultati]
    
    return risultati

print(ex7('ex7/A'))