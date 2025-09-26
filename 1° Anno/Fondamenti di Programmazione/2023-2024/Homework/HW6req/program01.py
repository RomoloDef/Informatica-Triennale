#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
È una tranquilla serata di dicembre e mentre fuori piove a dirotto
ricevi una chiamata dalla tuo amico Bart, poco esperto di computer.
Dopo averlo calmato, ti racconta di essersi messo al
pc per cercare un regalo perfetto sull'onda del successo dei siti di
e-commerce alternativi, facendo ricerche sui siti più disparati
utilizzando un traduttore automatico. Ti racconta di essere finito
su un sito con il dominio .atp, pensando che avesse a che fare
con il tennis, sua grande passione. Dopo aver
seguito un paio di prodotti sullo strano sito, si è accorto che
il suo browser rispondeva più lentamente e il puntatore del mouse
cominciava ad andare a scatti. Dopo pochi secondi, gli è apparso un
messaggio di avvertimento che lo informava di essere stato
infettato da un ransomware di ultima generazione, che prende
di mira i file del pc. Colto dal panico, si è ricordato della
tua impresa con gli spartiti dei Tarahumara e ti ha chiamato
affinché lo aiuti a recuperare i suoi file. Il giorno dopo,
ti rechi a casa di Bart e analizzi la situazione: come pensavi,
il ransomware è il famigerato Burl1(ONE), che cifra i file del pc
memorizzando la chiave di cifratura all'interno delle immagini
con estensione .png, trasformandole in puzzle complicatissimi.
Poiché Bart memorizza le sue immagini su un servizio on cloud,
riesci a recuperare le immagini originali in modo da poter
risalire alla chiave di cifratura del ransomware. Riuscirai
a trovare tutte le chiavi? Bart conta su di te!

