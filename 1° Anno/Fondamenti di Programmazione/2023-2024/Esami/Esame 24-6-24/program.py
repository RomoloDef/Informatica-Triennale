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
'''func1: 2 punti

Si definisca la funzione func1(L) che prende in input un elenco di
liste di caratteri.  La funzione restituisce l'elenco di caratteri che
non si ripetono all'interno di ciascuna lista interna.

Ad esempio, data la lista L = [['e', 'a', 'e'], ['b', 'c'], ['c', 'd', 'd']]
la funzione restituisce la lista ['a', 'b', 'c', 'c']
poiché 'a' non si ripete nella lista ['e', 'a', 'e'].
'b' e 'c' non si ripetono nella lista ['b', 'c']
e 'c' non si ripete nella lista ['c', 'd', 'd'].

'''
def func1(L):
    lista_finale = []
    for lista in L:
        for carattere in lista:
            if lista.count(carattere) == 1:
                lista_finale.append(carattere)
    return (lista_finale)
    pass

# L = [['e', 'a', 'e'], ['b', 'c'], ['c', 'd', 'd']]
# print(func1(L))
# L = [['a', 'b', 'b', 'b', 'a'], ['z', 'y', 'x', 'w', 'v'], ['a']]
# print(func1(L))
# L = [['a', 'a', 'b', 'b', 'c', 'a', 'b', 'c', 'd']]
# print(func1(L))
# L = [['a', 'b', 'c', 'a', 'b', 'c'], ['z', 'y', 'x', 'x', 'z', 'y'], ['a', 'b', 'a', 'b'], ['z', 'z']]
# print(func1(L))

# %% ----------------------------------- FUNC2 ------------------------- #
''' func2: 2 punti

Si definisca la funzione func2(L0, L1) che riceve 2 liste L0 e L1.
La prima lista L0 contiene stringhe S0, S1, ... Sn-1, la seconda lista
L1 contiene numeri interi positivi I0, I1, ... In-1.
La funzione restituisce una stringa ottenuta concatenando ogni stringa
Sj ripetuta Ij volte.

Ad esempio, se L0 = ['ab', 'o o'] e L1 = [2, 3] la funzione restituisce:
'ababo oo oo o'.
'''
def func2(L0, L1):
    stringa = ""
    for i in range(len(L0)):
        stringa += L0[i] * L1[i]
    return stringa
        
    pass

# L0 = ['ab', 'o o']
# L1 = [2, 3]
# print(func2(L0, L1))
# L0 = ['quick', 'brow', 'fox']
# L1 = [2, 0, 2]
# print(func2(L0, L1))
# L0 = ['h', 'e', 'l', 'o']
# L1 = [1, 1, 2, 1]
# print(func2(L0, L1))
# L0 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
# L1 = [0, 1, 2, 3, 4, 5, 6, 7, 8]
# print(func2(L0, L1))

# %% ----------------------------------- FUNC3 ------------------------- #
'''  func3: 4 punti

Si definisca la funzione func3(file_in) che legge un file di testo.
Il file contiene numeri interi separati da spazi (multipli) e su righe
diverse.  La funzione restituisce la somma dei numeri sulle righe pari
meno la somma dei numeri sulle righe dispari. La prima riga del file è
la riga 0, quindi è una riga pari; la seconda riga è la riga 1, quindi
è dispari, e così via.

Ad esempio, se il file contiene:
   4 1 2 -3
0 1 -2         
       10
 -5 6

la funzione restituisce 14, poiché 14=(4+1+2-3+10)-(0+1-2-5+6)
'''

def func3(file_in):
    with open(file_in, 'r', encoding = 'utf-8') as file:
        somma_pari = 0
        somma_dispari = 0
        for i, riga in enumerate(file):
            if i % 2 == 0:
                somma_pari += sum(map(int, riga.split()))
            else:
                somma_dispari += sum(map(int, riga.split()))
    return somma_pari - somma_dispari

    pass
