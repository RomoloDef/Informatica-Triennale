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

def controllo_nero(x, y, w, h, img):
  # controllo se il rettangolo è nero
  for i in range(x, x + w):
    for j in range(y, y + h):
      if img[j][i] != 0:
        return False
  return True

def cerco_rettangoli(img):
  # cerco i rettangoli
  rettangoli = []
  for y in range(len(img)):
    for x in range(len(img[0])):
      if img[y][x] != 0:
        # cerco la larghezza
        w = 1
        while x + w < len(img[0]) and img[y][x + w] != 0:
          w += 1
        # cerco l'altezza
        h = 1
        while y + h < len(img) and img[y + h][x] != 0:
          h += 1
        # controllo se è nero
        if controllo_nero(x, y, w, h, img):
          rettangoli.append((x, y, w, h, img[y][x]))
  return rettangoli

def area_rettangolo_destra_o_sinistra(x, y, w, h, d, img):
  # controllo se c'è spazio a destra o a sinistra
  for i in range(x - d, x + w + d):
    for j in range(y - d, y + h + d):
      if img[j][i] != 0:
        return False
  return True

def ex(file_png, file_txt, file_out):
    def trova_coordinate(city):
        coordinate = {}

        for riga in range(len(city)):
            for colonna in range(len(city[0])):
                pixel = city[riga][colonna]

                if pixel != (0, 0, 0):
                    if pixel not in coordinate:
                        coordinate[pixel] = {'min_riga': riga, 'max_riga': riga, 'min_colonna': colonna,
                                             'max_colonna': colonna}
                    else:
                        coordinate[pixel]['min_riga'] = min(coordinate[pixel]['min_riga'], riga)
                        coordinate[pixel]['max_riga'] = max(coordinate[pixel]['max_riga'], riga)
                        coordinate[pixel]['min_colonna'] = min(coordinate[pixel]['min_colonna'], colonna)
                        coordinate[pixel]['max_colonna'] = max(coordinate[pixel]['max_colonna'], colonna)

        return coordinate



    city = load_png8(file_png)
    coordinate = trova_coordinate(city)

    with open(file_out, 'w', encoding="utf-8") as output_file:
        sorted_coordinate = sorted(coordinate.items(), key=lambda x: (-x[1]['min_riga'], x[1]['min_colonna']))

        for pixel, coords in sorted_coordinate:
            ascissa_start = coords['min_colonna']
            ordinata_start = coords['min_riga']
            lunghezza_ascissa = coords['max_colonna'] - coords['min_colonna'] + 1
            lunghezza_ordinata = coords['max_riga'] - coords['min_riga'] + 1
            r = pixel[0]
            g = pixel[1]
            b = pixel[2]

            output_file.write(f"{ascissa_start},{ordinata_start},{lunghezza_ascissa},{lunghezza_ordinata},{r},{g},{b}\n")

    with open(file_txt, mode="rt", encoding="utf-8") as file:
        lines = file.readlines()
        tuple_list = []
        temp_numbers = []

        for line in lines:
            elements = line.split()
            numbers = [int(x) for x in elements if x.isdigit()]
            temp_numbers.extend(numbers)

            while len(temp_numbers) >= 3:
                tuple_elem = tuple(temp_numbers[:3])
                tuple_list.append(tuple_elem)
                temp_numbers = temp_numbers[3:]

    astronavi = {}

    for index, elemento in enumerate(tuple_list):
        astronavi[f'Astronave_{index + 1}'] = {'larghezza': elemento[0], 'lunghezza': elemento[1], 'distanza': elemento[2]}

    controlli = []

    for astronave in astronavi:
        b = astronavi[astronave]["larghezza"]
        h = astronavi[astronave]["lunghezza"] + (2 * astronavi[astronave]["distanza"])
        distanza = astronavi[astronave]["distanza"]
        matrice = city
        atterraggi = cerco_rettangoli(matrice, b, h, distanza)
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

                is_area_sx_dx_nera = area_rettangolo_destra_o_sinistra(matrice, riga_A, colonna_A, riga_B, colonna_B, colonna_D,colonna_G)

                if is_area_sx_dx_nera :
                    risultato_astronave = True
                    break

        controlli.append(risultato_astronave)

    return controlli
  
