#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
################################################################################
################################################################################

""" Operations to do FIRST OF ALL:
 1) Save this file as program.py
 2) Assign the variables below with your
    NAME, SURNAME and MATRICULATION NUMBER
 3) Change the directory name examPY in your matriculation number

To pass the exam you have to:
    - solve at least 3 func problems and
    - solve at least 1 rec problem
    - get a score greater or equal to 18

The final score is the sum of the solved problems.
"""
name       = "Romolo"
surname    = "Deffereria"
student_id = "2114887"

#########################################

################################################################################
################################################################################
################################################################################
# ---------------------------- DEBUG SUGGESTIONS ----------------------------- #
# To run only some of the tests, you can comment the entries with which the
# 'tests' list is assigned at the end of grade.py
#
# To debug recursive functions you can turn off the recursive test setting
# DEBUG=True in the file grade.py
#
# DEBUG=True turns on also the STACK TRACE that allows you to know which
# line number in program.py generated the error.
################################################################################

# %%  ---- FUNC1 ----
''' func1: 2 punti
Definisci una funzione func1(string_list) che prende in input una lista di stringhe e
restituisce un'altra lista con solo le stringhe che iniziano con una lettera maiuscola.
La lista restituita deve essere ordinata per numero di lettere in ordine crescente.
'''
def func1(string_list):
    lista = []
    for stringa in string_list:
        if stringa[0].isupper():
            lista.append(stringa)
    return sorted(lista, key = lambda x: len(x))
    pass

string_list = ['Home', 'dog', 'HASSe','Zar']
print(func1(string_list))

# %%  ---- FUNC2 ----
''' func2: 2 punti
Definisci una funzione func2(pathname) che prende in input una stringa che rappresenta
il percorso di un file di testo. Il file contiene solo righe con due parole separate da
uno spazio. La funzione deve restituire un dizionario dove le chiavi sono i primi
elementi di una riga e i valori sono insiemi con i secondi elementi di una riga.
Ogni secondo elemento di una riga appare nell'insieme corrispondente alla chiave
del primo elemento della stessa riga.

Esempio:
Contenuto di animals.txt:
    cat     meaow
    dog     woof
    cat     purr
La chiamata func2('animals.txt') restituisce {'cat':{'meaow', 'purr'}, 'dog':{'woof'}}
'''
def func2(pathname):
    dizionario = {}
    with open(pathname, 'r', encoding='utf-8') as file:
        righe = file.readlines()
        for riga in righe:
            parole = riga.strip().split()
            if len(parole) == 2:
                chiave, valore = parole
                if chiave in dizionario:
                    dizionario[chiave].add(valore)
                else:
                    dizionario[chiave] = {valore}
    return dizionario

# Esempio di utilizzo
pathname = 'animals.txt'
expected = {'cat': {'meaow', 'purr'}, 'dog': {'woof'}}
print(func2(pathname))  # Output: {'cat': {'meaow', 'purr'}, 'dog': {'woof'}}

# %%  ---- FUNC3 ----
'''  func3: 2 punti
Definisci una funzione func3(listA, listB, listC) che prende tre liste
di numeri (interi o float) e restituisce una nuova lista dove ogni elemento è
ottenuto considerando la somma tra gli elementi corrispondenti delle liste
listA e listB, somma moltiplicata per l'elemento corrispondente di listC.
La funzione deve restituire la lista costruita.
'''
def func3(listA, listB, listC):
    lista = []
    for i in range(len(listA)):
        lista.append((listA[i]+listB[i]) * listC[i])
    return lista
    pass

listA = [4, 1, 3, 5, 2]
listB = [5, 1, 1, 2, 3]
listC = [10, 5, 9, 9, 6]
#expected = [90, 10, 36, 63, 30]
print(func3(listA,listB,listC))

# %%  ---- FUNC4 ----
""" func4: 6 punti

Definisci la funzione func4(triangles) che prende in input una lista di
terzine di numeri positivi ed elimina dalla lista tutte le terzine che
non possono essere i lati di un triangolo rettangolo. Ogni numero nella
terzina può essere sia un cateto che l'ipotenusa, e non c'è un ordine
predeterminato. La funzione deve restituire il numero di terzine
eliminate dalla lista triangles. La lista triangles deve essere modificata
in loco. Per valutare se un triangolo è rettangolo si può usare il
teorema di Pitagora: la somma dei quadrati costruiti sui cateti deve
essere uguale al quadrato costruito sull'ipotenusa. Per i confronti,
usare la funzione di arrotondamento round(x, 3).

Esempio: se triangles = [(3, 4, 5), (12, 36.05551, 34),
                         (1,1,3), (8,8,8), (2, 3, 4)],
         la funzione func4(triangles) restituisce il valore 3 e modifica la lista
         in modo che
         triangles = [(3, 4, 5), (12, 36.05551, 34)].

Infatti, considerando il risultato atteso triangles = [(3, 4, 5), (12, 36.05551, 34)]
si verifica quanto segue:

| terzina            | verifica è True                                 |
| (3, 4, 5)          | round( 3² + 4² , 3) == round( 5² , 3)           |
| (12, 36.05551, 34) | round( 12² + 34² , 3) == round( 36.05551² , 3)   |

NOTA: Suddividi il problema in piccoli sottoproblemi. Scrivi piccole funzioni
per ciascun sottoproblema. Componi tutto insieme.

"""


