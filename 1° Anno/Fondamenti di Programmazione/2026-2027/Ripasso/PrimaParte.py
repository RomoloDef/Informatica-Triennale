## Primo argomento di Fondamenti di Programmazione

"""
Prima di passare agli argomenti della prima macro-cateoria del corso, facciamo un excursus sulle tipologie di
di dato in Python
"""

a1 = 5      # questo è un tipo di dato intero

a2 = 5.0    # questo è un tipo di dato float

a3 = True   # questo è un tipo di dato booleano - assume solo True o False, solo 1 o 0, solo Vero o Falso

a4 = "Ciao, sono Romolo"    # questo è un tipo di dato strina - si usa per inserire del testo in una variabile

"""
Per capire che tipo di si sta trattando, si può utilizzare il costrutto type()
Per esempio:
"""

print(type(a1))

"""
Possiamo eseguire operazioni aritmetiche (più, meno, per, diviso, modulo, elevamento a potenza) sui diversi tipi di dato
"""

numero1 = 4
numero2 = 5
numero3 = 6

print(numero1 + numero2)  # 9
print(numero1 - numero2)  # -1
print(numero1 * numero2)  # 20
print(numero1 / numero2)  # 0.8
print(numero1 % numero2)  # 4
print(numero1 ** numero2) # 1024

"""
Allo stesso modo possiamo eseguire operazioni di confronto
"""

x = 7
y = 8

print(x == y) # x è uguale a y? (False)
print(x != y) # x è diverso da y? (True)
print(x < y)  # x è minore di y? (True)
print(x > y)  # x è maggiore di y? (False)
print(x <= y) # x è minore o uguale a y? (True)
print(x >= y) # x è maggiore o uguale a y? (False)

"""
E infine possiamo eseguire operazioni logiche sui diversi tipi di dato
"""

print(x > y and x < y)  # x è maggiore di y E x è minore di y? (False)
print(x > y or x < y)   # x è maggiore di y OPPURE x è minore di y? (True)
print(not(x > y))       # non è vero che x è maggiore di y? (True)


"""
Gli operatori di confronto e le operazioni loiche in particolare, 
sono il ponte per il primo costrutto fondamentale della programmazione: IF

IF è una struttura condizionale che permette di eseguire un blocco di codice 
solo se una determinata condizione booleana è vera (True).
"""

# ---- IF ----

if x < y:
    print("x è minore di y")    

# Nel caso in cui si volesse cercare un caso in cui la condizione sia falsa, si usa il costrutto ELSE

if x > y:
    print("maggiore")
else:
    print("minore")

# Esiste anche una terza via, ossia il costrutto ELIF, che sta per else if, unisce le due cose in un'unica struttura logica

if x > y:
    print("maggiore")
elif x == y:
    print("uguale")
else:
    print("minore")


"""
Prima di affrontare i costrutti iterativi come For e While, introduco velocemente le collezioni di dati: 
    1. Insiemi - elementi disordinati e non ripetuti
    2. Liste - elementi ordinati e ripetuti
    3. Tuple - elementi ordinati e non ripetuti
    4. Dizionari - elementi associati a una chiave
"""

Insieme = {1, 2, 3, 4, 5}  # insieme non ordinato e non ripetuto
print(Insieme)

Lista = [1, 2, 3, 4, 5]  # lista ordinata e ripetuta
print(Lista)

Tupla = (1, 2, 3, 4, 5)  # tupla ordinata e non ripetuta
print(Tupla)

Dizionario = {1: "Uno", 2: "Due", 3: "Tre", 4: "Quattro", 5: "Cinque"}  # dizionario associato a una chiave
print(Dizionario)

"""
Visti rapidamente come sono fatte le collezioni di dati (li vedremo nel dettaglio più avanti), si può passare
ai costrutti iterativi:

    1. Costrutto While
       Il ciclo while esegue ripetutamente un blocco di codice finché una determinata condizione 
       booleana rimane vera (True). È un ciclo indefinito, in quanto non si conosce a priori quante volte 
       verrà eseguito; l'iterazione si interrompe solo quando la condizione diventa falsa.

    2. Costrutto For
       Il ciclo for in Python viene utilizzato per iterare sugli elementi di una sequenza (come una lista, 
       una tupla, una stringa o un dizionario). È un ciclo definito, il che significa che il numero di 
       iterazioni è noto a priori (corrisponde al numero di elementi della sequenza da scorrere).


"""

# ---- WHILE ----