# print(func3("func3/in1.txt"))
# print(func3("func3/in2.txt"))
# print(func3("func3/in3.txt"))
# print(func3("func3/in4.txt"))

# %% ----------------------------------- FUNC4 ------------------------- #
""" func4: 2 punti

Si definisca la funzione func4(D) che riceve in ingresso un
dizionario, in cui ogni chiave è una stringa e il valore
corrispondente è una collezione (un insieme, un dizionario, una lista,
...).
La funzione restituisce un elenco di liste, in cui ogni sottoelenco S
corrisponde a un elemento del dizionario in ingresso e contiene quanto
segue: - come primo elemento I0, la chiave dell'elemento del
dizionario corrispondente - come secondo elemento I1, il valore
dell'elemento del dizionario corrispondente.
Le liste interne sono ordinate in base alla lunghezza del secondo
elemento I1 in ogni lista interna, in ordine inverso (dalla più lunga
alla più corta).  Se le due liste interne hanno un secondo elemento
con la stessa lunghezza, vengono ordinati in base al valore del primo
elemento I0 (in ordine alfabetico o numerico).

Ad esempio, se D = {"f":(1, 2, 3), "a":["h", "w"], "c":{"f":3, "g":[1,2]}}
la funzione restituisce: [["f", (1, 2, 3)], ["a", ["h", "w"]], ["c", {"f":3, "g":[1,2]}]].
"""

def func4(D):

    pass
