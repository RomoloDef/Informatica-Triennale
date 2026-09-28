#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 09:42:43 2024

@author: danielefriolo
"""


# Ignorare le righe fino alla 35
from typing import Any, Callable, List, Tuple
import sys
from unittest import result



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


# Implementare una funzionalità equivalente a `dict.update()`, che data una
# lista di dizionari, ritorna un dizionario con tutte le chiavi presenti nei
# dizionari di input. Per valori, si usano i valori nei dizionari di input
# scegliendo quelli dei dizionari con indice superiore se presenti.
def update_dict(dictionaries: List[dict]) -> dict:
    dizionario = {}
    for d in dictionaries:
        for chiave, valore in d.items():
            dizionario[chiave] = valore
    return dizionario
    pass


# Implementare una funzione che prende in input una lista di dizionari e ritorna
# un dizionario le cui chiavi sono le chiavi presenti nei due di input e come
# valori ritorna una lista con i valori presenti nei dizionari di input.
# Si possono usare i set.
def merge_dict(dictionaries: List[dict]) -> dict:
    dizionario: dict
    dizionario = {}
    for d in dictionaries:
        for chiave, valore in d.items():
            if chiave in dizionario:
                dizionario[chiave].append(valore)
            else:
                dizionario[chiave] = [valore]
    return dizionario   


# Implementare una funzione che prende in input una lista di dizionari e ritorna
# un dizionario le cui chiavi sono quelle presenti in tutti i dizionari e i cui
# valori sono la lista di valori delle relative chiavi. Si possono usare i set.
def intersect_dict(dictionaries: List[dict]) -> dict:
    chiavi = set(dictionaries[0].keys())
    for d in dictionaries[1:]:
        chiavi_correnti = set(d.keys())
        chiavi_comuni = chiavi & chiavi_correnti
    dizionario = {}
    for chiave in chiavi_comuni:
        valori = []
        for d in dictionaries:
            valori.append(d[chiave])
        dizionario[chiave] = valori
    return dizionario
    

# Scrivere una funzione che data una stringa, ritorna una lista di tuple
# consituita da parola e frequenza, ordinata per frequenza. La frequenza è
# il numero di volte in cui la parole appare nel testo.
# Per evitare problemi nel trovare le parole, togliere tutti i caratteri
# non alfanumerici, a parte gli spazi, e convertire le parole in minuscolo.
# Usare la funzione `isalnum()` per testare i caratteri.
def word_frequency(string: str):
    lista_finale = []
    stringa = string.lower()
    stringa_finale = ""
    for c in stringa:
        if c.isalnum() or c.isspace():
            stringa_finale += c
    lista = stringa_finale.split()
    frequenza: dict
    frequenza = {}
    for stringa in lista:
        if stringa in frequenza:
            frequenza[stringa] += 1
        else:
            frequenza[stringa] = 1
    for chiave, valore in frequenza.items():
        lista_finale.append((valore, chiave))
    criterio_di_ordinamento = lambda elemento: (elemento)
    fine = sorted(lista_finale, key = criterio_di_ordinamento, reverse = False)
    return fine


# Scrivere una funzione che data una stringa di numeri interi separati da spazi,
# ritorna la lista ordinata dei numeri interi con frequenza massima.
def number_frequency(string: str):
    lista = []
    lista_di_numeri = string.split()
    for numero in lista_di_numeri:
        lista.append(int(numero))
    lista_finale = []
    frequenza: dict
    frequenza = {}
    for n in lista:
        if n in frequenza:
            frequenza[n] += 1
        else:
            frequenza[n] = 1
    massima_frequenza = max(frequenza.values())
    for chiave, frequenza in frequenza.items():
        if frequenza == massima_frequenza:
            lista_finale.append(chiave)
    return sorted(lista_finale)
    

# Scrivere una funzione che restituisce True se una lista di interi
# è composta da una prima parte ordinata in modo crescente, seguita
# da una seconda parte ordinata in modo decrescente (o viceversa).
# Le due parti non devono avere necessariamente la stessa lunghezza.
# Utilizzare un solo ciclo e non utilizzare sorted/sort, ne la funzione
# is_sorted implementata precedentemente.
# Si assuma che la lista abbia almeno sempre 3 elementi.
def is_sorted_half(a: list) -> bool:
    pass



#check_test(update_dict, {'Ciao': 1, 'Pippo': 2, 'Pluto': 3},[{"Ciao": 1, "Pippo": 2}, {"Pluto": 3}])
#check_test(update_dict, {'Ciao': 1, 'Pippo': 4, 'Pluto': 3}, [{"Ciao": 1, "Pippo": 2}, {"Pluto": 3, "Pippo": 4}])
#check_test(merge_dict, {'Ciao': [1], 'Pippo': [2], 'Pluto': [3]},[{"Ciao": 1, "Pippo": 2}, {"Pluto": 3}])
#check_test(merge_dict, {'Ciao': [1], 'Pippo': [2, 4], 'Pluto': [3]}, [{"Ciao": 1, "Pippo": 2}, {"Pluto": 3, "Pippo": 4}])
#check_test(intersect_dict, {'Pippo': [2, 3]}, [{"Ciao": 1, "Pippo": 2}, {"Pippo": 3, "Pluto": 4}])
#check_test(intersect_dict, {'Pippo': [2, 3], 'Pluto': [5, 4]},[{"Ciao": 1, "Pippo": 2, "Pluto": 5}, {"Pippo": 3, "Pluto": 4}])
#check_test(word_frequency, [(1, "ciao"), (1, "pippo")], "Ciao Pippo")
#check_test(word_frequency, [(1, "pluto"), (2, "pippo")], "Pippo Pluto Pippo")
#check_test(word_frequency, [(1, 'pippo'), (1, 'pluto'), (2, 'ciao')], "Ciao Pippo! Ciao Pluto!")
#check_test(number_frequency, [10], "1 2 2 3 10 10 10")
#check_test(number_frequency, [2, 5], "1 1 5 5 5 2 2 2")
#check_test(is_sorted_half, False, [1, 2, 3])
#check_test(is_sorted_half, False, [3, 2, 1])
#check_test(is_sorted_half, True, [1, 3, 2])
#check_test(is_sorted_half, True, [3, 1, 2])
#check_test(is_sorted_half, True, [1, 2, 5, 6, 8, 9, 3])