# Indice che ci servirà per scorrere gli elementi della lista tramite ciclo while

indice = 0

# Mentre l'indice è minore della lunghezza della lista

while indice < 4:
    print(indice)
    indice += 1         # Equivale a scrive indice = indice + 1

# Se non viene modificato l'indice, il ciclo diventa infinito, quindi bisogna fare attenzione a non commettere errori

# In questo contesto viene anche usato il costrutto break nel caso in cui si vuol far terminare il ciclo in anticipo

indice = 0
while indice <= 4:
    print("ciao")
    if indice == 2:
        break
    indice += 1 

# Un altro costrutto importante per il ciclo while è il continue

indice = 0
while indice < 4:
    indice += 1   
    if indice == 2:
        continue
    print(indice)

# Infine possiamo usare il costrutto else (comune con l'IF) quando la condizione del while diventa falsa (cioè quando il ciclo si conclude)

indice = 0
while indice <= 3:
    print(indice)
    indice += 1
else:
    print("Basta!")


# ---- FOR ----

listaCittà = ["Roma", "Milano", "Pescara"]
esempioStringa = "Hamburger"

# Iterando in una collezione di dati (come in questo caso una lista) si ottiene 
# la possibilità di stampare ogni elemento della collezione

for città in listaCittà: 
    print(città)

# Iterando in una strina invece, si stampa ogni indice della stringa (che corrisponde con la lettera in una determinata posizione)

for lettera in esempioStringa:
    print(lettera)

# Una variante è quella dei cicli annidati

listaNome1 = ["Romolo", "Fred"]
listaNome2 = ["Pippo", "Paperino"]

for nome in listaNome1:
    for nome2 in listaNome2:
        print(nome, nome2)

"""
Ora che sappiamo come trattare le variabili e utilizzare i costrutti if, while e for, 
possiamo passare allo studio delle stringhe in modo più approfondito.
Le stringhe sono collezioni di caratteri, quindi possiamo utilizzare i costrutti iterativi 
su di esse, ma possiamo fare anche altre operazioni specifiche.
"""

# ---- STRINGHE E SLICING ----

Stringa = "Paperino"

# Essendo considerate una lista di caratteri, si può iterare sui caratteri o fare quello che viene chiamato SLICING
# Per esempio:

for lettera in Stringa:
    if lettera in "aeiou":
        print(lettera)

# La lunghezza della stringa può essere trovata in due modi:

lunghezza = len(Stringa)

# SLICING: posso prendere un pezzetto di stringa (slice)

print(Stringa[0])

# Oppure prendere un range di lettere in una stringa

print(Stringa[1:4])     # Si prendono i caratteri esclusi quelli dall'indice superiore in poi

# Gli indici negativi nella stringa e lo slicing inverso

print(Stringa[-1])      # Prende l'ultimo carattere della stringa
print(Stringa[::-1])    # Inverte la stringa

# Oppure prendere gli ultimi x caratteri

print(Stringa[-3:])

# costrutto ord ci permette di vedere a quale numero ASCII corrisponde ogni lettera

print(f"Il valore ASCII di {Stringa[0]} è {ord(Stringa[0])}")

# oppure al contrario, tramite il codice ASCII, si può risalire alla lettera

print(f"La lettera corrispondente al codice ASCII {ord(Stringa[0])} è {chr(ord(Stringa[0]))}")

# Concatenazione di due stringhe

Stringa2 = "Questo è il primo argomento" + " di Python"
print(Stringa2) 

"""
Di seguito vediamo i metodi fondamentali per modificare le stringhe:
    1. upper() - rende maiuscola la stringa
    2. lower() - rende minuscola la stringa
    3. strip() - elimina gli spazi bianchi all'inizio e alla fine della stringa
    4. replace() - sostituisce una sottostringa con un'altra sottostringa
    5. split() - divide la stringa in una lista di sottostringhe
    6. count() - conta il numero di occorrenze di una sottostringa
Questi sono solo alcuni metodi, ce ne sono molti altri per molte altre funzioni. 
"""

# Esempi pratici

stringa_esempi = "   Benvenuti al corso di Python!   "

# 1. upper()
print(f"upper(): {stringa_esempi.upper()}")

# 2. lower()
print(f"lower(): {stringa_esempi.lower()}")

# 3. strip()
stringa_pulita = stringa_esempi.strip()
print(f"strip(): '{stringa_pulita}'")

# 4. replace()
print(f"replace(): {stringa_pulita.replace('Python', 'Programmazione')}")

