import immagini

def es42(fImageIn, fcolori, fImageOut):
    '''
    Si progetti la funzione es42(fImageIn, fcolori, fImageOut) che
    modifica il colore di alcuni pixel presenti in un imagine  PNG fImageIn  e salva poi l'immagine
    modificata  in un nuovo file PNG FImageOut.
    La funzione inoltre ritorna il numero di pixel dell'immagine i cui colori sono stati modificati.
    I colori da modificare sono specificati dal file di testo fcolori.
    Il file fcolori ha tante righe quanti sono i colori da modificare.
    Ogni riga di fcolori contiene  6 interi a valori tra 0 e 255.
    I primi tre indicano il colore da modificare
    e i secondi tre il nuovo colore
    Ad esempio la presenza eventuale della riga
    0 0 0  255 255 255
    indica che nell'immagine tutti  i pixel di colore nero ( i.e. di colore  (0,0,0)) devono
    assumere colore bianco (i.e. devono assumere colore (255,255,255)).

    NOTA: i colori devono essere sostituiti contemporaneamente
    (e non con una sostituzione alla volta che potrebbe modificare un pixel piu' volte)

    :param fImageIn: nome del file PNG contenente l'immagine da modificare
    :param fcolori: nome del file di testo in cui trovare i colori da modificare
    :param fImageOut: nome del file PNG in cui salvare l'immagine modificata
    :return: numero di pixel modificati
    '''
    img = immagini.load(fImageIn)
    altezza = len(img)
    larghezza = len(img[0])
    
    with open(fcolori, mode = "r", encoding = "utf-8") as F:
        righe = F.readlines()
        colori = []
        for riga in righe:
            valori = list(map(int, riga.split()))
            colore1 = tuple(valori[0:3])
            colore2 = tuple(valori[3:6])
            colori.append((colore1, colore2))
    
    conteggio = 0
    img_copia = []
    for row in img:
        nuova_riga = row[:]      
        img_copia.append(nuova_riga)
        
    for colore_da_cambiare, colore_da_inserire in colori:    
        for x in range(larghezza):
            for y in range(altezza):
                if img_copia[y][x] == colore_da_cambiare:
                    img[y][x] = colore_da_inserire
                    conteggio += 1
                    break
                    
    immagini.save(img, fImageOut + ".png")
    
    return conteggio
                
print(es42("scacchiera.png", "fcolori1.txt", "scacchieraOut1"))



