## Secondo argomento di Fondamenti di programmazione

"""
Il secondo argomento importante del corso di Fondamenti di Programmazione è la manipolazione e l'interazione con i Files.
I File sono formati da blocchi di bytes consecutivi e, quelli che verranno visti durante il corso, sono di testo (txt, py) oppure
binari (png, mp4, mp3, jpeg). Per leggere e aprire i files correttamente, deve essere chiesto al sistema operativo di preparere
le strutture dati necessarie per interagire con la memoria. In python questo viene fatto tramite la libreria 'os' e la funzione 'open'
"""

import os

# Sintassi 

"""
La sintassi è così composta:
    - filename: è una stringa che indica il percorso da aprire
    - mode: è una stringa che indica il modo in cui il file viene aperto
        1) r (read) solo per leggerne il contenuto
        2) w (write) per scriverci dentro
        3) a (append) per aggiungere un contenuto alla fine
        4) x (exclusive) crea un nuovo file e da errore se esiste già
    - encoding: è una stringa che indice come viene codificato o decodificato il file di testo
        1) utf-8: codifica unicode
        2) ascii: codifica ASCII
    - with: ci assicura che venga aperto un "contesto" dove le cose vengano gestite bene in caso di errore e che il file venga chiuso
"""

with open('1° Anno/Fondamenti di Programmazione/2026-2027/Ripasso/files/testo_semplice.txt', mode = 'w', encoding = 'utf-8') as F:
    # Operazioni da fare (esempio scrivere una frase dentro al file)
    F.write("Pippo è andato al mare\n")
    F.write("Pluto è spiaggiato\n")
    F.write("Topolino è bagnato\n")
    # Controllando nella directory e nel file nello specifico, è stata scritta quella frase

# Possiamo controllare

with open('1° Anno/Fondamenti di Programmazione/2026-2027/Ripasso/files/testo_semplice.txt', mode = 'r', encoding = 'utf-8') as F:
    # Operazioni da fare (esempio leggere dentro al file)
    testo = F.read()
    # print(testo)
    # Funziona!

"""
Di seguito spieghiamo le funzioni più importanti per la lettura di un file su Python:
    • file.read() che permette di leggerne tutto il contenuto (o una parte)
    • file.readline() che permette di leggere una riga da un file di testo
    • file.readlines() che permette di leggere tutte le righe da un file di testo
    • file.close() per chiudere il file, finire di scriverlo su disco e rilasciare la memoria usata
"""

# La funzione read è stata già mostrata sopra quindi:

with open('1° Anno/Fondamenti di Programmazione/2026-2027/Ripasso/files/testo_semplice.txt', mode = 'r', encoding = 'utf-8') as F:
    # Stampa una riga alla volta
    riga = F.readline()
    #print(riga)

with open('1° Anno/Fondamenti di Programmazione/2026-2027/Ripasso/files/testo_semplice.txt', mode = 'r', encoding = 'utf-8') as F:
    # Operazioni da fare (esempio leggere dentro al file)
    righe = F.readlines()
    for riga in righe:
        print(riga)
    
