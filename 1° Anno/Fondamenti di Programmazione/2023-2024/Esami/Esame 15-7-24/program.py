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
    - risolvere almeno 1 esercizio di tipo ex (problema ricorsivo) AND;
    - ottenere un punteggio maggiore o uguale a 18

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
Si definisca la funzione func1(L) che, ricevendo come argomento una lista
di stringhe L, restituisce una lista di tuple. Ogni tupla contiene due
elementi corrispondenti agli elementi della lista L: il primo è la lunghezza
il secondo è il numero di vocali della stringa originale corrispondente,
ignorando la distinzione fra minuscole e maiuscole.
La lista di tuple deve essere ordinata in ordine decrescente rispetto al
numero di vocali e, in caso di parità, crescente rispetto alla lunghezza
della stringa.

Esempio:
L = ['cAsa', 'xyzzY', 'gAtto', 'topO', 'ragno', 'canE', 'tappEto', 'Oca']
risultato = [(7, 3), (3, 2), (4, 2), (4, 2), (4, 2), (5, 2), (5, 2), (5, 0)]
'''
def func1(L):
    lista = []
    for stringa in L:
        numero_vocali = sum(1 for char in stringa if char.lower() in "aeiou")
        lista.append((len(stringa), numero_vocali))
    lista.sort(key=lambda x: (-x[1], x[0]))
    return lista
                
    pass

# L = ['cAsa', 'xyzzY', 'gAtto', 'topO', 'ragno', 'canE', 'tappEto', 'Oca']
# print(func1(L)) # [(7, 3), (3, 2), (4, 2), (4, 2), (4, 2), (5, 2), (5, 2), (5, 0)]


# %% ----------------------------------- FUNC2 ------------------------- #
''' func2: 2 punti
Si definisca la funzione func2(D) che, ricevendo come argomento un
dizionario D, che ha come chiavi dei valori interi e come valori delle
liste di stringhe, restituisce un insieme di tuple.

Ogni tupla contiene tre elementi: il primo è la chiave, il secondo è
la prima parola della lista di stringhe in ordine alfabetico, il terzo
l'ultima parola della lista di stringhe in ordine alfabetico.

Esempio:
D = {1: ['casa', 'gatto', 'topo', 'ragno'], 2: ['tappeto', 'cane', 'oca']}
risultato = {(2, 'cane', 'tappeto'), (1, 'casa', 'topo')}
'''
def func2(D):
    chiavi = []
    for chiave in D.keys():
        chiavi.append(chiave)
    print(chiavi)
    prime_parole = []
    ultime_parole = []
    for valore in D.values():
        valore = sorted(valore, key = lambda x: x)
        if valore:
            prime_parole.append(valore[0])
            ultime_parole.append(valore[-1])
    print(prime_parole)
    print(ultime_parole)
    risultato = set(zip(chiavi, prime_parole, ultime_parole))
    return risultato
    pass

# D = {1: ['casa', 'gatto', 'topo', 'ragno'], 2: ['tappeto', 'cane', 'oca']}
# print(func2(D)) # {(2, 'cane', 'tappeto'), (1, 'casa', 'topo')}

# %% ----------------------------------- FUNC3 ------------------------- #
'''  func3: 2 punti
Si definisca la funzione func3(L1, L2) che, ricevendo come argomento
due liste di stringhe L1 e L2, restituisce un dizionario che ha come
chiavi le stringhe presenti solo in L1 e come valori degli insiemi di
stringhe.

Ad ogni chiave di D corrisponde l'insieme delle stringhe di L2 non
presenti in L1 e che hanno la stessa lunghezza della stringa chiave.