def func4(triangles):
    terzine_da_rimuovere = []
    for terna in triangles:
        a, b, c = sorted(terna)
        if round(a**2 + b**2, 3) != round(c**2, 3):
            terzine_da_rimuovere.append(terna)
    
    for terna in terzine_da_rimuovere:
        triangles.remove(terna)
    
    return len(terzine_da_rimuovere)

triangles = [(3, 4, 5), (12, 36.05551, 34), (1,1,3), (8,8,8), (2, 3, 4)]
print(func4(triangles))

# %%  ---- FUNC5 ----
""" func5: 6 points
Define a function func5(img, filename) that returns a copy of the image img
flipped with respect to the vertical axis and saves the image in the file
with path as the filename string taken in input. The function returns the
color of the pixel in position (0,0) of the new image.
"""
import images
def func5(img, filename):
    # WRITE HERE YOUR CODE
    pass



# %% ----------------------------------- EX.1 ----------------------------------- #
"""
Ex1: 6 punti

Definisci la funzione ricorsiva ex1 che prende in input una stringa
'directory' e una stringa 'namefile'. La funzione deve cercare
ricorsivamente all'interno della directory data da directory e in tutte
le sottodirectory tutti i file con nome uguale a namefile. Tali file
devono essere interpretati come file di testo. Ogni file di testo
contiene solo stringhe numeriche positive. I file con lo stesso namefile
hanno sempre lo stesso numero di stringhe numeriche. La funzione deve
restituire una lista di interi ottenuti sommando le stringhe numeriche
dei file trovati, posizione per posizione.

Esempio: se vengono trovati due file con lo STESSO namefile e quei
file contengono le sequenze "11 23 90" e "11 77 0," la funzione ex1
restituisce la lista [22, 100, 90].

Si consiglia di utilizzare le funzioni os.listdir, os.path.isfile e
os.path.isdir e di NON utilizzare la funzione os.join in Windows (usare
la concatenazione tra stringhe con il carattere '/').

È proibito usare la funzione os.walk.

NOTA: Suddividi il problema in piccoli sottoproblemi. Scrivi piccole
funzioni per ciascun sottoproblema. Componi tutto insieme.
"""

import os

def ex1(directory, namefile):
    def esplora(directory, namefile, somme):
        for nome in os.listdir(directory):
            fullname = directory + '/' + nome
            if os.path.isdir(fullname):
                esplora(fullname, namefile, somme)
            elif os.path.isfile(fullname) and nome == namefile:
                with open(fullname, 'r', encoding='utf-8') as file:
                    righe = file.readlines()
                    for riga in righe:
                        numeri = list(map(int, riga.split()))
                        if not somme:
                            somme.extend(numeri)
                        else:
                            for i in range(len(numeri)):
                                somme[i] += numeri[i]

    somme = []
    esplora(directory, namefile, somme)
    return somme

# Esempio di utilizzo
print(ex1('ex1/A', 'namefile.txt'))  # Output: [22, 100, 90] (se i file contengono le sequenze "11 23 90" e "11 77 0")

    


# %% Ex2
"""
Ex2: 3+3 punti
Definisci una funzione ricorsiva (o una che utilizza funzioni ricorsive)
ex2(strings, n) che prende un insieme 'strings' e un intero 'n' e
genera ricorsivamente tutte le possibili stringhe che possono essere
costruite concatenando n stringhe dell'insieme strings. La funzione deve
restituire tutte le stringhe costruite. La funzione può restituire
un insieme con tutte le stringhe costruite (3 punti), oppure una lista
ordinata (6 punti). La lista è ordinata considerando l'ordine decrescente
della lunghezza delle stringhe e, in caso di parità, considerando l'ordine
alfabetico.

Esempio: se strings={'a','b','c','de'}, la funzione ex2(strings, 2)
restituisce l'insieme {'ab','ac','ade','ba','ca','dea','bc','bde','cb','deb','cde','dec'} (3 punti)
oppure la lista ['ade', 'bde', 'cde', 'dea', 'deb', 'dec', 'ab', 'ac', 'ba', 'bc', 'ca', 'cb'] (6 punti)
"""


def ex2(strings, n):
    if n == 0:
        return {''}
    if n == 1:
        risultato = []
        for X in strings:
            risultato.append(X)
        return set(risultato)
    else:
        risultato = []
        for i in range(len(strings)):
            resto = list(strings.copy())
            Y = resto.pop(i)
            sottosoluzioni = ex2(resto, n-1)
            for sottosoluzione in sottosoluzioni:
                risultato.append(Y+sottosoluzione)
        risultato = sorted(risultato)
        return set(risultato)
    

strings={'a','b','c','de'}
print(ex2(strings,2))

###################################################################################
if __name__ == '__main__':
    # Place your tests here
    print('*'*50)
    print('ITA\nDevi eseguire il grade.py se vuoi debuggare con il grader incorporato.')
    print('Altrimenit puoi inserire qui del codice per testare le tue funzioni ma devi scriverti i casi che vuoi testare')
    print('*'*50)
    print('ENG\nYou have to run grade.py if you want to debug with the automatic grader.')
    print('Otherwise you can insert here you code to test the functions but you have to write your own tests')
    print('*'*50)