# D = {"f":(1, 2, 3), "a":["h", "w"], "c":{"f":3, "g":[1,2]}}
# print(func4(D))
# D = {3: {'name': 'Steve', 'age': 25, 'marks': 60}, 2: {'name': 'Anil', 'age': 23, 'marks': 75}, 1: {'name': 'Asha', 'age': 20, 'marks': 70}}
# print(func4(D))
# D = {'hp': {'name': ' Folio Elitebook 9470M', 'brand': 'HewlettPackard Laptop', 'price':30000},
#             'lenovo': {'name': 'Camera 8989', 'brand': 'Lenovo Laptop', 'price':40000},
#             'dell': {'name': 'Dell Inspiron', 'brand': 'Dell Laptop', 'price':200}}
# print(func4(D))
# cities = ["Aberdeen", "Abilene", "Akron", "Albany", "Albuquerque", "Alexandria", "Allentown", "Amarillo", "Anaheim", "Anchorage", "Ann Arbor", "Antioch", "Apple Valley", "Appleton", "Arlington", "Arvada", "Asheville", "Athens", "Atlanta", "Atlantic City", "Augusta", "Aurora", "Austin", "Bakersfield", "Baltimore", "Barnstable", "Baton Rouge", "Beaumont", "Bel Air", "Bellevue", "Berkeley", "Bethlehem", "Billings", "Birmingham", "Bloomington", "Boise", "Boise City", "Bonita Springs", "Boston", "Boulder", "Bradenton", "Bremerton", "Bridgeport", "Brighton", "Brownsville", "Bryan", "Buffalo", "Burbank", "Burlington", "Cambridge", "Canton", "Cape Coral", "Carrollton", "Cary", "Cathedral City", "Cedar Rapids", "Champaign", "Chandler", "Charleston", "Charlotte", "Chattanooga", "Chesapeake", "Chicago", "Chula Vista", "Cincinnati", "Clarke County", "Clarksville", "Clearwater", "Cleveland", "College Station", "Colorado Springs", "Columbia", "Columbus", "Concord", "Coral Springs", "Corona", "Corpus Christi", "Costa Mesa", "Dallas", "Daly City", "Danbury", "Davenport", "Davidson County", "Dayton", "Daytona Beach", "Deltona", "Denton", "Denver", "Des Moines", "Detroit", "Downey", "Duluth", "Durham", "El Monte", "El Paso", "Elizabeth", "Elk Grove", "Elkhart", "Erie", "Escondido", "Eugene", "Evansville", "Fairfield", "Fargo", "Fayetteville", "Fitchburg", "Flint", "Fontana", "Fort Collins", "Fort Lauderdale", "Fort Smith", "Fort Walton Beach", "Fort Wayne", "Fort Worth", "Frederick", "Fremont", "Fresno", "Fullerton", "Gainesville", "Garden Grove", "Garland", "Gastonia", "Gilbert", "Glendale", "Grand Prairie", "Grand Rapids", "Grayslake", "Green Bay", "GreenBay", "Greensboro", "Greenville", "Gulfport-Biloxi", "Hagerstown", "Hampton", "Harlingen", "Harrisburg", "Hartford", "Havre de Grace", "Hayward", "Hemet", "Henderson", "Hesperia", "Hialeah", "Hickory", "High Point", "Hollywood", "Honolulu", "Houma", "Houston", "Howell", "Huntington", "Huntington Beach", "Huntsville", "Independence", "Indianapolis", "Inglewood", "Irvine", "Irving", "Jackson", "Jacksonville", "Jefferson", "Jersey City", "Johnson City", "Joliet", "Kailua", "Kalamazoo", "Kaneohe", "Kansas City", "Kennewick", "Kenosha", "Killeen", "Kissimmee", "Knoxville", "Lacey", "Lafayette", "Lake Charles", "Lakeland", "Lakewood", "Lancaster", "Lansing", "Laredo", "Las Cruces", "Las Vegas", "Layton", "Leominster", "Lewisville", "Lexington", "Lincoln", "Little Rock", "Long Beach", "Lorain", "Los Angeles", "Louisville", "Lowell", "Lubbock", "Macon", "Madison", "Manchester", "Marina", "Marysville", "McAllen", "McHenry", "Medford", "Melbourne", "Memphis", "Merced", "Mesa", "Mesquite", "Miami", "Milwaukee", "Minneapolis", "Miramar", "Mission Viejo", "Mobile", "Modesto", "Monroe", "Monterey", "Montgomery", "Moreno Valley", "Murfreesboro", "Murrieta", "Muskegon", "Myrtle Beach", "Naperville", "Naples", "Nashua", "Nashville", "New Bedford", "New Haven", "New London", "New Orleans", "New York", "New York City", "Newark", "Newburgh", "Newport News", "Norfolk", "Normal", "Norman", "North Charleston", "North Las Vegas", "North Port", "Norwalk", "Norwich", "Oakland", "Ocala", "Oceanside", "Odessa", "Ogden", "Oklahoma City", "Olathe", "Olympia", "Omaha", "Ontario", "Orange", "Orem", "Orlando", "Overland Park", "Oxnard", "Palm Bay", "Palm Springs", "Palmdale", "Panama City", "Pasadena", "Paterson", "Pembroke Pines", "Pensacola", "Peoria", "Philadelphia", "Phoenix", "Pittsburgh", "Plano", "Pomona", "Pompano Beach", "Port Arthur", "Port Orange", "Port Saint Lucie", "Port St. Lucie", "Portland", "Portsmouth", "Poughkeepsie", "Providence", "Provo", "Pueblo", "Punta Gorda", "Racine", "Raleigh", "Rancho Cucamonga", "Reading", "Redding", "Reno", "Richland", "Richmond", "Richmond County", "Riverside", "Roanoke", "Rochester", "Rockford", "Roseville", "Round Lake Beach", "Sacramento", "Saginaw", "Saint Louis", "Saint Paul", "Saint Petersburg", "Salem", "Salinas", "Salt Lake City", "San Antonio", "San Bernardino", "San Buenaventura", "San Diego", "San Francisco", "San Jose", "Santa Ana", "Santa Barbara", "Santa Clara", "Santa Clarita", "Santa Cruz", "Santa Maria", "Santa Rosa", "Sarasota", "Savannah", "Scottsdale", "Scranton", "Seaside", "Seattle", "Sebastian", "Shreveport", "Simi Valley", "Sioux City", "Sioux Falls", "South Bend", "South Lyon", "Spartanburg", "Spokane", "Springdale", "Springfield", "St. Louis", "St. Paul", "St. Petersburg", "Stamford", "Sterling Heights", "Stockton", "Sunnyvale", "Syracuse", "Tacoma", "Tallahassee", "Tampa", "Temecula", "Tempe", "Thornton", "Thousand Oaks", "Toledo", "Topeka", "Torrance", "Trenton", "Tucson", "Tulsa", "Tuscaloosa", "Tyler", "Utica", "Vallejo", "Vancouver", "Vero Beach", "Victorville", "Virginia Beach", "Visalia", "Waco", "Warren", "Washington", "Waterbury", "Waterloo", "West Covina", "West Valley City", "Westminster", "Wichita", "Wilmington", "Winston", "Winter Haven", "Worcester", "Yakima", "Yonkers", "York", "Youngstown"]
# D = {char: {city for city in cities if city.startswith(char)} for char in 'ABCDEFGHIJKLMNOPRSTUVWY'}
# print(func4(D))

