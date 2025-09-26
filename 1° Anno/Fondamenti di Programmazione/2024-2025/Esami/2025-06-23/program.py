#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
################################################################################
################################################################################

""" Operazioni da fare PRIMA DI TUTTO:
 1) Salvare il file come program.py
 2) Assegnare le variabili sottostanti con il tuo
    NOME, COGNOME, NUMERO DI MATRICOLA

Per superare l'esame è necessario:
    - risolvere almeno 3 esercizi di tipo func AND;
    - ottenere un punteggio maggiore o uguale a 18 (15 se DSA)

Il voto finale è la somma dei punteggi dei problemi risolti.

IMPORTANTE: impostare DEBUG = True in `grade.py` per aumentare il livello
di debug e conoscere dove un esercizio genera errore.
Ricordare che per testare e valutare la ricorsione è necessario
impostare DEBUG = False
"""
nome       = "Romolo"
cognome    = "Deffereria"
matricola  = "2114887"

#########################################

# %% ----------------------------------- FUNC1 ------------------------- #
''' func1: 2 punti
Si definisca la funzione func1(D), che riceve come parametro un dizionario
D, in cui ogni chiave e' un intero positivo N e il corrispondente valore
e' una lista di caratteri alfabetici L.
La funzione ritorna una lista in cui ogni item ' una stringa ottenuta ripetendo
N volte ciascuno dei caratteri in L. La lista e' ordinata in ordine alfabetico
decrescente.
Ad esempio se D = {2 : ['s', 'u', 'e'], 3 : ['q', 'a'], la funzione ritornera'
L = ['uu', 'ss', 'qqq', 'ee', 'aaa']
'''


def func1(D):
    lista = []
    for chiave, valore in D.items():
        for c in valore:
            lista.append(c * chiave) 
    ordinamento = lambda parola: parola
    return sorted(lista, key = ordinamento, reverse = True)
    pass

# Test della funzione func1
# print(func1({2: ['s', 'u', 'e'], 3: ['q', 'a']}))
# risultato: ['uu', 'ss', 'qqq', 'ee', 'aaa']


# %% ----------------------------------- FUNC2 ------------------------- #
''' func2: 2 punti
Si definisca la funzione func2(L) che ha come parametro una lista L di N liste.
Ogni lista P della lista L e' cosi' definita:
- P puo' essere vuota oppure contenere una sola lista, a sua volta definita come P.
La funzione ritorna una lista di N interi, in cui l'elemento i-esimo
indica il numero di liste nidificate nella lista in i-esima posizione di L.
Ad esempio, se L = [ [[]], [], [[[]]], [[]], [[[[]]]], [], [[[]]] ]
la funzione restituira' [1, 0, 2, 1, 3, 0, 2]
'''

def profondita(lista):
    if not isinstance(lista, list) or not lista:  # se non è lista o è vuota
        return 0
    massimo = 0
    for sotto in lista:
        valore = profondita(sotto)
        if valore > massimo:
            massimo = valore
    return 1 + massimo

def func2(L):
    risultato = []
    for elem in L:
        risultato.append(profondita(elem))
    return risultato
    pass


# Test della funzione func2
# print(func2( [ [[]], [], [[[]]], [[]], [[[[]]]], [], [[[]]] ]))
# risultato: [1, 0, 2, 1, 3, 0, 2]

# %% ----------------------------------- FUNC3 ------------------------- #
'''  func3: 2 punti
Si definisca la funzione func3(S) che riceve in input una stringa contenente
delle parole separate da virgole ed, opzionalmente, anche da spazi.
La funzione deve estrarre le parole da S, considerando solo quelle che
cominciano con una vocale, ed inserirle in una seconda lista ordinata
alfabeticamente senza considerare la differenza tra maiuscole e minuscole.
Ad esempio se S = "Brad,ALIce, keVin,  oscar, Dana,   UMA,ian, Zoe"
la funzione restituira': ['ALIce', 'ian', 'oscar', 'UMA']
'''


def func3(S):
    lista = []
    parti = S.split(',')
    for parola in parti:
        lista.append(parola.strip())
    finale = []
    for parola in lista:
        if parola[0] in 'aeiouAEIOU':
            finale.append(parola)
    ordinamento = lambda parola: parola.lower()
    return sorted(finale, key = ordinamento)
    pass

# Test della funzione func3
# print(func3("Brad,ALIce, keVin,  oscar, Dana,   UMA,ian, Zoe"))
# # risultato: ['ALIce', 'ian', 'oscar', 'UMA']


