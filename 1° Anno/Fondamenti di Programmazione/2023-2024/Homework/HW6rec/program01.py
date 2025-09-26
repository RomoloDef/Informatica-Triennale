# -*- coding: utf-8 -*-
'''
I Caponians, una specie aliena proviente da un non ben specificato
pianeta della galassia, stanno pianificando da un bel po' l'invasione
del pianeta Terra. Per farlo, hanno creato e installato in vari punti
del pianeta varie *mind bending machine*, macchine che riducono
l'intelligenza degli umani attraverso la rete telefonica [1].

Terminata la fase di riduzione dell'intelligenza umana, il prossimo
passo verso la conquista della Terra sara' lo sbarco sul nostro
pianeta, che avverra' non appena i Caponians avranno trovato dei punti
sufficientemente spaziosi per far atterrare le loro astronavi.

Un'astronave vista dall'alto puo' essere rappresentata come un
rettangolo di dimensioni W (larghezza) e H (altezza). Nel considerare
lo spazio necessario ad un'astronave per atterrare vanno pero' aggiunti
sui 4 lati del rettangolo 4 aree in piu'. Le aree in piu' sono una una
per lato.
Le aree sporgono tutte di una stessa quantita' D, per permettere di
aprire su ogni lato un portellone di sbarco. Ogni portellone e' quindi
largo quanto il lato dell'astronave su cui si trova e lungo D, su
qualunque lato si trovi.

I Caponians vorrebbero sbarcare con le loro astronavi in alcune nostre
citta', di cui hanno scaricato le rispettive mappe. Una citta' puo'
essere rappresentata come un'immagine rettangolare nera, in cui ogni
palazzo e' rappresentato come un rettangolo colorato (ogni palazzo ha
un colore che lo identifica univocamente).

Per definire gli ultimi dettagli del piano di sbarco, i Caponians
hanno bisogno di un algoritmo che, data la mappa di una citta' e un
elenco di astronavi definite come sopra, confermi oppure no se
ciascuna astronave ha abbastanza spazio per atterrare in quella citta',
aprire i suoi 4 portelloni e sbarcare il suo contenuto. Le astronavi
non atterrano contemporaneamente nella citta', quindi vanno valutate
separatamente le une rispetto alle altre.

(1) Quindi, data un'immagine nera (citta') con dei rettangoli colorati
pieni (palazzi) disegnati sopra, con ogni rettangolo di un colore
diverso da tutti gli altri, bisognera':

- determinare posizione, dimensioni e colore di ogni rettangolo
- salvare in un file di testo un rettangolo per riga
- nel file, ogni rettangolo e' rappresentato con una sequenza di 7 valori:
     x, y, w, h, r, g, b
  separati da virgole, in ordine di coordinata y (numero di riga)
  decrescente e, a parimerito, di x (pixel della riga) crescente.

(2) Successivamente, e' dato un file di testo contente N terne di
interi.  Ogni terna separata internamente e dalle altre terne da un
qualunque numero di spazi, tabulazioni o ritorni a capo. Ogni terna
rappresenta larghezza W, altezza H e distanza minima D (vedere sotto)
di un rettangolo (astronave) che si vorrebbe aggiungere all'immagine
al punto (1):

- restituire una lista di N valori booleani, l'i-esimo valore nella
lista e' True se nell'immagine c'e' abbastanza spazio per inserire
l'i-esimo rettangolo

- un rettangolo puo' essere inserito nell'immagine se esiste almeno una
posizione nell'immagine in cui c'e' abbastanza spazio (cioe' un'area
costituita interamente da pixel neri) per contenere il rettangolo
stesso, piu' le 4 "estensioni" del rettangolo, ossia i 4 portelloni
dell'astronave.

Ad esempio, se un'astronave da inserire ha 2 pixel di
larghezza e 3 di altezza e D = 2, bisognera' cercare uno spazio
nell'immagine adatto a contenere la seguente figura:

                              **
                              **
                            **++**
                            **++**
                            **++**
                              **
                              **

in cui i simboli + sono i pixel del rettangolo/astronave 2x3 e i *
sono i pixel delle 4 estensioni/portelloni

Esempio:
Data la seguente immagine rappresentata con un carattere per ogni
pixel, dove "." e' un pixel nero mentre caratteri diversi da "." sono
pixel colorati (*=rosso, +=verde):

**....
**....
......
......
....++
....++

Il file con i rettangoli trovati da voi salvato deve contenere le
righe:
4,4,2,2,0,255,0
0,0,2,2,255,0,0

e dati le seguenti astronavi:

(3, 3, 0)
(2, 2, 4)
(1, 1, 3)
(4, 2, 1)
(2, 4, 1)

verra' restituita la lista: [True, False, False, False, False]
infatti solo la prima astronave puo' atterrare ad esempio nella
zona marcata da 'X' (non ha sportelloni, infatti D = 0)

**.XXX
**.XXX
...XXX
......
....++
....++

mentre le altre non entrano nella mappa perche', pur avendo un punto
in cui possono atterrare, non possono aprire tutti i portelloni


[1] https://en.wikipedia.org/wiki/Zak_McKracken_and_the_Alien_Mindbenders)
'''

from pngmatrix import load_png8

def rettangolo_nero(immagine, i, j, b, h):
    for x in range(i, i + h):
        for y in range(j, j + b):
            pixel = immagine[x][y]
            if pixel != (0, 0, 0):
                return False
    return True

def crea_rettangolo(i, j, b, h):
    vertice_superiore_sinistro = (i, j)
    vertice_superiore_destro = (i, j + b - 1)
    vertice_inferiore_sinistro = (i + h - 1, j)
    vertice_inferiore_destro = (i + h - 1, j + b - 1)
    return {
        "VerticeSuperioreSinistro": vertice_superiore_sinistro,
        "VerticeSuperioreDestro": vertice_superiore_destro,
        "VerticeInferioreSinistro": vertice_inferiore_sinistro,
        "VerticeInferioreDestro": vertice_inferiore_destro
    }

