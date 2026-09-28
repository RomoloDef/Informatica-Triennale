

'''
    Es 9: 3 punti
    Si definisca la funzione es9(pathDir ) ricorsiva (o che fa uso di funzioni o 
    metodi ricorsive/i) che:
    - riceve come argomento l'indirizzo di una cartella.
    - restituisce una lista contenente i nomi delle sottocartelle in essa contenute a
      qualsiasi livello e per ogni sottocartella anche lo spazio  (in byte) occupato all'interno 
      della cartella da eventuali file di tipo .txt.
      La lista contiene dunque coppie, il primo elemento della coppia e' il nome di 
      una sottocartella ed il secondo e' lo spazio occupato dai file .txt presenti nella
      sottocartella.
      Le coppie devono comparire nella lista ordinate in modo decrescente rispetto 
      alla loro seconda componente e  a parita' vanno ordinate poi in modo lessicografico 
      crescente rispetto alla prima componente.
      File e cartelle il cui nome comincia  col carattere '.' non vanno considerati. 
      
      Ai fini dello svolgimento dell'esercizio possono risultare utili 
      le seguenti funzioni nel modulo os:
      os.listdir(), os.path.isfile(), os.path.isdir(), os.path.basename(), 
      os.path.getsize()

    Esempio: con es9('Informatica/Software') viene restituita la lista:
    [('SistemiOperativi', 287), ('Software', 10), ('BasiDati', 0)]

'''

import os
def es9(pathDir: str):
    # nome della cartella corrente (basename del path)
    cartella_corrente = os.path.basename(pathDir)
    # calcolo lo spazio dei file .txt presenti DIRETTAMENTE in questa cartella
    spazio = 0
    for nome in os.listdir(pathDir):
        if nome in '_.': continue
        fullname = pathDir + '/' + nome
        if os.path.isfile(fullname) and nome.endswith(".txt"):
            spazio += os.path.getsize(fullname)
    # creo la lista con la coppia della cartella corrente
    risultato = [(cartella_corrente, spazio)]
    # ora esploro ricorsivamente le sottocartelle
    for nome in os.listdir(pathDir):
        if nome in '_.': continue
        fullname = pathDir + '/' + nome
        if os.path.isdir(fullname):
            risultato.extend(es9(fullname)) # QUESTO è QUELLO CHE MI MANCAVA
    risultato.sort(key=lambda t: (-t[1], t[0]))
    return risultato


# esempio
print(es9('Informatica/Software'))
                
    
        