Esempio:
L1 = ['casa', 'gatto', 'cane', 'oca', 'elefante']
L2 = ['paperino', 'cane', 'gatto', 'ragno', 'topo', 'cip', 'map']
risultato = {'elefante': {'paperino'}, 'oca': {'cip', 'map'}, 'casa': {'topo'}}
'''

def func3(L1, L2):
    risultato = {}
    for stringa in L1:
        if stringa not in L2:
            insieme = set()
            for stringa2 in L2:
                if stringa2 not in L1 and len(stringa) == len(stringa2):
                    insieme.add(stringa2)
            risultato[stringa] = insieme
    return risultato

# L1 = ['casa', 'gatto', 'cane', 'oca', 'elefante']
# L2 = ['paperino', 'cane', 'gatto', 'ragno', 'topo', 'cip', 'map']
# print(func3(L1, L2)) # {'elefante': {'paperino'}, 'oca': {'cip', 'map'}, 'casa': {'topo'}}

# %% ----------------------------------- FUNC4 ------------------------- #
""" func4: 6 punti
Si definisca la funzione func4(file_input, file_output) che, ricevendo
come argomento il path di un file di testo file_input contenente
parole separate da spazi, tab e a capo, crea un file di testo
file_output e ritorna una tupla.

Il file in output deve contenere tutte le parole contenute nel file
indicato da file_input SENZA RIPETIZIONI e organizzate con le seguenti
regole:

- Le parole che iniziano con la stessa lettera, indipendentemente se
  maiuscola o minuscola, devono essere sulla stessa riga in ordine
  alfabetico decrescente, separate da uno spazio.

- Le righe devono essere ordinate in ordine alfabetico crescente
  rispetto alla prima parola di ogni riga.

La funzione torna il numero di parole lette dal file ed il numero
totale di caratteri letti dal file di input.

Esempio:
se il file di input contiene le 20 parole:
    casa cane gatto topo
    paperino ragno topo
    cane cip cip
    casa cane gatto topo
    paperino ragno topo
    cane cip cip
il risultato è un file di output contenente:
    cip casa cane
    gatto
    paperino
    ragno
    topo
e la funzione ritorna (20, 156)
"""

def func4(input_filename, output_filename):
    with open(input_filename, 'r', encoding = 'utf-8') as file:
        testo = file.read()
        parole = testo.split()
    D = {}
    for parola in parole:
        iniziale = parola[0].lower()
        D[iniziale] = D.get(iniziale, []) + [parola]
    for k,v in D.items():
        D[k].sort(reverse=True)
    with open(output_filename, mode='w', encoding='utf8') as f:
        for k in sorted(D):
            f.write(' '.join(D[k]) + '\n')
    return len(parole), len(testo)     
 
 
# print(func4('func4/in_0.txt', 'func4/out_0.txt')) # (20, 156)


# %% ----------------------------------- FUNC5 ------------------------- #
""" func5: 6 punti
Si definisca la funzione func5(input_png, output_png, S) che,
ricevendo come argomento il path di un file .png input_png, e un
intero S, crea un file .png output_png che contiene l'immagine di
input, suddivisa in quadretti SxS, in cui ciascun quadretto è ruotato
in senso orario di 90°.

NOTA: se esistono quadretti che sbordano a destra o sotto, non devono
essere ruotati.

La funzione ritorna il numero di quadretti ruotati.

Esempio: se l'immagine input_png è func5/3cime.png e S=50, l'immagine
output_png sarà come func5/expected_3cime_50.png e la funzione tornerà
15.  
"""
import images

def func5(input_png, output_png, S):
    ## Scrivi qui il tuo codice
    pass


# print(func5('func5/in_3cime.png', 'func5/out_3cime_50.png', 50)) # 15
# print(func5('func5/in_3cime.png', 'func5/out_3cime_13.png', 13)) # 294

# %% ----------------------------------- EX.1 ------------------------- #
"""
Ex1: 6 punti

Definire la funzione ex1(stringa, l), ricorsiva o che utilizza funzioni o metodi ricorsivi,
che prende in ingresso una stringa e un intero l e restituisce
l'insieme di tutti i possibili anagrammi di lunghezza l senza alcun carattere
doppio che possono essere costruiti con i caratteri della stringa.
Se l è maggiore della lunghezza della stringa, l'insieme restituito è vuoto.

Esempio:
    ex1('aabca', 4) should return the set
    {'acba', 'caba', 'acab', 'abac', 'abca', 'baca'}

"""
import os

def senza_doppi(s:str):
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            return False 
    return True

def ex1(string, l):
    if l == 0:
        return {""}   # insieme con stringa vuota come base
    if l > len(string):
        return set()

    risultato = set()
    for i in range(len(string)):
        lettera = string[i]
        resto = string[:i] + string[i+1:]
        for p in ex1(resto, l-1):
            nuovo = lettera + p
            if senza_doppi(nuovo):
                risultato.add(nuovo)
    return risultato
    pass



print(ex1('aabca', 4)) # {'acba', 'caba', 'acab', 'abac', 'abca', 'baca'}
# print(ex1('aabca', 5)) # {'abaca', 'acaba'}

# %% ----------------------------------- EX.1 ------------------------- #
"""
Ex2: 6 points

Definire una funzione ex2(root), ricorsiva o che utilizzi funzioni
o metodi ricorsivi, che prenda in input un albero con valori interi,
istanza della classe tree.BinaryTree.
La funzione deve modificare l'albero in modo che ogni nodo con due figli
abbia il figlio di sinistra più piccolo di quello di destra.
Lo scambio deve avvenire sull'intero albero, non solo sui valori.
La funzione deve restituire l'altezza dell'albero. 

Per esempio, se l'albero in ingresso è:

               6
              / \
             5   3
            /   / \
           4   10  6
              /   / \
             7   8  1
             
la funzione lo modifica in questo modo:

                6
              /   \
             3     5
            / \   /
           6  10  4
          / \  /  
         1  8 7   
                 
e ritorna il valore 4
"""
import tree

def ex2(root):
    ## Scrivi qui il tuo codice
    pass
    if root is None: 
        return 0
    if not root.left is None and not root.right is None and root.left.value > root.right.value:
        root.left, root.right = root.right, root.left
    return max(ex2(root.left), ex2(root.right)) + 1


# T = tree.BinaryTree.fromList([6, [5, None, [4, None, None] ], [3, [10, [7, None, None], None],
#                                                                [6, [8, None, None], [1, None, None]]]])
# print(T)
# print(ex2(T))
# print(T)
    
# %% 
###################################################################################
if __name__ == '__main__':
    # Scrivi qui i tuoi test
    print('*'*50)
    print('Devi eseguire il grade.py se vuoi debuggare con il grader incorporato.')
    print('Altrimenit puoi inserire qui del codice per testare le tue funzioni ma devi scriverti i casi che vuoi testare')
    print('*'*50)