def ricerca_rettangoli_neri(immagine, b, h, distanza):
    atterraggi = False
    rettangoli = {}

    for i in range(len(immagine) - h + 1):
        for j in range(len(immagine[0]) - b + 1):
            if rettangolo_nero(immagine, i, j, b, h):
                if (j >= distanza) and (j + b - 1 <= len(immagine[0]) - distanza - 1):
                    atterraggi = True
                    nome_rettangolo = f"rettangolo_{i}_{j}"
                    rettangoli[nome_rettangolo] = crea_rettangolo(i, j, b, h)

    return atterraggi, rettangoli

def area_rettangolo_nero(immagine, riga_A, colonna_A, riga_B, colonna_B, colonna_D,colonna_G):
    return all(immagine[x][y] == (0, 0, 0) for x in range(riga_B, riga_A + 1) for y in range(colonna_D, colonna_G + 1))

def ex(file_png, file_txt, file_out):
    def ricerca_coordinate(città):
        coordinate = {}
    
        for riga, riga_valore in enumerate(città):
            for colonna, pixel in enumerate(riga_val):
                if pixel != (0, 0, 0):
                    coordinate.setdefault(pixel, {'min_riga': riga, 'max_riga': riga, 'min_colonna': colonna, 'max_colonna': colonna})
                    coordinate[pixel]['min_riga'] = min(coordinate[pixel]['min_riga'], riga)
                    coordinate[pixel]['max_riga'] = max(coordinate[pixel]['max_riga'], riga)
                    coordinate[pixel]['min_colonna'] = min(coordinate[pixel]['min_colonna'], colonna)
                    coordinate[pixel]['max_colonna'] = max(coordinate[pixel]['max_colonna'], colonna)
    
        return coordinate
    città = load_png8(file_png)
    coordinate = {}

    for riga, riga_val in enumerate(città):
        for colonna, pixel in enumerate(riga_val):
            if pixel != (0, 0, 0):
                coordinate.setdefault(pixel, {'min_riga': riga, 'max_riga': riga, 'min_colonna': colonna, 'max_colonna': colonna})
                coordinate[pixel]['min_riga'] = min(coordinate[pixel]['min_riga'], riga)
                coordinate[pixel]['max_riga'] = max(coordinate[pixel]['max_riga'], riga)
                coordinate[pixel]['min_colonna'] = min(coordinate[pixel]['min_colonna'], colonna)
                coordinate[pixel]['max_colonna'] = max(coordinate[pixel]['max_colonna'], colonna)

    with open(file_out, 'w', encoding="utf-8") as output_file:
        coordinate_ordinate = sorted(coordinate.items(), key=lambda x: (-x[1]['min_riga'], x[1]['min_colonna']))
        for pixel, coordinata in coordinate_ordinate:
            ascissa_inizio = coordinata['min_colonna']
            ordinata_inizio = coordinata['min_riga']
            lunghezza_ascissa = coordinata['max_colonna'] - coordinata['min_colonna'] + 1
            lunghezza_ordinata = coordinata['max_riga'] - coordinata['min_riga'] + 1
            r, g, b = pixel
            output_file.write(f"{ascissa_inizio},{ordinata_inizio},{lunghezza_ascissa},{lunghezza_ordinata},{r},{g},{b}\n")

    with open(file_txt, mode="rt", encoding="utf-8") as file:
        lines = file.readlines()
        lista_tuple = []
        lista_numeri = []

        for line in lines:
            elementi = line.split()
            numeri = [int(x) for x in elementi if x.isdigit()]
            lista_numeri.extend(numeri)

            while len(lista_numeri) >= 3:
                elementi_tuple = tuple(lista_numeri[:3])
                lista_tuple.append(elementi_tuple)
                lista_numeri = lista_numeri[3:]

    astronavi = {}

    for index, elemento in enumerate(lista_tuple):
        astronavi[f'Astronave_{index + 1}'] = {'larghezza': elemento[0], 'lunghezza': elemento[1], 'distanza': elemento[2]}

    controlli = []

    for astronave in astronavi:
        b = astronavi[astronave]["larghezza"]
        h = astronavi[astronave]["lunghezza"] + (2 * astronavi[astronave]["distanza"])
        distanza = astronavi[astronave]["distanza"]
        matrice = città
        atterraggi = ricerca_rettangoli_neri(matrice, b, h, distanza)
        rettangoli = atterraggi[1]

        if atterraggi[0] == False:
            controlli.append(False)
            continue

        risultato_astronave = False

        if atterraggi[0] == True:
            for rettangolo in rettangoli:
                colonna_sx = rettangoli[rettangolo]["VerticeSuperioreSinistro"][1]
                riga_sx_alta = rettangoli[rettangolo]["VerticeSuperioreSinistro"][0]
                riga_sx_bassa = rettangoli[rettangolo]["VerticeInferioreSinistro"][0]
                colonna_dx = rettangoli[rettangolo]["VerticeSuperioreDestro"][1]

                riga_A = riga_sx_bassa - distanza
                colonna_A = colonna_sx
                riga_B = riga_sx_alta + distanza
                colonna_B = colonna_sx
               
                colonna_D = colonna_sx - distanza

               
                colonna_G = colonna_dx + distanza

                area = area_rettangolo_nero(matrice, riga_A, colonna_A, riga_B, colonna_B, colonna_D,colonna_G)

                if area :
                    risultato_astronave = True
                    break

        controlli.append(risultato_astronave)

    return controlli