# 5. split()
print(f"split(): {stringa_pulita.split(' ')}")

# 6. count()
print(f"count('o'): {stringa_pulita.count('o')}")

"""
Analizzate le stringhe possiamo passare finalmente alle strutture dati fondamentali in Python:
"""

# --- LISTE ----

"""
Le liste sono collezioni di dati che possono contenere elementi di qualsiasi tipo. 
Le liste sono ordinate e modificabili, il che significa che è possibile aggiungere, rimuovere o modificare gli elementi in qualsiasi momento. 
Inoltre, le liste possono contenere duplicati, il che significa che è possibile avere più elementi uguali all'interno della stessa lista.
"""

esempioLista = [0, 1, 2, 3, 4, 5, "Romolo"]

# Posso creare una lista o convertire un'altra struttura dati in lista tramite il metodo list()

secondaLista = list(("ciao", "sono", "romolo"))

# Essendo una struttura dati modificabile, posso apportare modifiche accedendo tramite gli indici

print(secondaLista[0])

# Ora voglio cambiare e inserire un altro elemento nella prima posizione

secondaLista[0] = "Pippo"
print(secondaLista)

# Lo stesso discorso vale per più elementi utilizzando lo slicing

secondaLista[1:3] = ["sono", "fred"]
print(secondaLista)

"""
Vediamo ora i metodi più usati per modificare le liste (gli altri li vedremo più avanti):

    1. append() - aggiunge un elemento alla fine della lista
    2. remove() - rimuove un elemento dalla lista
    3. pop() - rimuove un elemento dalla lista tramite indice
    4. insert() - inserisce un elemento nella lista in una posizione specifica
    5. sort() - ordina la lista
    6. reverse() - inverte la lista

Questi sono solo alcuni metodi, ce ne sono molti altri per molte altre funzioni. 
"""

# Esempi di questi metodi 

lista = ["roma", "napoli", "milano"]

# 1. append()
lista.append("torino")
print(lista)

# 2. insert()
lista.insert(1, "firenze")
print(lista)

# 3. extend()
y = ["bologna", "verona"]
lista.extend(y)
print(lista)

# 4. remove()
lista.remove("napoli")
print(lista)

# 5. pop()
lista.pop(2)     # se non si inserisce un indice rimuove l'ultimo elemento
print(lista)

# 6. del()
del lista[1]
print(lista)

# 7. clear()
lista.clear()
print(lista)    # lista vuota

"""
Avendo più liste può interessare anche l'unione di esse, che può avvenire in più modi:
    1. Inserendo una lista in un'altra lista (diventando due liste annidate)
    2. Unendo due liste tramite l'operatore + 
    3. Estendendo un lista con un'altra lista (extend)
"""

lista1 = ["roma", "napoli", "milano"]
lista2 = ["torino", "firenze", "bologna"]

# Unione tramite operatore + 
print(lista1 + lista2)

# Unione tramite append
for città in lista2:
    lista1.append(città)
print(lista1)

# Unione tramite extend
lista1.extend(lista2)

"""
Di fondamentale importanza per le strutture dati, specialmente per le liste, è l'ordinamento ma lo vedremo più in basso
"""

# --- INSIEMI (SET) ---

"""
Gli insiemi (set) sono collezioni di elementi unici e non ordinati. 
Ciò significa che non è possibile avere elementi duplicati all'interno di un insieme, 
e gli elementi non hanno una posizione specifica (non è possibile accedervi tramite indice).
"""

# Per creare un insieme bisogna usare le parentesi graffe o, in alternativa, il costrutto set()

esempioInsieme1 = {1, 2, 3, 4, 5}

esempioInsieme2 = set([2, 3, 6, 8])

# Come per le liste anche per gli insiemi possiamo trovare la lunghezza
print(len(esempioInsieme1))

"""
Per accedere agli elementi di un insieme, non essendo indicizzati, l'unico modo per farlo 
è quello di scorrere tutto l'insieme tramite un ciclo for (ma se ci interessa solo uno o pochi elementi 
potremmo scorrere gli elementi di un'altra struttura dati che però contiene al suo interno gli elementi dell'insieme)
"""

esempioInsieme3 = {1, 4, 5, 9, 3, 2}

for elemento in esempioInsieme3:
    print(elemento)

