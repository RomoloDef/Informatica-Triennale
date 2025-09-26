#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
################################################################################
################################################################################

""" Operazioni da svolgere PRIMA DI TUTTO:
 1) Salvare il file come program.py
 2) Assegnare le variabili sottostanti con il proprio
    NOME, COGNOME, NUMERO DI MATRICOLA

Per superare l'esame e' necessario soddisfare tutti i seguenti vincoli:
    - ottenere un punteggio maggiore o uguale a 18 (15 per i DSA)

Il voto finale e' la somma dei punteggi dei problemi risolti.

Attenzione! DEBUG=True nel grade.py per migliorare il debugging.
Per testare correttamente la ricorsione è, però, necessario DEBUG=False.

"""
nome       = "Romolo"
cognome    = "Deffereria"
matricola  = "2114887"


#########################################

################################################################################
# ---------------------------- SUGGERIMENTI PER IL DEBUG --------------------- #
# Per eseguire solo alcuni dei test, si possono commentare le voci
# corrispondenti ai test che non si vogliono eseguire all'interno della lista
# `test` alla FINE di `grade.py`.
#
# Per eseguire il debug di funzioni ricorsive potete disattivare il test di
# ricorsione, assegnando `DEBUG=True` all'interno file `grade.py`.
#
# L'impostazione DEBUG=True attiva anche lo la stampa a terminale dello STACK
# TRACE degli errori, che permette di conoscere il numero della linea di
# program.py che ha generato un errore.
################################################################################


# %% -------------------------------- FUNC.1 -------------------------------- #
''' func1: 2 punti
Si definisca la funzione func1(string_list1, string_list2) che riceve in
ingresso due liste di stringhe e restituisce una nuova lista di stringhe
contenente le stringhe presenti soltanto in una delle due liste in ingresso
(ossia, che non compaiono in entrambe le liste). La lista in output
dev'essere ordinata in ordine di lunghezza crescente e in caso di parità 
in ordine alfabetico inverso.
'''
def func1(string_list1, string_list2):
    finale = []
    for stringa in string_list1:
        if stringa not in string_list2: 
            finale.append(stringa)
    for stringa in string_list2:
        if stringa not in string_list1:
            finale.append(stringa)
    ordinamento = lambda x: (len(x), -ord(x[0]))
    return sorted(finale, key = ordinamento)
    pass

# string_list1 = ['a','bb','c']
# string_list2 = ['a','dd']
# expected = ['c', 'dd', 'bb']
# print(func1(string_list1,string_list2))

# %% -------------------------------- FUNC.2 -------------------------------- #
''' func2: 2 punti
Si definisca una funzione funct2(path_to_file) che riceve in ingresso
una stringa che rappresenta il percorso ad un file testuale. La funzione
deve restituire il dizionario che associ ad ogni carattere nel testo il
conteggio delle sue occorrenze.

Esempio:
  Il contenuto di func2_test_1.txt è:
cat rat fat
art
  L'output atteso dall'invocazione di func2('func2/func2_test_1.txt') è:
  {'c':1, 'a':4, 't':4, 'r':2, 'f':1, ' ':2, '\n':1}

Nota:
  Aprire il file con encoding 'utf-8'.
'''
def func2(path_to_file):
    occorrenze: dict = {}
    with open(path_to_file, mode = "r", encoding = "utf8") as F:
        caratteri = []
        righe = F.readlines()
        for riga in righe:
            for c in riga:
                caratteri.append(c)
        for c in caratteri:
            if c in occorrenze:
                occorrenze[c] += 1
            else:
                occorrenze[c] = 1
    return occorrenze
    pass

# pathname = 'func2/func2_test_1.txt'
# print(func2(pathname))

# %% -------------------------------- FUNC.3 -------------------------------- #
'''  func3: 2 punti
Si definisca una funzione func3(a_list) che riceve in ingresso una lista
di numeri ed opera su di essa (ossia, provocando side-effect) rimuovendo tutti
gli elementi uguali al massimo e al minimo.
La funzione deve restituisce la differenza fra la lunghezza iniziale e la
lunghezza finale della lista.

Esempio:
    se a_list = [3, 12, -3, 4, 6, 12]
    dopo la chiamata a func3(a_list) si ha che
    a_list = [3, 4, 6]
    e la funzione restituisce 3.

IMPORTANTE: la lista `a_list` deve risultare cambiata alla fine
dell'esecuzione della funzione.
'''

def func3(a_list):
    massimo = max(a_list)
    minimo = min(a_list)
    for i in range(len(a_list)-1,-1,-1):
        if a_list[i] == massimo:
            del a_list[i]
        elif a_list[i] == minimo:
            del a_list[i]
    return a_list
    pass

# print(func3([3, 12, -3, 4, 6, 12]))

