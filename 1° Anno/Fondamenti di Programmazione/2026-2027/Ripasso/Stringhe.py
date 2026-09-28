## Primo argomento di Fondamenti di Programmazione - Stringhe

# Stringhe e Slicing

Stringa1 = "Paperino"

# primo esempio di slicing (prendiamo la prima lettera)
print(Stringa1[0])

# costrutto ord ci permette di vedere a quale numero ASCII corrisponde ogni lettera

print(f"Il valore ASCII di {Stringa1[0]} è {ord(Stringa1[0])}")

# oppure al contrario, tramite il codice ASCII, si può risalire alla lettera

print(f"La lettera corrispondente al codice ASCII {ord(Stringa1[0])} è {chr(ord(Stringa1[0]))}")

# Concatenazione di due stringhe

Stringa2 = "Questo è il primo argomento" + " di Python"
print(Stringa2) 

# Esercizietto 1

numero1 = input("Inserisci un numero: ")

numero2 = input("Inserisci un secondo numero: ")

somma = int(numero1) + int(numero2)
print(somma)