# %% ----------------------------------- FUNC5 ------------------------- #
""" func5: 8 punti

Si definisca la funzione func5(file_in, file_out) che legge il file
file_in contenente un'immagine, utilizzando la funzione load del
pacchetto images.
L'immagine è rappresentata come un elenco di liste di pixel, ogni
pixel è una tupla (r, g, b) e le liste interne rappresentano le righe
dell'immagine.
L'immagine ha uno sfondo nero e alcuni diamanti e X non neri disegnati
su di essa, secondo gli schemi seguenti (un meno rappresenta un pixel
nero e un asterisco rappresenta un pixel non nero):

            -*-
diamante =  *-*
            -*-


X =         *-*
            -*-
            *-*

Ogni diamante o X è tale che l'area 3x3 occupata dai suoi pixel è
distanziata di 1 pixel in ogni direzione, rispetto a ciascuno degli
altri diamanti e X dell'immagine.
Dopo aver letto l'immagine, la funzione trasforma tutti i diamanti in
X e viceversa, senza modificarne il colore (tutti i pixel di un
diamante o di una X hanno lo stesso colore).
Infine, la funzione salva l'immagine risultante nel file file_out
utilizzando la funzione save del pacchetto images e restituisce una
tupla (a, b), dove a è il numero di diamanti e b è il numero di X
nell'immagine di input.  """

import images

def func5(file_in, file_out):
    img = images.load(file_in)
    h, w = len(img), len(img[0])

    num_diamanti = 0
    num_x = 0

    # scorri tutti i possibili blocchi 3x3
    for y in range(h - 2):
        for x in range(w - 2):
            # estrai blocco 3x3
            blocco = [row[x:x+3] for row in img[y:y+3]]

            # il colore è quello del primo pixel non nero
            colore = None
            for riga in blocco:
                for pixel in riga:
                    if pixel != (0, 0, 0):
                        colore = pixel
                        break
                if colore:
                    break
            if not colore:
                continue  # solo nero → ignora

            # pattern diamante
            diamante = [
                [(0,0,0), colore, (0,0,0)],
                [colore, (0,0,0), colore],
                [(0,0,0), colore, (0,0,0)]
            ]

            # pattern X
            xshape = [
                [colore, (0,0,0), colore],
                [(0,0,0), colore, (0,0,0)],
                [colore, (0,0,0), colore]
            ]

            if blocco == diamante:
                num_diamanti += 1
                # trasformalo in X
                for dy in range(3):
                    for dx in range(3):
                        img[y+dy][x+dx] = xshape[dy][dx]
            elif blocco == xshape:
                num_x += 1
                # trasformalo in diamante
                for dy in range(3):
                    for dx in range(3):
                        img[y+dy][x+dx] = diamante[dy][dx]

    images.save(img, file_out)
    return (num_diamanti, num_x)