# %% -------------------------------- FUNC.4 -------------------------------- #
""" func4: 6 punti
Si definisca una funzione func4(input_filepath, output_filename) che
riceve in ingresso due percorsi a file:
  - Il file `input_filepath` contiene una sequenza di parole, ossia stringhe
    separate da spazi, tabulazioni o invii a capo.
  - Il file `output_filename` indica dove salvare un nuovo file di testo,
    i cui contenuti sono specificati di seguito.
Il file in output deve contenere tutte le parole presenti in
`input_filename`, ripetute una sola volta e organizzate in righe nel modo
seguente.

Le righe nel file di output sono in ordine alfabetico decrescente.
All'interno di ogni riga, le parole
  - hanno la stessa lettera iniziale, senza distinzione fra maiuscole e
    minuscole;
  - sono separate da uno spazio;
  - sono ordinate in base alla loro lunghezza e, in caso di pari
    lunghezza, in base all'ordine alfabetico, senza distinzione fra
    maiuscole e minuscole. Nel caso in cui nessuno dei criteri sin qui
    forniti distingua le parole, quelle coincidenti devono essere
    disposte secondo ordinamento lessicografico (ovverosia, si tiene conto
    della differenza tra lettere maiuscole e minuscole solo in ultima
    istanza).

La funzione deve restituire il numero di righe scritte nel file
`output_filename`.

Esempio:
  Nel file 'func4/func4_test1.txt' sono presenti le seguenti due righe:
cat bat    rat
Condor baT
  L'invocazione di func4('func4/func4_test1.txt', 'func4/func4_out1.txt')
  dovrà scrivere nel file 'func4/func4_out1.txt' le seguenti tre righe
  restituendo il valore 3:
rat
cat Condor
baT bat
"""

def func4(input_filename, output_filename):
    with open(input_filename, mode="r", encoding="utf8") as file:
        parole = []
        iniziali = []
        righe = file.readlines()
        for riga in righe:
            riga = riga.split()
            for stringa in riga:
                parole.append(stringa)
        for stringa in parole:
            iniziali.append(stringa[0])
        iniziali = list(set(iniziali))
        dizionario = {}
        for parola in parole:
            iniziale = parola[0].lower()
            if iniziale not in dizionario:
                dizionario[iniziale] = []
            dizionario[iniziale].append(parola)
        for chiave in dizionario:
            dizionario[chiave].sort(key = lambda p: ((len(p), p.lower(), p)))
        
    righe_scritte = 0
    with open(output_filename, mode = "w", encoding = "utf8") as F:
        for chiave in sorted(dizionario.keys(), reverse=True):
            valore = dizionario[chiave]
            F.write(" ".join(valore) + "\n")
            righe_scritte += 1
        
    return righe_scritte
        
            
       
    pass

print(func4('func4/func4_test1.txt', 'func4/func4_out1.txt'))

# %% -------------------------------- FUNC.5 -------------------------------- #
""" func5: 8 punti
Si definisca una funzione func5(imagefile, output_imagefile, color) che riceve
in ingresso due stringhe che rappresentano due percorsi a file di immagini PNG e
un colore fornito come una tupla RGB.
L'immagine nel file `imagefile` contiene esclusivamente segmenti orizzontali
bianchi su uno sfondo nero. Ogni riga ha al più un segmento bianco.
La funzione deve creare una nuova immagine in cui sono presenti gli stessi
segmenti dell'immagine in ingresso e modificare il colore dei segmenti con
lunghezza minima utilizzando il colore color preso in ingresso.

L'immagine così ottuenuta deve essere salvata in formato PNG nel file con
percorso `output_imagefile`.

La funzione restituisce il numero di segmenti colorati nell'immagine
in output.
"""
import images
def func5(imagefile, output_imagefile, color, lunghezza_min=1):
    # carico l'immagine come matrice di pixel
    img = images.load(imagefile)
    altezza, larghezza = len(img), len(img[0])
    
    segmenti_colorati = 0

    # scorro tutte le righe
    for y in range(altezza):
        x_start = None
        for x in range(larghezza):
            r, g, b = img[y][x]
            if (r, g, b) == (255, 255, 255):  # pixel bianco
                if x_start is None:
                    x_start = x
                if x == larghezza - 1:  # fine riga
                    lunghezza = x - x_start + 1
                    if lunghezza >= lunghezza_min:
                        # coloro il segmento
                        for xi in range(x_start, x + 1):
                            img[y][xi] = color
                        segmenti_colorati += 1
            else:
                if x_start is not None:
                    lunghezza = x - x_start
                    if lunghezza >= lunghezza_min:
                        # coloro il segmento
                        for xi in range(x_start, x):
                            img[y][xi] = color
                        segmenti_colorati += 1
                    x_start = None

    # salvo l'immagine modificata
    images.save(output_imagefile, img)

    return segmenti_colorati
                
# imagefile = 'func5/image01.png'
# output_imagefile = 'func5/expected01.png'
# color = (255,0,0)            
# print(func5(imagefile, output_imagefile, color ))
    