"""
Anche gli insiemi hanno vari metodi tra cui:

    1. add() - aggiunge un elemento all'insieme
    2. update() - aggiorna l'insieme con elementi da un'altra struttura dati
    3. remove() - rimuove un elemento dall'insieme
    4. discard() - rimuove un elemento dall'insieme
    5. pop() - rimuove un elemento dall'insieme tramite indice
    6. clear() - svuota l'insieme
    7. del() - elimina l'insieme

Questi sono solo alcuni metodi, ce ne sono molti altri per molte altre funzioni. 
"""

# Esempi di questi metodi 

insieme = {10, 4, 5, 9, 3, 2}

# 1. add() - aggiunge un elemento all'insieme

insieme.add(6)
print(insieme)

# 2. update() - aggiorna l'insieme con elementi da un'altra struttura dati

insieme.update([7, 8, 9, 10])
print(insieme)

# 3. remove() - rimuove un elemento dall'insieme

insieme.remove(7)
print(insieme)

# 4. discard() - rimuove un elemento dall'insieme

insieme.discard(8)
print(insieme)

# 5. pop() - rimuove un elemento dall'insieme tramite indice

insieme.pop()
print(insieme)

# 6. clear() - svuota l'insieme

insieme.clear()
print(insieme)

# 7. del() - elimina l'insieme

del insieme
# print(insieme) - viene mostrato NameError perché non più definito

"""
Oltre a questi metodi "classici", gli insiemi, essendo delle strutture matematiche, presentano dei metodi
che corrispondono alle operazioni insiemistiche:

    1. union() - restituisce l'unione di due insiemi
    2. intersection() - restituisce l'intersezione di due insiemi
    3. difference() - restituisce la differenza tra due insiemi
    4. symmetric_difference() - restituisce la differenza simmetrica tra due insiemi
    5. symmetric_difference_update() - aggiorna l'insieme con la differenza simmetrica tra due insiemi

"""

# Esempi di questi metodi 

insieme1 = {1, 2, 3, 4, 5}
insieme2 = {4, 5, 6, 7, 8}

# 1. union() - unione
unione = insieme1.union(insieme2)
print(f"Unione: {unione}")

# 2. intersection() - intersezione
intersezione = insieme1.intersection(insieme2)
print(f"Intersezione: {intersezione}")

# 3. difference() - differenza
differenza = insieme1.difference(insieme2)
print(f"Differenza (insieme1 - insieme2): {differenza}")

# 4. symmetric_difference() - differenza simmetrica
diff_simmetrica = insieme1.symmetric_difference(insieme2)
print(f"Differenza simmetrica: {diff_simmetrica}")

# 5. symmetric_difference_update() - aggiorna l'insieme con la differenza simmetrica
insieme1.symmetric_difference_update(insieme2)
print(f"Insieme1 dopo symmetric_difference_update: {insieme1}")

# ---- TUPLE ----

"""
Le tuple sono collezioni di dati ordinate e immutabili.
Ciò significa che non è possibile modificare gli elementi di una tupla.

La sintassi è la medesima delle liste, ma si usano le parentesi tonde () invece delle quadre [].
"""

tupla = (1, 2, 3, 4, 5)

# possiamo crearne una anche con il metodo tuple()

tupla2 = tuple([1, 2, 3, 4, 5])

# Questo tipo di struttura dati come anticipato non permette modifiche ma ci può essere l'accesso tramite indici

print(tupla[0])

# Per poterle modificare, bisogna usare un'escamotage: trasformarle in liste con il metodo list(), modificarle e poi riconvertirle in tuple

tupla3 = ("roma", "milano", "chieti")
print(f"Tupla originale: {tupla3}")

tupla_trasformata = list(tupla3)

# Ora modifico un valore della nuova lista
tupla_trasformata[2] = "pescara"
tupla_corretta = tuple(tupla_trasformata)
print(f"Tupla corretta: {tupla_corretta}") 

"""
I metodi he ci interessano per le tuple sono gli stessi delle liste tranne quelli che modificano la tupla:
    1. count() - restituisce il numero di occorrenze di un elemento
    2. index() - restituisce l'indice di un elemento
"""

# Esempi di questi metodi 

tupla = (1, 2, 3, 4, 5, 2, 3, 3, 1, 2)

# 1. count() - conta le occorrenze di un elemento
print(f"L'elemento 2 compare {tupla.count(2)} volte")

# 2. index() - restituisce l'indice di un elemento
print(f"L'indice dell'elemento 3 è {tupla.index(3)}")

# ---- DIZIONARI ----

