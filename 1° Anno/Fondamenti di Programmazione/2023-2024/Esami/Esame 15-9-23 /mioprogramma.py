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

Il voto finale è dato dalla somma dei punteggi degli esercizi risolti.

Attenzione! DEBUG=True nel grade.py per migliorare il debugging.
Per testare correttamente la ricorsione è, però, necessario DEBUG=False.

"""

nome       = "Romolo"
cognome    = "Deffereria"
matricola  = "2114887"


# %% ----------------------------------- FUNC1 ------------------------- #
'''func1: 2 punti

Si definisca la funzione func1(int_list, keys) che prende in ingresso una
lista 'int_list' e un set 'keys' contenenti interi. La funzione restituisce
un dizionario in cui le chiavi sono gli interi in keys e i valori sono
liste con gli interi presenti in int_list divisibili per l'intero della
chiave corrispondente.
Le liste sono ordinate in ordine decrescente.


Esempio: se int_list=[4, 6, 10, 13] e keys={2, 3, 5}
  l'invocazione di func1(int_list, keys) deve restituire il dizionario
  {2:[10, 6, 4], 3:[6], 5:[10]}
'''
def func1(int_list, keys):
    dizionario = {}
    for key in keys:
        interi_divisibili = set()
        for intero in int_list:
            if intero % key == 0:
                interi_divisibili.add(intero)
        lista = sorted(interi_divisibili, reverse=True)
        print(lista)
        dizionario[key] = lista
    return dizionario
    pass

int_list=[4, 6, 10, 13]
keys={2, 3, 5}

print(func1(int_list, keys))


# %% ----------------------------------- FUNC2 ------------------------- #
''' func2: 2 punti

Si definisca una funzione func2(a_string, char) che prende in ingresso due
stringhe 'a_string' e 'char' e restituisce un'altra stringa. La stringa
'char' è composta da un solo carattere.
La nuova stringa ha tutte i caratteri della stringa a_string con un valore
unicode strettamente maggiore del valore del carattere in 'char'. I caratteri
nella stringa in output sono ripetute una volta sola e in ordine alfabetico
inverso.
Si suggerisce di usare la funzione ord per determinare il valore unicode di
un carattere.

Esempio: se a_string='impossible' l'invocazione di func2(a_string, 'i') dovrà
         restituire la stringa 'spoml'
'''

def func2(a_string, char):
    nuova_stringa = ''
    for c in a_string:
        if ord(c) > ord(char):
            nuova_stringa += c
    return ''.join(sorted(set(nuova_stringa), reverse=True))
    pass

# print(func2('impossible', 'i'))


# %% ----------------------------------- FUNC3 ------------------------- #
'''func3: 2 punti

Definire una funzione func3(string_list1, string_list2) che prende
in ingresso due liste di stringhe e restituisce una nuova lista di stringhe.
La nuova lista è composta da tutte le stringhe presenti in una delle due
liste di input che contengono come sottostringa almeno una stringa o una
stringa invertita dall'altra lista.
La lista risultante deve essere ordinata per numero di caratteri in ordine
decrescente, in caso di uguaglianza, in ordine alfabetico.

Esempio: se string_list1=['shop', 'park', 'elichopter', 'cat', 'elephant'] e
            string_list2=['ark', 'contact', 'hop', 'mark']
         l'invocazione di func3(string_list1, string_list2) restituirà
         la lista ['elichopter','contact','park', 'shop']

         Infatti:
             'elichopter' contiene 'hop',
             'contact' contiene la stringa invertita di 'cat'
             'park' contiene 'ark'
             'shop' contiene 'hop'
'''

def func3(string_list1, string_list2):
    string_list3 = []
    for stringa1 in string_list1:
        for stringa2 in string_list2:
            if stringa2 in stringa1 or stringa2[::-1] in stringa1:
                string_list3.append(stringa1)
                break
            if stringa1 in stringa2 or stringa1[::-1] in stringa2:
                string_list3.append(stringa2)
                break
    return sorted(string_list3, key=lambda x: (-len(x), x))
            
        
    pass


string_list1=['succouring', 'compartmental', 'sour', 'varityped', 'go', 'fulmination', 'wilfulness', 'dangerous', 'subtracting', 'fragmented', 'preciseness', 'rem', 'hypnotically']
string_list2=['hartebeests', 'absorbencies', 'straitening', 'precise', 'saragossa', 'enumerates', 'regna', 'margarines', 'invigilates', 'maladapted', 'prosperous', 'capitalize']
print(func3(string_list1, string_list2))

# %% ----------------------------------- FUNC4 ------------------------- #
""" func4: 6 punti

Si scriva una funzione func4(input_file, output_file) che prende in
ingresso due stringhe, 'input_file' e 'output_file' che rappresentano
i percorsi a due file.
Per ogni riga del file indicato da 'input_file' bisogna creare una
riga all'interno di un nuovo file indicato da 'output_file'.
In ogni riga del file indicato da 'input_file' sono presenti una serie
di parole composte da caratteri numerici e alfabetici, separate da spazi
e tabulazioni. Per ogni parola, la funzione individua i caratteri numerici,
li trasforma in interi e li somma insieme. In seguito, la funzione calcola il
prodotto di tutti i valori ottenuti per quella riga, scrivendo il risultato
sotto forma di stringa in una nuova riga del file 'output_file'.
Ogni parola ha almeno un carattere numerico.

La funzione deve restituire la somma di tutti i prodotti calcolati.

Esempio: se il contenuto del file 'input_file' è il seguente
car13 5park5 spike2
no1ne rebel44 ni4ce