# %% --------------------------------- EX.1 --------------------------------- #
"""
Ex1: 6 punti

Implementare la funzione ex1 (in modo ricorsivo o utilizzando funzioni
ricorsive) come segue. La funzione ex1 riceve in ingresso i seguenti
argomenti:
  - `directory`, una stringa che rappresenta il percorso di una directory
  - `ext`, una stringa che rappresenta un'estensione di file.
La funzione deve cercare in modo ricorsivo all'interno della `directory`
e in tutte le sue sottodirectory i file che abbiano `ext` come estensione.
Questi file devono essere interpretati come file di testo. La funzione
ex1 deve calcolare la somma delle dimensioni di tutti i file trovati
nelle sottodirectory e restituire un dizionario strutturato come
come segue:
  - le chiavi sono tutte le sottodirectory in cui è presente almeno
    un file con estensione `ext`
  - i valori sono la somma delle dimensioni di TUTTI i file contenuti in quella
  sottodirectory (inclusi quelli con estensione diversa).
Le sottodirectory devono essere riportate con il percorso relativo alla
directory corrente. Per esempio, data la struttura di directory:
A/
  B/
    file1.png    #4 byte
    file2.txt    #18 byte
  file3.txt      #8 byte

L'invocazione `ex1("A", ".png")` deve restituire `{"A/B":22}`

La dimensione di un file può essere calcolata contando il numero di caratteri
letti dal file.

Si consiglia di utilizzare le funzioni os.listdir, os.path.isfile e
os.path.isdir e NON la funzione os.join in Windows. Utilizzare
la concatenazione tra stringhe con il carattere '/'.

E' PROIBITO usare la funzione os.walk.
"""

import os


def ex1(directory, ext):
    risultato = {}
    totale = 0
    estensione = False
    for nome in os.listdir(directory):
        if nome[0] in '._': continue
        fullname = directory + '/' + nome 
        if os.path.isdir(fullname):
            trovato = ex1(fullname, ext)
            risultato.update(trovato)
        if os.path.isfile(fullname):
            with open(fullname, mode = "r", encoding = "utf8") as file:
                contenuto = file.read()
                size = len(contenuto)
                totale += size
        if nome.endswith(ext):
            estensione = True
    if estensione is True:
        risultato[directory] = totale
    return risultato
    pass

directory = 'ex1/A'
ext = '.py'
print(ex1(directory, ext))



# %% --------------------------------- EX.2 --------------------------------- #
"""
Ex2: 6 punti

Si definisca la funzione ex2(root) che riceve in ingresso la radice di un
albero binario, come definito nella classe `BinaryTree` del modulo tree.py.
La funzione deve restituire la somma di tutti i valori associati ai nodi che
sono ad un livello dispari nell'albero con radice `root`, e sottraendo tutti i
valori associati ai nodi ad un livello pari. La radice si assume a livello 0.

Esempio:

        ______5______                        ______2______
       |             |                      |             |
       8__        ___2___                __ 7__        ___5___
          |      |       |              |      |      |       |
          3      9       1             _4_     3_    _0_     _5_
                                      |   |      |  |   |   |   |
                                      2   -1     1  8   3   2   9

    Se l'albero è quello di sinistra, la funzione deve ritornare il valore -8.
    Se l'albero è quello di destra, la funzione deve ritornare il valore 22.
"""
import tree

def ex2(root):
    if root is None:
        return 0
    nodi_dispari = cerca_nodi_dispari(root, profondità=0)
    somma = 0
    for nodo in nodi_dispari:
        somma = sum(nodi_dispari)
    nodi_pari = cerca_nodi_pari(root, profondità=0)
    somma_pari = 0
    for nodo in nodi_pari:
        somma_pari = sum(nodi_pari)
    return somma - somma_pari
    
    
def cerca_nodi_pari(root, profondità = 0):
    if root is None:
        return []
    nodi = []
    if profondità % 2 == 0:
        nodi.append(root.value)
    nodi += cerca_nodi_pari(root.left, profondità+1)
    nodi += cerca_nodi_pari(root.right, profondità+1)
    return nodi
    
def cerca_nodi_dispari(root, profondità = 0):
    if root is None:
        return []
    nodi = []
    if not profondità % 2 == 0:
        nodi.append(root.value)
    nodi += cerca_nodi_dispari(root.left, profondità+1)
    nodi += cerca_nodi_dispari(root.right, profondità+1)
    return nodi
    pass

# root = tree.BinaryTree.fromList([5, [8, None, [3, None, None]], [2, [9, None, None],[1, None, None]]])
# print(ex2(root))

###################################################################################
if __name__ == '__main__':
    # Place your tests here
    print('*' * 50)
    print('ITA\nEseguire grade.py per effettuare il debug con grader incorporato.')
    print('Altrimenti, inserire codice qui per verificare le funzioni con test propri')
    print('*' * 50)
    print('ENG\nRun grade.py to debug the code with the automatic grader.')
    print('Alternatively, insert here the code to check the functions with custom test inputs')
    print('*' * 50)