Il ransomware Burl1 memorizza la chiave di cifratura dividendo
in tasselli quadrati le immagini con estensione .png ed eseguendo
o meno delle rotazioni dei singoli tasselli di 90, 180 oppure 270°, 
ovvero eseguendo una, due o tre rotazioni a destra. La chiave avrà
rispettivamente una 'R' (right) una 'F' (flip) o una 'L' (left) a
seconda della rotazione fatta. L'assenza di rotazione indica il
carattere 'N'. Per ogni immagine è necessario ricostruire la chiave
di cifratura sotto forma di una lista di stringhe: ogni stringa
corrisponde alla sequenza di rotazioni di ogni tassello di una
riga. Per cui un'immagine 100x60 in cui i tasselli hanno dimensione
20 nasconderà una chiave di cifratura di 15 caratteri, organizzati
in tre stringhe da cinque caratteri ognuna. Infatti, ci saranno
5 tasselli per riga (100//20 = 5) e 3 righe (60//20 = 3).
Per scoprire le rotazioni eseguite devi utilizzare l'immagine
che hai recuperato dal cloud per eseguire il confronto con
l'immagine cifrata.

Devi scrivere la funzione
jigsaw(puzzle_image: str, plain_image: str, tile_size:int, encrypted_file: str, plain_file: str) -> list[str]:
che prende in ingresso 
- il nome del file contenente l'immagine con i tasselli ruotati, 
- il nome del file contenente l'immagine con i tasselli non ruotati, 
- un intero che indica la dimensione del lato dei tasselli quadrati, 
- il nome di un file di testo da decifrare con la chiave di cifratura 
- e il nome in cui salvare il file decifrato.

La funzione deve restituire la chiave di cifratura nascosta
nell'immagine in puzzle_image, ovvero la sequenza di
rotazioni da fare per ricostruire l'immagine iniziale e decifrare
il file in input.

Ad esempio, confrontando l'immagine in test01_in.png con test01_exp.png
e considerando i tasselli quadrati da 20 pixel, è possibile
stabilire che le rotazioni applicate sono state
            - 'LFR' per i tasselli della prima riga
            - 'NFF' per i tasselli della seconda riga e
            - 'FNR' per i tasselli della terza riga
            Per cui la chiave da ritornare sarà: ['LFR', 'NFF', 'FNR'].
            
La decifratura del file si ottiene attuando una trasformazione del
cattere in posizione i mediante il carattere della chiave in posizione
i modulo la lunghezza della chiave.

Ad esempio, se la chiave è ['LFR', 'NFF', 'FNR'], la chiave è lunga 9 
e bisogna decifrare il carattere in posizione 14 del file in input,
bisogna considerare il carattere in posizione 14%9 = 5 della chiave,
ovvero 'F'.
Le trasformazioni per la decifratura sono le seguenti:
    - R = text[i] sostituito dal carattere con ord seguente
    - L = text[i] sostituito dal carattere con ord precedente
    - N = resta invariato
    - F = swap text[i] con text[i+1]. Se i+1 non esiste, si considera 
          il carattere text[0].

Ad esempio, se la chiave di cifratura è LFR e il testo cifrato è BNVDCAP,
il testo in chiaro sarà AVOCADO, in quanto la decifratura è la seguente:

step     key      deciphering-buffer
1        LFR      BNVDCAP -> ANVDCAP
         ^        ^
2        LFR      ANVDCAP -> AVNDCAP
          ^        ^
3        LFR      AVNDCAP -> AVODCAP
           ^        ^
4        LFR      AVODCAP -> AVOCCAP
         ^           ^
5        LFR      AVOCCAP -> AVOCACP
          ^           ^
6        LFR      AVOCACP -> AVOCADP
           ^           ^
7        LFR      AVOCADP -> AVOCADO
         ^              ^

'''


import images

def lavoro_tasselli(immagine_ruotata, immagine_normale, tile_size):
    # calcolo l'altezza e la larghezza dell'immagine
    altezza, larghezza = len(immagine_ruotata), len(immagine_ruotata[0])
    # inizializzo una nuova varibaile che avrà stesse dimensioni dell'immagine ma ruotata
    immagine_finale = [[0] * larghezza for _ in range(altezza)]
    # inizializza una lista per le rotazioni di ciascun tasssello
    chiave_di_cifratura = []

    # I due for loop servono per scorrere i tasselli tramite le righe e le colonne
    for y in range(0, altezza, tile_size):
        for x in range(0, larghezza, tile_size):
            # Estraggo il tassello dall'immagine ruotata
            tassello = [row[x:x+tile_size] for row in immagine_ruotata[y:y+tile_size]]
            # Estraggo il tassello dall'immagine non ruotata
            tassello_normale = [row[x:x+tile_size] for row in immagine_normale[y:y+tile_size]]
            
            # Inizializzo il conteggio delle rotazioni del tassello
            rotazioni = 0
            # Tramite il ciclo while, il tassello continua a ruotare fino a quando non corrisponde con il tassello dell'immagine normale
            while tassello != tassello_normale:
                tassello = rotazione_90(tassello)
                rotazioni += 1
            # Se il numero di rotazioni è uguale alle volte che il tassello ruota, aggiungi la lettera alla chiave
            if rotazioni == 1:
                chiave_di_cifratura.append('R')
            elif rotazioni == 2:
                chiave_di_cifratura.append('F')
            elif rotazioni == 3:
                chiave_di_cifratura.append('L')
            else:
                chiave_di_cifratura.append('N')
                
            # Vengono inseriti i tasselli ruotati nell'immagine ruotata
            for i in range(tile_size):
                for j in range(tile_size):
                    immagine_finale[y + i][x + j] = tassello[i][j]

    return immagine_finale, chiave_di_cifratura

# Funzione per la rotazione di un'immagine. Nel nostro caso servirà per ruotare i singoli tasselli
def rotazione_90(immagine):
    altezza, larghezza = len(immagine), len(immagine[0])
    immagine_ruotata = [[0] * altezza for _ in range(larghezza)]

    for y in range(altezza):
        for x in range(larghezza):
            X = larghezza - 1 - y
            Y = x
            immagine_ruotata[Y][X] = immagine[y][x]

    return immagine_ruotata

def decifratura(testo_cifrato, chiave):
    # Inizializzo una stringa che conterrà il testo decifrato
    testo_decifrato = ""
    # For loop per iterare su ogni carattere del testo cifrato
    for i in range(len(testo_cifrato)):
        # Ottengo il carattere corrispondente dalla chiave di cifratura tramite (%) affinchè la chiave si ripeta quando si raggiunge la fine.
        chiave_carattere = chiave[i % len(chiave)]
        # Se il carattere è uguale a R incrementa l'ordine del carattere corrente e lo aggiunge al testo decifrato.
        if chiave_carattere == 'R':
            testo_decifrato += chr((ord(testo_cifrato[i]) + 1))
        # Se il carattere della chiave è 'L', decrementa l'ordine del carattere corrente e lo aggiunge al testo decifrato.
        elif chiave_carattere == 'L':
            testo_decifrato += chr((ord(testo_cifrato[i]) - 1))
        # Se il carattere della chiave è 'F' si verificano detrminate condizioni: 
        elif chiave_carattere == 'F':
            # Verifico se ci sono altri caratteri nel testo cifrato dopo quello corrente. Se la risposta è sì, si verificano due condizioni
            if (i+1) < len(testo_cifrato):
                # Aggiungo il carattere successivo al testo decifrato.
                testo_decifrato += testo_cifrato[i+1]
                # Eseguo uno swap tra il carattere corrente e il successivo nel testo cifrato.
                testo_cifrato = testo_cifrato[:i+1] + testo_cifrato[i] + testo_cifrato[i+2:]
            # Altrimenti, se ci si trova all'ultimo carattere del testo cifrato:
            else:
                testo_decifrato += testo_cifrato[i]
                
        else:
            # Aggiungo il carattere corrente dal testo decifrato
            testo_decifrato += testo_cifrato[i]
    return testo_decifrato

def jigsaw(puzzle_image: str, plain_image: str, tile_size: int, encrypted_file: str, plain_file: str) -> list[str]:
    # Carico le immagini
    immagine_modificata = images.load(puzzle_image)
    immagine_normale = images.load(plain_image)
    larghezza = len(immagine_modificata[0])
    numero_di_tasselli = larghezza // tile_size
    # Richiamo e applico le funzioni precedenti
    immagine_modificata, chiave_di_cifratura = lavoro_tasselli(immagine_modificata, immagine_normale, tile_size)
    chiave_di_cifratura_raggruppata = ["".join(chiave_di_cifratura[i:i+numero_di_tasselli]) for i in range(0, len(chiave_di_cifratura), numero_di_tasselli)]
    # Apro il file di lettura
    with open(encrypted_file, 'r', encoding = 'utf-8') as f:
        testo_cifrato = f.read()
        
    testo_decifrato = decifratura(testo_cifrato, ''.join(chiave_di_cifratura_raggruppata))
    # Scrivo sul plain file il mio testo decriptato
    with open(plain_file, 'w', encoding= 'utf-8') as f:
        f.write(testo_decifrato)

    return chiave_di_cifratura_raggruppata

if __name__ == '__main__':
    print(jigsaw('tests/test01_in.png', 'tests/test01_exp.png', 20,
                 'tests/test01_enc.txt', 'output/test01_out.txt'))

