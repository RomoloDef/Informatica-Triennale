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
    la funzione ex1( deve restituire l'insieme
    {'ab', 'ba', 'ac', 'ca', 'bc', 'cb'}
"""

def ex1(a_set, n):
    if n == 0:
        return {''}  
    
    risultato = set()
    a_list = list(a_set)
    
    for i in range(len(a_list)):
        c = a_list[i]
        resto = a_list[:i] + a_list[i+1:]  # rimuovo il carattere
        sottostringhe = ex1(resto, n-1)
        for s in sottostringhe:
            risultato.add(c + s)  # concateno
    
    return risultato

# Test
# print(ex1({'a','b','c'}, 2))
# Output: {'ab', 'ac', 'ba', 'bc', 'ca', 'cb'}

# %% ------------------------------------------------------------ #

"""
Ex2: 7 punti

Si definisca la funzione ex2(alphabet), ricorsiva o che utilizza
funzioni o metodi ricorsivi, che prende in ingresso una stringa
"alphabet" e restituisce un set.  La stringa alphabet può contenere
caratteri maiuscoli e minuscoli oppure tutti in un solo stile (tutto
maiuscolo, o tutto minuscolo). La funzione deve generare tutte le
possibili parole che si possono creare combinando i caratteri di
"alphabet" usando le segueni regole:
  1. una volta che un carattere è stato usato non si può più utilizzare
  (come nelle permutazioni)
  2. un carattere maiuscolo deve essere seguito da un carattere minuscolo
  e viceversa. Questo vuol dire che NON si possono concatenare due caratteri
  tipo maiuscolo maiuscolo oppure minuscolo e minuscolo. 

Se alfabet='icA' si deve generare il set:
{'i', 'Ai', 'cAi', 'iAc', 'Ac', 'cA', 'c', 'A', 'iA'}
"""

def ex2(alphabet):
    if not alphabet:
        return {""}
    
    risultato = set()
    for i, c in enumerate(alphabet):
        resto = alphabet[:i] + alphabet[i+1:]
        for sottostringa in ex2(resto):
            if not sottostringa or c.isupper() != sottostringa[0].isupper():
                risultato.add(c + sottostringa)
        risultato.add(c)
    return risultato

# print(ex2('icA'))

# %% ------------------------------------------------------------ #

"""
Ex3: 6 punti

Si definisca la funzione ex1(n, faces), ricorsiva o che usa un metodo
ricorsivo, che prende in ingresso due interi, n e faces.

La funzione deve restituire una lista con tutti i possibili esiti del
lancio di 'n' dadi, ognuno con 'faces' facce. Ogni esito è rappresentato
da una tupla con 'n' elementi, un elemento per ogni dado.
La lista restituita deve essere ordinata in ordine crescente.

Esempio:
    ex1(2, 3) deve restituire la lista
    [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]
"""

def ex3(n, faces):
    
    pass

# %% ------------------------------------------------------------ #

"""
Ex4: 6 punti

Si definisca la funzione ex1(L), ricorsiva o che utilizza funzioni o
metodi ricorsivi,che, data una lista di N liste di M caratteri
ciascuna, costruisce e restituisce la lista di tutte le possibili
stringhe di N caratteri ottenute concatenando un carattere della prima
lista, un altro della seconda, uno della terza e così via.

Ad esempio, se la lista di input è: [['c', 'q', 'a'], ['w', 'e', 'y']],
la funzione restituisce: ['ae', 'aw', 'ay', 'ce', 'cw', 'cy', 'qe', 'qw', 'qy'].
La lista ritornata deve essere ordinata in ordine alfabetico.

"""

def ex4(L):
    if not L:
        return ['']
    else:
        risultato = []
        prima_sottolista = L[0]
        resto = L[1:]
        combinazioni = ex4(resto)
        for c in (prima_sottolista):
            for comb in combinazioni:
                risultato.append(c + comb)
    ordinamento = lambda parola: parola
    return sorted(risultato, key = ordinamento)
    pass

L = [['c', 'q', 'a'], ['w', 'e', 'y']]
print(ex4(L))

# %% ------------------------------------------------------------ #

"""
Ex5: 3+3 punti
Definisci una funzione ricorsiva (o una che utilizza funzioni ricorsive)
ex2(strings, n) che prende un insieme 'strings' e un intero 'n' e
genera ricorsivamente tutte le possibili stringhe che possono essere
costruite concatenando n stringhe dell'insieme strings. La funzione deve
restituire tutte le stringhe costruite. La funzione può restituire
un insieme con tutte le stringhe costruite (3 punti), oppure una lista
ordinata (6 punti). La lista è ordinata considerando l'ordine decrescente
della lunghezza delle stringhe e, in caso di parità, considerando l'ordine
alfabetico.

Esempio: se strings={'a','b','c','de'}, la funzione ex5(strings, 2)
restituisce l'insieme {'ab','ac','ade','ba','ca','dea','bc','bde','cb','deb','cde','dec'} (3 punti)
oppure la lista ['ade', 'bde', 'cde', 'dea', 'deb', 'dec', 'ab', 'ac', 'ba', 'bc', 'ca', 'cb'] (6 punti)
"""

def ex5(strings, n):
    pass