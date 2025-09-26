
'''
Ajeje la bibliotecaria ha recentemente trovato una stanza nascosta
nella biblioteca di Keras (un posto fantastico situato in
Umkansa, il villaggio più grande delle Montagne Bianche).
Lì ha scoperto diversi libri contenenti
spartiti musicali di antiche canzoni Tarahumara e ha,
quindi, invitato un amico musicista a dare un'occhiata.
Il musicista le ha detto che è una scoperta sensazionale,
dato che gli spartiti sono scritti in notazione Tarahumara,
una popolazione ormai estinta, ma molto famosa per 
aver influenzato i musicisti della Sierra Nevada. Per poter
riprodurre i brani le suggerisce di farli tradurre in una
notazione familiare ai musicisti Umkansaniani, ultimi
discendenti dei Tarahumara, in modo che possano riprodurli.

I Tarahumara scrivevano le note usando numeri invece di lettere:
0 al posto di A, 1 al posto di B e così via, fino a 7 al posto di G. 
Le note bemolle (b) e diesis (#)
(vedi la nota 3 sotto, se non sai cosa sono bemolle e diesis)
erano seguite rispettivamente da un - e da un + 
(ad esempio, 0- significa A bemolle). 
Inoltre, ripetevano semplicemente lo stesso numero più volte 
per rappresentare la durata della nota. 
Ad esempio, 0000 significa che la nota A ha una lunghezza di 4, 
mentre 0-0-0-0- significa che la nota A bemolle ha una lunghezza di 4.

Le pause venivano scritte come spazi:
ad esempio, dodici spazi rappresentano una pausa lunga 12. 
Sia le note che le pause potevano estendersi su
diverse linee della partitura (ad esempio, iniziando dalla linea
x e continuando sulla riga x+1, x+2 e così via).
Infine, gli spartiti musicali erano scritti da destra
a sinistra e dall'alto verso il basso, mentre andare accapo 
non significava nulla in termini di partitura musicale.

Gli Umkansaniani, invece, sono soliti scrivere le note utilizzando lettere,
e ogni nota è seguita dalla sua durata (quindi, l'esempio
sopra verrebbe scritto come A4). 
Le note bemolle e diesis sono seguite rispettivamente 
da una 'b' o da una '#' (ad esempio, A bemolle è scritto Ab, 
quindi l'esempio sopra verrebbe scritto ad Ab4). 
Le pause vengono scritte utilizzando la lettera P, seguita dalla 
loro durata e non viene utilizzato alcuno spazio.
Infine, gli Umkansaniani sono abituati a leggere la musica da
sinistra a destra, scritta su una singola riga.

Poiché Ajeje sa che sei un abile programmatore, 
ti fornisce una cartella contenente la trascrizione
di tutte le canzoni di Tarahumara che ha trovato, 
organizzate in più sottocartelle e file (un brano per file).
Inoltre, ha preparato un file indice in cui ogni riga
contiene il titolo di una canzone Tarahumara (tra virgolette),
seguito da uno spazio e dal percorso del file contenente
quella canzone (tra virgolette, relativa alla cartella principale).
Vorrebbe tradurre tutte le canzoni elencate nell'indice e 
salvarle in nuovi file, ciascuno denominato con il titolo 
della canzone che contiene (con estensione .txt),
in una struttura di cartelle corrispondente a quella originale.
Inoltre, vorrebbe archiviare nella cartella principale della
struttura creata un file indice contenente su ogni riga
il titolo di una canzone (tra virgolette) e la corrispondente
lunghezza del brano, separati da uno spazio. 
Le canzoni nell'indice devono essere ordinate per lunghezza decrescente e, 
se la durata di alcuni brani è la stessa, in ordine alfabetico ascendente. 
La durata di una canzone è la somma delle durate
di tutte le note e delle pause di cui è composta.

Sarai capace di aiutare Ajeje nel tradurre le canzoni
Tarahumara in canzoni Umkansaniane?

Nota 0: di seguito viene fornita una funzione per
Umkansanizzare le canzoni di Tarahumara; 
dopo essere stata eseguita, deve restituire un dizionario 
in cui ogni chiave è il titolo di una canzone
ed il valore associato è la durata del brano.

Nota 1: l'indice delle canzoni da tradurre è il file 'index.txt'
che si trova nella directory passata nell'argomento source_root

Nota 2: l'indice delle canzoni tradotte è il file 'index.txt'
che deve essere creato nella directory passata nell'argomento target_root

Nota 3: le note bemolle e diesis sono solo versioni "alterate".
di note regolari; per esempio un A# ("A diesis") è la
versione alterata di un A, cioè una nota A che è un
mezzo tono più alto del A regolare; lo stesso vale per
note bemolle, che sono mezzo tono più basse delle note normali;
dal punto di vista dei compiti, note bemolle e diesis
devono essere trattate allo stesso modo delle note regolari 
(ad eccezione della loro notazione).

Nota 4: Usiamo la notazione inglese delle note A B C D E F G.

Nota 5: potete usare le funzioni della libreria 'os' per creare le directory necessarie
(ad esempio os.makedirs)
'''

