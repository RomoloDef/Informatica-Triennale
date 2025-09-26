# Ignorare le righe fino alla 31
from typing import Any, Callable, List, Tuple, Dict, Union
import sys
from unittest import result
import images

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Esegue un test e controlla il risultato
def check_test(func: Callable, expected: Any, *args: List[Any]):
    func_str = func.__name__
    args_str = ', '.join(repr(arg) for arg in args)
    try:
        result = func(*args)
        result_str = repr(result)
        expected_str = repr(expected)
        test_outcome = "succeeded" if (result == expected) else "failed"
        color = bcolors.OKGREEN if (result == expected) else bcolors.FAIL
        print(f'{color}Test on {func_str} on input {args_str} {test_outcome}. Output: {result_str} Expected: {expected_str}')
    except BaseException as error:
        error_str = repr(error)
        print(f'{bcolors.FAIL}ERROR: {func_str}({args_str}) => {error_str}')


# Scrivere una funzione che data una matrice di interi, restituisce la matrice trasposta
# Ad esempio:
# 5 2 9    ->  5 3
# 3 1 0        2 1
#              9 0
def transpose(m : List[List[int]]) -> List[List[int]]:
    altezza = len(m)
    larghezza = len(m[0])
    nuova_matrice: list = []
    for x in range(larghezza):
        nuova_riga = []
        for y in range(altezza):
            nuova_riga.append(m[y][x])
        nuova_matrice.append(nuova_riga)
    return nuova_matrice
            
    pass

# Scrivere una funzione che date due matrici, restituisca una matrice
# equivalente alla somma fra le due matrici.
# Esempio:
#     1 0 1        1 2 1       2 2 2
#     2 1 1   +    2 3 1   =   4 4 2
#     0 1 1        4 2 2       4 3 3
#     1 1 2        1 2 3       2 3 5
# Restituire None se le due matrici non possono essere sommate.
#def matrix_matrix_sum(A: List[List[int]], B: List[List[int]]) -> List[List[int]]:     
    pass

# Scrivere una funzione che date due matrici, restituisca una matrice
# equivalente al prodotto fra le due matrici.
# Esempio:
#     1 0 1        1 2 1       5  4 3
#     2 1 1   x    2 3 1   =   8  9 5
#     0 1 1        4 2 2       6  5 3
#     1 1 2                    11 9 6
# Restituire None se le due matrici non possono essere moltiplicate.
#def matrix_matrix_mul(A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
    pass

# Definire una funzione che dato il nome di un file (img_in) contenente un'immagine,
# calcola l'immagine rotata di 90 gradi a destra e invertita rispetto l'asse verticale.
# L'immagine risultante viene salvata nel file con nome indicato come parametro (img_out)
# Per leggere/scrivere l'immagine usare i comandi load/save del modulo "images" visto a lezione.
# Controllare il file risultante per verificare la correttezza della funzione (non vengono effettuati test automatici)

Pixel = tuple[int, int, int]
black: Pixel = (0, 0, 0)
white : Pixel = 255, 255, 255 
red : Pixel = 255, 0, 0 
green : Pixel = 0, 255, 0 
blue: Pixel= 0, 0,255 
cyan : Pixel = 0, 255, 255 
yellow: Pixel = 255, 255, 0 
purple: Pixel = 255, 0, 255 
grey : Pixel = 128, 128, 128

def img_rotate_right_and_flip_v(img_in: str, img_out: str):
    img = images.load(img_in)
    
    img2 = ruota_destra(img)
    img3 = flip_verticale(img2)
    img4 = ruota_destra(img3)
    images.visd(img4)
    
    images.save(img4, img_out)
    
def crea_immagine(larghezza: int, altezza: int, colore: Pixel=black):
    img = []
    for y in range(altezza):
        riga = []
        for x in range(larghezza):
            riga.append(colore)
        img.append(riga)
    return img
    
def ruota_destra(img):
    altezza, larghezza = len(img), len(img[0])
    img2 = crea_immagine(altezza, larghezza)
    for y in range(altezza):
        for x in range(larghezza):
            XD = altezza - 1 - y
            YD = x
            img2 [YD][XD] = img[y][x]
    return img2

def flip_verticale(img):
    altezza, larghezza = len(img), len(img[0])
    img2 = crea_immagine(larghezza, altezza)
    
    for y in range(altezza):
        for x in range(larghezza):
            Xd = x
            Yd = altezza - 1 - y
            img2[Yd][Xd] = img[y][x]
    
    return img2

pass

# Definire una funzione che dato il nome di un file (img_in) contenente un'immagine,
# calcola l'immagine con i canali rosso e blu invertiti.
# L'immagine risultante viene salvata nel file con nome indicato come parametro (img_out)
# Per leggere/scrivere l'immagine usare i comandi load/save del modulo "images" visto a lezione.
# Controllare il file risultante per verificare la correttezza della funzione (non vengono effettuati test automatici)

