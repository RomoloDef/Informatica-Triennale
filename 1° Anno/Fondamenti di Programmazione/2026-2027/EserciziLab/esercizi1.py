# Il file è diviso in celle: ogni cella inizia con una riga "# %%".
# In Spyder (o VS Code) potete eseguire la cella in cui si trova il cursore
# con Ctrl+Invio, oppure con Maiusc+Invio per eseguirla e passare alla
# successiva. Potete anche eseguire tutto il file, come un normale programma.
# Eseguite per prima la cella "Funzioni per i test".

# %% Funzioni per i test (eseguire per prima)
# Queste funzioni servono per eseguire i test: non è necessario capire come
# funzionano.
from typing import Any, Callable, List
import sys


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


# Stampa il risultato di un test (senza controllarlo)
def print_test(func: Callable, *args: List[Any]):
    func_str = func.__name__
    args_str = ', '.join(repr(arg) for arg in args)
    try:
        result = func(*args)
        result_str = repr(result)
        print(f'{func_str}({args_str}) => {result_str}')
    except BaseException as error:
        error_str = repr(error)
        print(f'{bcolors.FAIL}ERRORE: {func_str}({args_str}) => {error_str}')


# Esegue un test e controlla il risultato
def check_test(func: Callable, expected: Any, *args: List[Any]):
    func_str = func.__name__
    args_str = ', '.join(repr(arg) for arg in args)
    try:
        result = func(*args)
        result_str = repr(result)
        expected_str = repr(expected)
        test_outcome = "superato" if (result == expected) else "fallito"
        color = bcolors.OKGREEN if (result == expected) else bcolors.FAIL
        print(f'{color}Test di {func_str} con input {args_str} {test_outcome}. Risultato: {result_str} Atteso: {expected_str}')
    except BaseException as error:
        error_str = repr(error)
        print(f'{bcolors.FAIL}ERRORE: {func_str}({args_str}) => {error_str}')


# %% Radice cubica
# Scrivere una funzione che prende un numero in virgola mobile, ne calcola la
# radice cubica, e la ritorna.
def cubic_root(n):
    if n < 0:
        return -((-n) ** (1/3))
    return n ** (1/3)


check_test(cubic_root, 2.0)
print(cubic_root(-1))


# %% Radici di un'equazione di secondo grado
# Scrivere una funzione che prende tre numeri in virgola mobile(`a`, `b`, `c`)
# e calcola le radici dell'equazione `a x ^ 2 + b x + c` e le ritorna entrambe.
def roots(a, b, c):
    delta = b**2 - 4*a*c
    r1 = (-b + delta**0.5) / (2*a)
    r2 = (-b - delta**0.5) / (2*a)
    return (r1, r2)


#print_test(roots, 2, 3, 4)
#check_test(roots, (-0.020002000400097586, -199.9799979995999), 1, 200, 4)


# %% Saluto con input
# Scrivere una funzione che ritorna una stringa di saluto formata da
# `Ciao `, seguito dal nome letto come input e poi da `Buona giornata!`
def print_hello():
    nome = input("Inserisci il tuo nome: ")
    return f"Ciao {nome}. Buona giornata!"

#print_test(print_hello)


# %% Somma delle cifre
# Avete una stringa di 5 caratteri. Ogni carattere è una cifra decimale.
# Ad esempio, `s = "85721"`. Stampate la somma delle cifre contenute nella stringa.
def dec_str_to_dec(s):
    somma = 0
    for c in s:
        c = int(c)
        somma += c
    return somma
    pass


#print("Risultato di dec_str_to_dec: ", end="")
#print(dec_str_to_dec("85721"))


# %% Da binario a decimale
# Scrivete una espressione che a partire da una stringa di 5 caratteri,
# rappresentante un numero binario, stampi la sua rappresentazione decimale.
# Ad esempio, `s = "00101" -> 5`.
def bin_str_to_dec(s):
    numero_binario = 0
    for c in s:
        c = int(c)
        numero_binario += c ** int(s[c])
    return numero_binario
    pass


#print("Risultato di bin_str_to_dec: ", end="")
#print(bin_str_to_dec("00101"))


# %% Numero con la virgola
# Avete una stringa di 5 caratteri. Il carattere centrale è il punto decimale
# ('.'). Ad esempio, s = "52.29". Stampare il numero decimale rappresentato
# dalla stringa(stamparlo come numero, non come stringa).
def dec_frac_str_to_dec(s):
    intero = s.split(".")[0]
    decimale = s.split(".")[1]

    decimale = "0." + decimale
    
    return int(intero) + float(decimale)
    pass


# print("Risultato di dec_frac_str_to_dec: ", end="")
# dec_frac_str_to_dec("52.29")
