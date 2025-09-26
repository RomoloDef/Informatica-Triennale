# Pattern per trovare i segmenti di un'immagine 

def trova_segmenti(img, colore):
    altezza, larghezza = len(img), len(img[0])
    segmenti = []
    for y in range(altezza):
        x_start = None
        for x in range(larghezza):
            if img[y][x] == colore:
                if x_start is None:
                    x_start = x # si inizia un nuovo segmento
                # se si è all'ultimo pixel si chiude il segmento
                if x == larghezza - 1:
                    segmenti.append((y, x_start, x))
                else:
                    if x_start is not None:
                        segmenti.append((y, x_start, x-1)) # si chiudo quello precedente 
                        x_start = None
    return segmenti 


# Pattern per trovare i quadrati

def trova_quadrati(img, target_color, N):
    altezza = len(img)
    larghezza = len(img[0])
    quadrati = []

    # scorri tutte le possibili posizioni in alto a sinistra di un quadrato NxN
    for y in range(altezza - N + 1):
        for x in range(larghezza - N + 1):
            match = True
            # controlla tutti i pixel del quadrato NxN
            for dy in range(N):
                for dx in range(N):
                    if img[y + dy][x + dx] != target_color:
                        match = False
                        break
                if not match:
                    break
            if match:
                quadrati.append((y, x))  # salva la posizione in alto a sinistra
    return quadrati


# Se voglio trovare i quadrati 2x2
# for y in range(altezza):
#     for x in range(larghezza):
#       if y + 1 < altezza and x + 1 < larghezza:
#         match = True 
#         for dy in range(2):
#             for dx in range(2):
#                 if img[y+dy][x+dx] != target_color:
#                     match = False 
#                     break
#                 if not match:
#                     break
#                 if match:
#                     quadrati.append((y, x))
#     return quadrati

