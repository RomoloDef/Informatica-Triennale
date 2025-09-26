

import immagini

'''    
    Es 12: 4 punti
    Progettare la  funzione es13(fimm,fimm1) che, 
    - riceve gli  indirizzi fimm e  fimm1 di due file .PNG. 
    - legge l'immagine da fimm ne modifica i colori dei pixel e la salva poi 
      all'indirizzo fimm1.
    - restituisce infine il numero di colori DIFFERENTI presenti nell'immagine modificata.
      I colori dei pixel dalla nuova immagine si ottengono a partire da quelli 
      dell'immagine originaria con la seguente  procedura:.
      le tuple dei DIFFERENTI colori presenti nella prima immagine vengono ordinate in 
      ordine crescente.
      La sequenza ordinata di tuple  che si ottiene viene suddivisa a gruppi di 50 (se il 
      numero totale di tuple non e' un multiplo di 50 allora l'ultimo gruppo avra' 
      meno di 50 elementi). 
      I colori corrispondenti alle tuple che compaiono come  primo elemento di 
      ciascun gruppo saranno i colori assegnati ai pixel dell'immagine.
      tutti i pixel che avevano colori corrispondenti a tuple finite in uno stesso 
      gruppo avranno come colore quello corrispondente alla prima tupla del gruppo.
      Ad esempio i pixel che avevano colori corrispondenti alle tuple finite nelle prime 50 posizioni 
      della sequenza ordinata  avranno ora tutti lo stesso colore (dato dal colore corrispondente 
      alla tupla che occupa la prima posizione  della sequenza), i pixel 
      che avevano colori le cui tuple  nella sequenza occupano le posizioni 
      da 50 a 99 avranno tutti lo stesso  colore (corrispondente alla tupla in posizione  
      50) ecc. ecc. 
      Sull'immagine Fig1.png la funzione deve produrre il file RisFig1.png e restituire il numero ?
    Per caricare e salvare i file PNG si possono usare load e save della libreria immagini.
    '''
def es13(fimm,fimm1):
    
    img = immagini.load(fimm)
    colori = []
    altezza = len(img)
    larghezza = len(img[0])
    
    for x in range(larghezza):
        for y in range(altezza):
            c = img[y][x]
            if c not in colori:
                colori.append(c)
    
    colori = sorted(colori, reverse = False)
    
    # suddivido la lista di tuple in gruppi
    colori50 = []
    for i in range(0, len(colori), 50):
        gruppo = colori[i:i+50]
        colori50.append(gruppo)
        
    mappa = {}
    for gruppo in colori50:
        rappresentante = gruppo[0]
        for c in gruppo:
            mappa[c] = rappresentante
            
    immagine = []
    for y in range(altezza):
        riga = []
        for x in range(larghezza):
            colore_originale = img[y][x]
            nuovo_colore = mappa[colore_originale]
            riga.append(nuovo_colore)
        immagine.append(riga)
        
    immagini.save(immagine, fimm1)
    
    numero_colori = set()
    for riga in immagine:
        for colore in riga:
            numero_colori.add(colore)
            
    return len(numero_colori)


print(es13("Foto1.png", "RisFoto1.png"))