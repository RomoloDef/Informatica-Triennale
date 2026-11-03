"""
Esercizi di Programmazione in Python (Gestione File)
Completa le funzioni sottostanti seguendo la traccia di ciascun esercizio.
"""


# ==============================================================================
# ES1
# Leggi un file di testo, trova tutte le parole uniche contenute
# (ignorando maiuscole/minuscole e punteggiatura), e scrivile in un secondo file
# in ordine di lunghezza decrescente e in caso di parità in ordine alfabetico.
# ==============================================================================
def es1(input_file: str, output_file: str) -> int:
    
    with open(input_file, mode = "r", encoding = "utf-8") as F:
        
        testo = F.read()
        for carattere in ",;.:!?'":
            testo = testo.replace(carattere, " ")
            
        lista_par = testo.split()
        uniche = list(set(lista_par))
        
        # ordinamento
        ordinate = sorted(uniche, key = lambda el: (-len(el), el))
        
    with open(output_file, mode = "w", encoding = "utf-8") as file:
        for parola in ordinate:
            parola_da_scrivere = parola + " "
            file.write(parola_da_scrivere)
            
    return len(ordinate)
                
    pass

#print(es1('input_es1.txt', 'output_es1.txt'))


# ==============================================================================
# ES2
# Leggi un file di testo, individua le righe che sono palindrome
# (ignorando spazi e maiuscole/minuscole), e scrivile in un secondo file.
# ==============================================================================
def es2(input_file: str, output_file: str) -> int:
    
    with open(input_file, mode = "r", encoding = "utf-8") as F:
        
        lista = []
        righe = F.readlines()
        for riga in righe:
            riga_mod = riga.lower().strip()
            lista.append(riga_mod)
            
        risultato = []
            
        for frase in lista:
            frase_clean = "".join(frase.lower().split())
            if frase_clean == frase_clean[::-1]:
                risultato.append(frase)
        
        for frase in risultato:
            if frase == "":
                risultato.remove(frase)
                
    with open(output_file, mode = "w", encoding = "utf-8") as file:
        
        for frase in risultato:
            frase_da_scrivere = frase + "\n"
            file.write(frase_da_scrivere)
            
    return len(risultato)
    
    pass

#print(es2('input_es2.txt', 'output_es2.txt'))


# ==============================================================================
# ES3
# Leggi un file che contiene numeri separati da virgole, spazi, tab o accapi,
# ne calcola la media, e scrivi in un secondo file tutti i numeri maggiori
# della media in ordine decrescente.
# ==============================================================================
def es3(input_file: str, output_file: str) -> float:
    
    with open(input_file, mode = "r", encoding = "utf-8") as F:
        
        numeri = []
        
        righe = F.readlines()
        for riga in righe:
            riga_mod = riga.split()
            riga_clean = [num.replace(",", "") for num in riga_mod]
            for numero in riga_clean:
                numeri.append(numero)
                
        sommatoria = 0
        for numero in numeri:
            sommatoria += int(numero)
            
        media = float(sommatoria // len(numeri))
        maggiori = []
        
        for num in numeri:
            if int(num) >= media:
                maggiori.append(num)
                
        ordinati = sorted(maggiori, key = lambda n: (-int(n)))
        
    with open(output_file, mode = "w", encoding = "utf-8") as file:
        
        for num in ordinati:
            num_da_scrivere = num + " "
            file.write(num_da_scrivere)
            
    return media
    
    pass

#print(es3('input_es3.txt', 'output_es3.txt'))

# ==============================================================================
# ES4
# Leggi un file di testo, raggruppa le righe in base alla loro lunghezza
# (ad esempio tutte le righe di 10 caratteri insieme), e scrivi ogni gruppo in un
# secondo file, separando i gruppi con una riga vuota.
# I gruppi vanno elencati in ordine crescente di lunghezza.
# ==============================================================================
def es4(input_file: str, output_file: str) -> int:
    
    with open(input_file, mode = "r", encoding = "utf-8") as F:
        
        parole = []
        
        righe = F.readlines()
        for riga in righe:
            for parola in riga.split():
                parole.append(parola)
                
        dizionario: dict = {}
        for parola in parole:
            lunghezza = len(parola)

      
            if lunghezza not in dizionario:
              dizionario[lunghezza] = []

            dizionario[lunghezza].append(parola)
        
        dizionario_ordinato =  {k: dizionario[k] for k in sorted(dizionario)}
            
        gruppi_parole = []
        for valore in dizionario_ordinato.values():
            gruppi_parole.append(valore)
            
    with open(output_file, mode = "w", encoding = "utf-8") as file:
         
         for gruppo in gruppi_parole:
             for parola in gruppo:
                 parola_da_scrivere = parola + " "
                 
                 file.write(parola_da_scrivere)
                 
             file.write("\n")
             
    return len(gruppi_parole)
    
    
    pass

print(es4('input_es4.txt', 'output_es4.txt'))