# %% ----------------------------------- FUNC4 ------------------------- #
""" func4: 6 punti
Definire la funzione func4(input_filepath, output_filepath) che legge il
file indicato da input_filepath.  Il file di input contiene parole separate
da ritorni a capo, spazi, tabulazioni, virgole o punto e virgola.  Due parole sono
considerate identiche se coincidono ignorando la distinzione
tra minuscole e maiuscole; in tal caso, la parola va considerata una sola volta.

Le parole considerate vanno raggruppate secondo la loro ultima lettera,
senza distinzione fra maiuscole e minuscole. Per ogni gruppo occorre
scrivere nel file di output una riga nel formato:

<lettera minuscola>: <numero parole>

La lettera iniziale di riga è in minuscolo, seguita da ": " (due punti più
spazio); di seguito, compare il numero di parole che terminano con quella lettera,
indipendentemente dal fatto che la lettera nella parola sia maiuscola o minuscola.
Le righe devono apparire in ordine alfabetico decrescente in base alla
lettera.

Attenzione, alla fine di ogni riga nel file di output NON c'e' alcuno spazio ma c'e'
SEMPRE un ritorno a capo!

La funzione deve restituire il numero totale di parole, compresi i duplicati,
trovate nel file di input.

Ad esempio:

contenuto di func4/func4_in1.txt:
GE
wOa;II,see	ua;PAO,oA;wOA
pao iu;jJa,kE

Chiamata
n = func4("func4/func4_in1.txt", "func4/func4_out1.txt")

contenuto atteso di func4/func4_out1.txt:
u: 1
o: 1
i: 1
e: 3
a: 4

Valore restituito: 12
"""


def func4(input_filepath, output_filepath):
    separatori = [' ', '\t', '\n', ',', ';']
    parole_uniche = set()  # per evitare duplicati
    totale_parole = 0
    parole = []

    # lettura e separazione parole
    with open(input_filepath, mode="r", encoding="utf8") as F:
        for riga in F:
            parola = ""
            for c in riga:
                if c in separatori:
                    if parola:
                        totale_parole += 1
                        parole.append(parola)
                        parole_uniche.add(parola.lower())
                        parola = ""
                else:
                    parola += c
            if parola:
                totale_parole += 1
                parole.append(parola)
                parole_uniche.add(parola.lower())

    # raggruppa parole per ultima lettera
    gruppi = {}
    for p in parole_uniche:
        ultima_lettera = p[-1].lower()
        if ultima_lettera not in gruppi:
            gruppi[ultima_lettera] = 1
        else:
            gruppi[ultima_lettera] += 1

    # scrivi file di output in ordine alfabetico decrescente
    with open(output_filepath, mode="w", encoding="utf8") as F_out:
        for lettera in sorted(gruppi.keys(), reverse=True):
            F_out.write(f"{lettera}: {gruppi[lettera]}\n")

    return totale_parole

# n = func4("func4/in_test1.txt", "func4/exp_test1.txt")
# print(n)


# %% ----------------------------------- FUNC5 ------------------------- #
""" func5: 8 punti
Definire la funzione func5(file_in, file_out) che usa images.load per
caricare l'immagine presente in file_in. L'immagine è una lista di liste
e ogni elemento interno è un pixel rappresentato dalla tupla (r, g, b).
Lo sfondo è completamente nero, cioè (0, 0, 0).

Nell'immagine possono apparire solo i seguenti gruppi di pixel non neri,
tutti di colore uniforme:
- gruppi 1x1, 1x2 o 2x1
- gruppi 2x2

Non esistono gruppi più grandi di 2x2 e due o piu' gruppi distinti ma vicini
sono sempre separati da pixel neri.

La funzione deve:
1. individuare tutti i blocchi 2x2 in cui i 4 pixel sono dello
   stesso colore non nero;
2. sostituire i quattro pixel con il nero, lasciando invariato il resto
   dell'immagine;
3. salvare il risultato in file_out mediante images.save;
4. restituire il numero di blocchi 2x2 trovati e oscurati.
"""
import images


def func5(file_in, file_out):
    img = images.load(file_in)
    altezza, larghezza = len(img), len(img[0])
    contatore_blocchi = 0
    for y in range(altezza - 1):
        for x in range(larghezza - 1):
            # vedo come è formato un blocco
            blocco = [img[y][x], img[y][x+1], img[y+1][x], img[y+1][x+1]]
            
            if blocco[0] != (0, 0, 0) and blocco.count(blocco[0]) == 4:
                        img[y][x] = (0, 0, 0)
                        img[y][x+1] = (0, 0, 0)
                        img[y+1][x] = (0, 0, 0)
                        img[y+1][x+1] = (0, 0, 0)
                        contatore_blocchi += 1
        
    images.save(img, file_out)
    return contatore_blocchi
        
        
    pass