def img_invert_channels(img_in: str, img_out : str):
    img = images.load(img_in)
    altezza, larghezza = len(img), len(img[0])

    for y in range(altezza):
        for x in range(larghezza):
            r, g, b = img[y][x]
            img[y][x] = (b, g, r)

    images.visd(img)
    images.save(img, img_out)
    
    

# Definire una funzione che dato il nome di un file (img_in) contenente un'immagine,
# calcola un'immagine in cui ognuno dei 3 canali è quantizzato su 128 possibili valori (cioè, ogni canale può solo assumere 128 valori anzichè 256).
# Ad esempio, (21, 126, 3) diventa (10, 63, 2)
# L'immagine risultante viene salvata nel file con nome indicato come parametro (img_out)
# Per leggere/scrivere l'immagine usare i comandi load/save del modulo "images" visto a lezione.
# Controllare il file risultante per verificare la correttezza della funzione (non vengono effettuati test automatici)
def img_quantize(img_in: str, img_out : str):
    img = images.load(img_in)
    altezza, larghezza = len(img), len(img[0])

    for y in range(altezza):
        for x in range(larghezza):
            r, g, b = img[y][x]
            r1, g1, b1 = r/2 , g/2, b/2
            img[x][y] = r1, g1, b1

    images.visd(img)
    images.save(img, img_out)
    pass

# Definire una funzione che dato il nome di un file (img_in) contenente un'immagine,
# calcola un'immagine in cui la metà destra dell'immagine è scambiata con la metà sinistra.
# (Cioè, le colonne nel range [0, N/2] diventano le colonne [N/2, N] nella nuova immagine,
# e le colonne [N, N/2] nella vecchia immagine diventano le colonne [0, N/2] nella nuova immagine).
# Si può assumere che l'immagine abbia un numero di colonne divisibile per 2.
# L'immagine risultante viene salvata nel file con nome indicato come parametro (img_out)
# Per leggere/scrivere l'immagine usare i comandi load/save del modulo "images" visto a lezione.
# Controllare il file risultante per verificare la correttezza della funzione (non vengono effettuati test automatici)
def img_invert_half(img_in: str, img_out: str):
    img = images.load(img_in)
    altezza, larghezza = len(img), len(img[0])
    nuova_img = []
    metà = larghezza // 2
    for y in range(altezza):
        nuova_riga = []
        for x in range(metà, larghezza):
            nuova_riga.append(img[y][x])
        for x in range(metà):
            nuova_riga.append(img[y][x])
        nuova_img.append(nuova_riga)
    images.save(nuova_img, img_out)

    pass

# Test funzioni
#check_test(transpose, [[5, 3], [2, 1]], [[5, 2], [3, 1]])
#check_test(transpose, [[5, 3], [2, 1], [9, 0]], [[5, 2, 9], [3, 1, 0]])
#check_test(transpose, [[5, 3]], [[5], [3]])
#check_test(transpose, [[5], [3]], [[5, 3]])
#check_test(matrix_matrix_sum, [[2, 2, 2], [4, 4, 2], [4, 3, 3], [2, 3, 5]], [[1, 0, 1], [2, 1, 1], [0, 1, 1], [1, 1, 2]], [[1, 2, 1], [2, 3, 1], [4, 2, 2], [1, 2, 3]])
#check_test(matrix_matrix_sum, None, [[1, 0, 1], [2, 1, 1], [0, 1, 1], [1, 1, 2]], [[1, 2], [2, 3], [4, 2], [1, 2]])
#check_test(matrix_matrix_sum, None, [[1, 0, 1], [2, 1, 1], [0, 1, 1], [1, 1, 2]], [[1, 2, 1], [2, 3, 1], [4, 2, 2]])
#check_test(matrix_matrix_mul, [[5, 4, 3], [8, 9, 5], [6, 5, 3], [11, 9, 6]], [[1, 0, 1], [2, 1, 1], [0, 1, 1], [1, 1, 2]], [[1, 2, 1], [2, 3, 1], [4, 2, 2]])
#check_test(matrix_matrix_mul, [[5], [8], [6], [11]], [[1, 0, 1], [2, 1, 1], [0, 1, 1], [1, 1, 2]], [[1], [2], [4]])
#check_test(matrix_matrix_mul, None, [[1, 0, 1], [2, 1, 1], [0, 1, 1], [1, 1, 2]], [[1, 2, 1], [2, 3, 1]])
#img_rotate_right_and_flip_v("img1.png", "img1_rotate_flip.png")
#img_invert_channels("img1.png", "img1_invert_channels.png")
#img_quantize("img1.png", "img1_quantized.png")
img_invert_half("img1.png", "img1_inverted_half.png")