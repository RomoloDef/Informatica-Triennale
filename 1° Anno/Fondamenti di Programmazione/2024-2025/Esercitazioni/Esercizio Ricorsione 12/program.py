

from albero import Nodo

'''
    Es 12: 3 punti
    Un albero si dice binario completo se tutti i suoi nodi interni hanno esattamente 2 
    figli e tutte le foglie si trovano allo stesso livello.
    Si definisca la funzione es12(k ) ricorsiva (o che fa uso di funzioni o 
    metodi ricorsive/i) che:
    - riceve come argomenti  un intero k 
    - costruisce un albero binario completo di altezza k composta da nodi del tipo  
      Nodo definito nella libreria albero.py allegata. Gli identificatore delle foglie, 
      letti da sinistra a destra sono i 2^k-interi che vanno da 1 a 2^k (nota che 
      un albero binario completo di altezza k ha sempre 2^k foglie). Gli identificatori 
      dei nodi interni sono dati dalla somma degli identificatori dei due loro figli. 
    - torna come risultato la radice dell'albero costruito. 
    Esempio: 
    - es12(2)  crea e restituisce l'albero a sinistra 
    - es12(3) crea e restituisce l'albero a destra


                    10                                  36               
             _______|______                      _______|______         
            |              |                    |              |        
            3              7                   10             26        
         ___|___        ___|__               ___|___        ___|__      
        |       |      |      |             |       |      |      |     
        1       2      3      4             3       7     11     15     
                                           _|_     _|_    _|_    _|_    
                                          |   |   |   |  |   |  |   |   
                                          1   2   3   4  5   6  7   8   
                                                                   
    '''


def es1(k):
    # creo l'albero binario senza valori
    tree = genera_albero_vuoto(k)
    # lo esploro e inserisco i valori nelle foglie ricordando fino a dove sono arrivato
    inserisci_foglie(tree, 1)
    # lo esploro e calcolo i valori interni
    calcola_interni(tree)
    # torno il nodo radice
    return tree

def genera_albero_vuoto(k):
    if k==0:                   # da controllare
        return Nodo(None)
    sx = genera_albero_vuoto(k-1)
    dx = genera_albero_vuoto(k-1)
    radice = Nodo(None)
    radice.f = [sx, dx]
    return radice

def inserisci_foglie(radice, N):
    if radice.f == []:
        radice.id = N
        return N+1
    nuovoN = inserisci_foglie(radice.f[0],N)
    return inserisci_foglie(radice.f[1],nuovoN)

def calcola_interni(radice):
    if radice.id is None:
        calcola_interni(radice.f[0])
        calcola_interni(radice.f[1])
        radice.id = radice.f[0].id + radice.f[1].id

# def calcola_interni2(radice):
#     if radice.id is not None:
#         return radice.id
#     else:
#         radice.id = calcola_interni2(radice.f[0]) + calcola_interni2(radice.f[1])
#         return radice.id
#     pass

print(es1(3))
    