# Test della funzione func5
# print(func5("func5/in_test1.png", "func5/out_test1.png"))
# risultato: 3 (il numero di blocchi 2x2 trovati nell'immagine di test)

# %% ----------------------------------- EX.1 ------------------------- #
'''
Ex1: 6 punti

Si consideri la classe BinaryTree contenuta nel file tree.py che definisce
un nodo di albero binario. Scrivere una funzione ex1(T) ricorsiva o che faccia
uso di una o piu' funzioni ricorsive.
La funzione riceve la radice di un BinaryTree come input. Nei nodi
dell'albero in input sono memorizzate delle stringhe vuote.
La funzione deve percorrere tutto l'albero e modificarlo in-place,
in modo che ogni nodo contenga una stringa di N asterischi, dove
N e' il livello del nodo. La radice si trova a livello 0, quindi
alla fine dell'esecuzione di ex1 conterra' ancora una stringa vuota.
La funzione ritorna l'altezza dell'abero (un albero con solo la
radice ha altezza 0).
Ad esempio, se T e' il seguente albero:

          ""                livello 0
       --------
       |      |
      ""      ""            livello 1
  ---------    --
  |       |      |
  ""     ""     ""          livello 2
  
Dopo aver eseguito la funzione, questa ritornera' il
valore 2 e T conterra':
          ""                livello 0
       --------
       |      |
      "*"    "*"            livello 1
  ---------    --
  |       |      |
 "**"    "**"   "**"        livello 2
'''
import tree


def ex1(T):
    modifica_albero_in_place(T, livello = 0)
    return calcolo_altezza(T)
    
def modifica_albero_in_place(T, livello = 0):
    if T is None:
        return
    T.value += "*"
    modifica_albero_in_place(T.left, livello+1)
    modifica_albero_in_place(T.right, livello+1)
    
def calcolo_altezza(T):
    if T is None:
        return -1
    return 1 + max(calcolo_altezza(T.left), calcolo_altezza((T.right)))
    
    pass


# Test della funzione ex1
# print(ex1(tree.BinaryTree.fromList(["", ["", ["", None, None], None], ["", None, ["", None, None]]])))
# risultato: 2

# %% ----------------------------------- EX.1 ------------------------- #
"""
Ex2: 6 punti

Scrivere la funzione ex2(L, k) ricorsiva oppure che faccia uso di
funzioni ricorsive. L è una lista di N liste di caratteri, ciascuna non
vuota. k è un intero compreso tra 0 e N.

Ogni carattere è una stringa di lunghezza 1 composta da sole lettere
ASCII minuscole. La funzione deve costruire e restituire la lista, ordinata in
modo alfabetico crescente, di tutte le stringhe lunghe N ottenute
scegliendo un carattere dalla prima sottolista, uno dalla seconda e così
via, a condizione che il numero totale di vocali presenti nella stringa
(esattamente le lettere 'a', 'e', 'i', 'o', 'u') sia pari a k.

Se in L compaiono caratteri ripetuti, l'output non deve contenere
duplicati: ogni stringa va inserita una sola volta.

Esempio:
L = [['c', 'q', 'a', 'a'], ['w', 'e', 'y']]
k = 1

Output atteso:
['aw', 'ay', 'ce', 'qe']
"""

def conta_vocali(stringa: str):
    vocali = 'aeiou'
    conteggio = 0
    for c in stringa:
        if c in vocali:
            conteggio += 1
    return conteggio

def ex2(L, k):
    if L == []:
        return ['']
    resto = ex2(L[1:], k)
    risultato = []
    for c in L[0]:
        for r in resto:
            combinazione = c + r
            risultato.append(combinazione)
        
    resto2 = ex2(L[1:], k-1)
    risultato2 = []
    for c in L[0]:
        for r in resto2:
            permutazione = c + r
            risultato2.append(permutazione)
            
    lista = risultato + risultato2
    finale = []
    for s in lista:
        if conta_vocali(s) == k:
            finale.append(s)
    
    # rimuovo eventuali duplicati e ordino
    return sorted(list(set(finale)))

# Test
L = [['c', 'q', 'a', 'a'], ['w', 'e', 'y']]
print(ex2(L, 1))
# Output corretto: ['aw', 'ay', 'ce', 'qe']


# %%
###################################################################################
if __name__ == '__main__':
    # Scrivi qui i tuoi test
    print('*' * 50)
    print('Devi eseguire il grade.py se vuoi debuggare con il grader incorporato.')
    print(
        'Altrimenti puoi inserire qui del codice per testare le tue funzioni ma devi scriverti i casi che vuoi testare')
    print('*' * 50)
