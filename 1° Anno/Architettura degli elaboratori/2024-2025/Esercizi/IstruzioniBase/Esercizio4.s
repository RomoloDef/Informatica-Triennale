# Effettuare la media aritmetica di 5 numeri positivi definiti in memoria
# e stampare il risultato a schermo

.globl main

.data 
    a: .word 5 
    f: .word 3
    c: .word 2
    d: .word 1
    e: .word 4

.text 
main:
    # 1. Carico gli indirizzi di memoria
    la t0, a
    la t1, f
    la t2, c
    la t3, d
    la t4, e
    
    # 2. Leggo i veri valori dalla memoria (MOLTO IMPORTANTE)
    lw t0, 0(t0)   # t0 = 5
    lw t1, 0(t1)   # t1 = 3
    lw t2, 0(t2)   # t2 = 2
    lw t3, 0(t3)   # t3 = 1
    lw t4, 0(t4)   # t4 = 4
    
    # 3. Effettuo le operazioni matematiche (Accumulo la somma)
    add t5, t0, t1 # t5 = 5 + 3 = 8
    add t5, t5, t2 # t5 = 8 + 2 = 10
    add t5, t5, t3 # t5 = 10 + 1 = 11
    add t5, t5, t4 # t5 = 11 + 4 = 15
    
    # 4. Calcolo la media (Divido per 5)
    li t6, 5       # Carico il numero totale degli elementi (5) in t6
    div t5, t5, t6 # t5 = 15 / 5 = 3. Il risultato (3) è in t5
    
    # 5. Stampo a schermo
    li a7, 1       # Carico in a7 il codice servizio 1 (Print Integer)
    mv a0, t5      # Sposto il risultato (t5) nel registro a0 per stamparlo
    ecall          # Chiamo il sistema operativo: stampa!

    # 6. Fine pulita del programma
    li a7, 10      # Carico in a7 il codice servizio 10 (Exit)
    ecall          # Termino il programma