"""
I dizionari sono una struttura dati in cui vi è un'associazione 
di due elementi, chiamati chiave (key) e valore (value). 
La sintassi è la medesima degli insiemi, ma si usano le parentesi graffe {}, 
ma si usa i due punti : per separare la chiave dal valore.
"""

# Esempio di dizionario
persona = {
    "nome" : "Luca",
    "cognome" : "Rossi",
    "età" : 25
}

# --- Accedere agli elementi ---

# tramite la chiave
print(f"Cognome: {persona['cognome']}")

# get() - metodo per accedere agli elementi in modo sicuro
print(f"Nome con get: {persona.get('nome')}")

# keys() - restituisce tutte le chiavi
chiavi = persona.keys()
print(f"Chiavi: {chiavi}")    # crea un oggetto dict_keys, simile a una lista con tutte le chiavi

# values() - restituisce tutti i valori
valori = persona.values()
print(f"Valori: {valori}")    # crea un oggetto dict_values, simile a una lista con tutti i valori

# items() - restituisce tutte le coppie chiave-valore
elementi = persona.items()
print(f"Items: {elementi}")    # crea un oggetto dict_items, simile a una lista di tuple con tutte le coppie

# vedere se una chiave è presente nel dizionario
print(f"La chiave 'nome' è presente? {'nome' in persona}")

# --- Modificare gli elementi ---

# Modifica diretta tramite chiave
persona["nome"] = "Marco"
print(f"Dopo modifica diretta: {persona}")

# update() - modifica o aggiunge uno o più elementi
persona.update({"nome": "Luca", "età": 26})
print(f"Dopo update(): {persona}")

# --- Aggiungere gli elementi ---

# Aggiunta diretta tramite nuova chiave
persona["colore"] = "blu"
print(f"Dopo aggiunta diretta: {persona}")

# update() - aggiungere più elementi contemporaneamente
persona.update({"sesso": "maschio", "occhi": "verdi"})
print(f"Dopo aggiunta multipla con update(): {persona}")

# --- Rimuovere gli elementi ---

# pop() - rimuove un elemento specificando la chiave e ne restituisce il valore
occhi = persona.pop("occhi")
print(f"Dopo pop('occhi'): {persona} (valore rimosso: {occhi})")

# popitem() - rimuove e restituisce l'ultimo elemento inserito (coppia chiave-valore)
ultimo = persona.popitem()
print(f"Dopo popitem(): {persona} (elemento rimosso: {ultimo})")

# del - elimina un elemento specifico
del persona["colore"]
print(f"Dopo del persona['colore']: {persona}")

# clear() - svuota completamente il dizionario
persona.clear()
print(f"Dopo clear(): {persona}")

# --- Ciclare gli elementi (Iterazione) ---
persona = {
    "nome": "Luca",
    "cognome": "Rossi",
    "età": 25
}

# Stampa solo le chiavi (default)
print("\nIterazione per chiavi:")
for x in persona:
    print(x)
    
# Stampa le chiavi esplicitamente con keys()
print("\nIterazione con keys():")
for x in persona.keys():
    print(x) 
    
# Stampa i valori usando la chiave
print("\nIterazione valori (tramite chiave):")
for x in persona:
    print(persona[x])

# Stampa i valori esplicitamente con values()
print("\nIterazione con values():")
for x in persona.values():
    print(x)
    
# Stampa sia chiavi che valori con items()
print("\nIterazione con items():")
for k, v in persona.items():
    print(f"{k}: {v}")
    
# --- Copiare un dizionario ---
# Metodo 1: copy()
persona_copia1 = persona.copy()

# Metodo 2: costruttore dict()
persona_copia2 = dict(persona)

# --- Dizionari annidati ---
# I dizionari possono contenere altri dizionari al loro interno
persona_completa = {
    "nome": "Luca",
    "cognome": "Rossi",
    "età": 25,
    "indirizzo": {
        "citta": "Roma",
        "civico": 12
    }
}
print(f"\nDizionario annidato: {persona_completa}")
print(f"Città: {persona_completa['indirizzo']['citta']}")

# --- Altre operazioni utili ---

# setdefault() - restituisce il valore di una chiave. Se non esiste, la crea
professione = persona.setdefault("professione", "Studente")
print(f"\nDopo setdefault('professione'): {persona}")

# fromkeys() - crea un nuovo dizionario partendo da una sequenza di chiavi
chiavi_nuove = ["a", "b", "c"]
valore_default = 0
nuovo_diz = dict.fromkeys(chiavi_nuove, valore_default)
print(f"Dizionario creato con fromkeys(): {nuovo_diz}")