import os

def Umkansanize(source_root: str, target_root: str) -> dict[str, int]:
    d = {}
    percorso_indice = source_root + '/' + 'index.txt'
    with open(percorso_indice, 'r', encoding='utf8') as f:
        riga_indice = f.readlines()
        for linea in riga_indice:
            titolo, percorso = linea[1:-2].split('" "')
            index_song = source_root + '/' + percorso
            with open(index_song, 'r', encoding='utf8') as file:
                righe = file.readlines()
                righe_invertite = [riga.strip()[::-1] for riga in righe]
                stringa_trasformata = ''.join(righe_invertite)
                lista_trasformata = trasformazione_in_lista(stringa_trasformata)
                lista_tradotta = traduzione_canzone(lista_trasformata) [0]
                durata_finale = traduzione_canzone(lista_trasformata) [1]
                d[titolo] = durata_finale

                os.makedirs(target_root, exist_ok=True)
                os.makedirs(target_root+'/'+os.path.dirname(percorso), exist_ok=True)
                target_file_path = target_root + '/'+ os.path.dirname(percorso)+'/' +titolo.strip('"') + '.txt'

                with open(target_file_path, 'w', encoding='utf8') as umkansanian_file:
                    umkansanian_file.write(lista_tradotta)

    file_index = target_root + '/' + 'index.txt'
    with open(file_index, 'w', encoding='utf8') as index:
        dizionario_ordinato = trasformazione(d)
        for tupla in dizionario_ordinato:
            c, v = tupla
        index.write('"' + c + '" ' + str(v) + '\n')
        
    return d

                
def traduzione_canzone(stringa: str):
    mappatura_note = {'0': 'A', '1': 'B', '2': 'C', '3': 'D', '4': 'E', '5': 'F', '6': 'G', ' ': 'P'}
    mappatura = {'0-': 'Ab', '1-': 'Bb', '2-': 'Cb', '3-': 'Db', '4-': 'Eb', '5-': 'Fb', '6-': 'Gb'}
    mappatura_seconda = {'0+': 'A#', '1+': 'B#', '2+': 'C#', '3+': 'D#', '4+': 'E#', '5+': 'F#', '6+': 'G#'}
    contatore = 1
    durata1 = 1
    temp = ""
    i = 0
    while i < len(stringa):
        if stringa[i] in mappatura_note:
            temp += mappatura_note[stringa[i]]
            while i < len(stringa) - 1 and stringa[i] == stringa[i + 1]:
                contatore += 1
                i += 1
        elif stringa[i] in mappatura:
            temp += mappatura[stringa[i]]
            while i < len(stringa) - 1 and stringa[i] == stringa[i + 1]:
                contatore += 1
                i += 1
        elif stringa[i] in mappatura_seconda:
            temp += mappatura_seconda[stringa[i]]
            while i < len(stringa) - 1 and stringa[i] == stringa[i + 1]:
                contatore += 1
                i += 1
        durata1 += contatore
        temp += str(contatore)
        contatore = 1
        i += 1
        
    return temp, durata1

def trasformazione_in_lista(stringa: str):
    lista = list(stringa)
    char = len(lista) - 1

    while char > 0:
        if lista[char] in ['+', '-'] and lista[char - 1].isdigit():
            lista[char - 1] += lista[char]
            lista.pop(char)
        char -= 1

    return lista

def durata(stringa:str):
    return len(stringa)

def trasformazione(d):
    d_ordinato = sorted(d.items(), key=lambda x: (-x[1], x[0]))
    out = dict()
    for tupla in d_ordinato:
        out[tupla[0]] = tupla[1]
    return out


                
    pass

    
if __name__ == '__main__':
    Umkansanize("Tarahumara", "Umkansanian")                
                                   
                     
