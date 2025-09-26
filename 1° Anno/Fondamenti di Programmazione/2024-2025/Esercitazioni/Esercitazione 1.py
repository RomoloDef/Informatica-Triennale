# ESERCIZIO 1
# Avete una stringa di 5 caratteri. Ogni carattere è una cifra decimale. Ad esempio, s="85721". Stampate la
# somma delle cifre contenute nella stringa.

stringa = "85721"
somma = 0
for i in stringa:
    somma += int(i)
print(somma)

# ESERCIZIO 2
# Scrivete una espressione che a partire da una stringa di 5 caratteri, rappresentante un numero binario, stampi la
# sua rappresentazione decimale. Ad esempio, s="00101" -> 5.

s = "00101"
decimale = 0
for i in range(len(s)):
    decimale += int(s[i]) * (2 ** (len(s) - 1 - i))
print(decimale)

# ESERCIZIO 3
# Avete una stringa di 5 caratteri. Il carattere centrale è il punto decimale ('.'). Ad esempio, s="52.29". Stampare il
#numero decimale rappresentato dalla stringa (stamparlo come numero, non come stringa).

s = "52.29"
print(float(s))