l'invocazione di func4('input_file', 'output_file') dovrà scrivere nel
file 'output_file' le due righe
80
32

e ritornare il valore 112.
"""
def func4(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        somma = 0
        for riga in lines:
            for parola in riga.split():
                somma_parola = 1
                for carattere in parola:
                    if carattere.isdigit():
                        somma_parola *= int(carattere)
                somma += somma_parola
    
    pass

# print(func4('func4/func4_test1.txt','func4/func4_out1.txt'))
# print(func4('func4/func4_test2.txt','func4/func4_out2.txt'))
# print(func4('func4/func4_test3.txt','func4/func4_out3.txt'))


# %% ----------------------------------- FUNC5 ------------------------- #
""" func5: 8 punti

Si definisca una funzione func5(input_pngfile) che prende in ingresso
una stringa che contiene il percorso ad un file con un'immagine in
formato PNG.
L'immagine indicata da 'input_pngfile' contiene dei segmenti
orizzontali di colore uniforme su uno sfondo nero. Su una riga ci
possono essere piu segmenti di colore diverso, anche attaccati fra
loro.  La funzione deve individuare tutti i segmenti presenti
nell'immagine e ritornare un lista di triple rappresentanti i colori
dei segmenti individuati, ordinati dal piu lungo al piu corto. In caso
di segmenti di uguale lunghezza, i colori vanno ordinati considerando
l'ordine prima della terza componente, poi della seconda e infine
della prima. Le componenti seguono un ordine crescente.  In caso di
segmenti di uguale colore, si deve considerare quello con la lunghezza
maggiore.

Esempio: nell'immagine del file func5/image01.png sono presenti quattro segmenti
         uno di lunghezza 50 con colore (0, 128, 200)
         uno di lunghezza 30 con colore (200, 128, 200)
         uno di lunghezza 30 con colore (200, 200, 128)
         uno di lunghezza 29 con colore (0, 128, 200),
         per cui func5('func5/image01.png') deve restituire la lista
         [(0, 128, 200), (200, 200, 128), (200, 128, 200)]
"""
import images

def func5(input_pngfile):
    
    pass

# print(func5('func5/image01.png'))
# print(func5('func5/image02.png'))
# print(func5('func5/image03.png'))
# print(func5('func5/image04.png'))


# %% ----------------------------------- EX.1 ------------------------- #
"""
Ex1: 6 punti

Si scriva una funzione ricorsiva ex1(a_set, n), o che al suo interno
usi una funzione ricorsiva, che prende in ingresso un set di stringhe 'a_set'
e un intero n e restituisca un nuovo set. Il set deve contenere tutte le
possibili stringhe ottenute con la concatenazione di n elementi appartenenti
ad da a_set, senza ripetizione.
Se n è maggiore del numero di elementi presenti in a_set, la funzione
restituisce un set vuoto.

Esempio:
    la funzione ex1({'a','b','c'}, 2) deve restituire l'insieme
    {'ab', 'ba', 'ac', 'ca', 'bc', 'cb'}
"""

def ex1(a_set, n):
    if n > len(a_set):
        return set()
    elif n == 1:
        return {carattere for carattere in a_set}
    else:
        set_finale = set()
        for carattere in a_set:
            sottosoluzioni = ex1(a_set - {carattere}, n-1)
            for sottosoluzione in sottosoluzioni:
                set_finale.add(carattere + sottosoluzione)
        return set_finale
    
    
print(ex1({'a', 'b', 'c'}, 2))

# %% ----------------------------------- EX.2 ------------------------- #
"""
Ex2: 6 punti

Si definisca la funzione ex2(root, m, n, k) ricorsiva (o che al suo interno
usa una funzione ricorsiva) che riceve in ingresso la radice di
un albero binario di interi, come definito nella classe `BinaryTree` del modulo
tree.py e tre interi m, n e k. La funzione ritorna il numero di nodi
dell'albero presenti ad un livello compreso fra m ed n, inclusi, con un
valore multiplo di k.
Si assume che la radice sia al livello 0.

Esempio:
    root
    ______5______           livello 0
   |             |
   8__        ___2___       livello 1
      |      |       |
     _3_     9       1      livello 2
    |   |
    6   12                  livello 3

    la chiamata a ex2(root, 1, 2, 3)  deve restituire il valore 2
  """


def ex2(root, m, n, k, level=0):
    return aggiungi_nodo(root, m, n, k, level)

def aggiungi_nodo(nodo, m, n, k, level):
        if nodo is None:
            return 0
        valori = 0
        if m <= nodo.value <= n and nodo.value % k == 0:
            valori += nodo.value
        valori += aggiungi_nodo(nodo.left, m, n, k, level + 1)
        valori += aggiungi_nodo(nodo.right, m, n, k, level + 1)
        return valori
    



# from tree import BinaryTree
# root = BinaryTree.fromList([5, [8, None, [3, [6, None, None], [12, None, None]]], [2, [9, None, None],[1, None, None]]])
# print(ex2(root, 1,2,3))

###################################################################################

if __name__ == '__main__':
    # Place your tests here
    print('*'*50)
    print('ITA\nDevi eseguire il grade.py se vuoi debuggare con il grader incorporato.')
    print('Altrimenti puoi inserire qui del codice per testare le tue funzioni ma devi scriverti i casi che vuoi testare')
    print('*'*50)
    print('ENG\nYou have to run grade.py if you want to debug with the automatic grader.')
    print('Otherwise you can insert here you code to test the functions but you have to write your own tests')
    print('*'*50)
# -*- coding: utf-8 -*-