print(func5("func5/img0_in.png", "func5/img0_out.png"))
# print(func5("func5/img1_in.png", "func5/img1_out.png"))
# print(func5("func5/img2_in.png", "func5/img2_out.png"))
# print(func5("func5/img3_in.png", "func5/img3_out.png"))


# %% ----------------------------------- EX.1 ------------------------- #
"""
Ex1: 6 punti

Si definisca la funzione ex1(L), ricorsiva o che utilizza funzioni o
metodi ricorsivi,che, data una lista di N liste di M caratteri
ciascuna, costruisce e restituisce la lista di tutte le possibili
stringhe di N caratteri ottenute concatenando un carattere della prima
lista, un altro della seconda, uno della terza e così via.

Ad esempio, se la lista di input è: [['c', 'q', 'a'], ['w', 'e', 'y']],
la funzione restituisce: ['ae', 'aw', 'ay', 'ce', 'cw', 'cy', 'qe', 'qw', 'qy'].
La lista ritornata deve essere ordinata in ordine alfabetico.

"""

def ex1(L):
    if L == []:
        return ['']
    else:
        risultato = []
        resto = ex1(L[1:])
        for c in L[0]:
            for r in resto:
                risultato.append(c + r)
    return sorted(risultato)
            
    pass

L = [['c', 'q', 'a'], ['w', 'e', 'y']]
print(ex1(L))
# L = [['0', '1'], ['0', '1'], ['0', '1'], ['0', '1']]
# print(ex1(L))
# L = [['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']]
# print(ex1(L))
# L = [['0', '1', '2'], ['a', 'b', 'c'], ['0', '1', '2'], ['x', 'y', 'z']]
# print(ex1(L))

# %% ----------------------------------- EX.1 ------------------------- #
"""
Ex2: 8 punti

Si definisca la funzione ex2(root), ricorsiva o che utilizza funzioni
o metodi ricorsivi, che prenda in input un albero binario e lo
modifichi (in-place) aggiungendo ricorsivamente a ogni nodo i valori
dei suoi nodi figli (se presenti).
La somma deve essere fatta dal basso verso l'alto, cioè le foglie
saranno aggiunte ai loro nodi genitori, e così via, fino a raggiungere
la radice.
La funzione restituisce una coppia che rappresenta il numero di valori
pari e dispari nell'albero originale.

Ad esempio, se l'albero di input è:

               1
              / \
             2   3
            /   / \
           4   5   6
              /
             7
L'albero modificato sarà:
               28
              /  \
             6    21
            /    / \
           4    12  6
               /
              7
e la funzione restituirà (4, 3).
"""

import tree

def ex2(root):
    pari, dispari = conto_pari_dispari(root)
    somma_albero(root)
    return (dispari, pari)
    pass

def conto_pari_dispari(root):
    if root is None:
        return (0,0)
    else:
        pari = 0
        dispari = 0
        if root.value % 2 == 0:
            pari += 1
        else:
            dispari += 1
        pari_sx, dispari_sx = conto_pari_dispari(root.left)
        pari_dx, dispari_dx = conto_pari_dispari(root.right)
    return (pari + pari_sx + pari_dx, dispari + dispari_sx + dispari_dx)


def somma_albero(root):
    if root is None:
        return 0
    somma_sx = somma_albero(root.left)
    somma_dx = somma_albero(root.right)
    root.value += somma_sx + somma_dx
    return root.value

                

    
# %% 
###################################################################################
if __name__ == '__main__':
    # Scrivi qui i tuoi test
    print('*'*50)
    print('Devi eseguire il grade.py se vuoi debuggare con il grader incorporato.')
    print('Altrimenit puoi inserire qui del codice per testare le tue funzioni ma devi scriverti i casi che vuoi testare')
    print('*'*50)
