
    
def es41(fname1):
    ''' 
    Data una sequenza S di  interi definiamo sequenza derivata da S la  sequenza di n interi dove l'i-esimo 
    elemento e' dato dalla somma dei primi i interi di S.
    Ad esempio:
    la sequenza derivata da 
    S= 2, -3, -4,  4, 4, -5, 3, 1,-1  e'
       2, -1, -5, -1, 3, -2, 1, 2, 1.
    
    Implementate la funzione es41(fname1) che prende in input l'indirizzo fname1 di un file di testo contenente una 
    sequenza S di interi e restituisce il numero che compare con maggior frequenza nella sequenza derivata da S.
    Nel caso in cui i numeri con maggior frequenza siano piu' di uno viene restituito quello di valore massimo.
    Ad esempio se il file fname contiene la sequenza S= 2, -3, -4,  4, 4, -5, 3, 1, -1   la funzione restituisce il valore 2.
    Nel file fname1, ciascun intero della sequenza  e' separato dal successivo da una virgola ed eventuali spazi.
    '''
    # inserisci qui il tuo codice

    with open(fname1, mode = 'r', encoding = "utf8") as F:
        riga = F.read().strip().split(",")
        lista_numeri = []
        for c in riga:
            lista_numeri.append(int(c))
        sequenza = []
        sequenza.append(lista_numeri[0])
        for i in range(1, len(lista_numeri)):
            sequenza.append(sequenza[i-1] + lista_numeri[i])
        frequenza = {}
        for n in sequenza:
            if n in frequenza:
                frequenza[n] += 1
            else:
                frequenza[n] = 1
        max_freq = max(frequenza.values())
        max_num = None
        for k, v in frequenza.items():
            if v == max_freq:
                if max_num is None or k > max_num:
                    max_num = k
    return max_num


print(es41('fsequenza1.txt'))






