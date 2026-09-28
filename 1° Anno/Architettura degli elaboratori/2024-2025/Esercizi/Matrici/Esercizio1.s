.globl main

.data 
matrice: .word 0:91
messaggio_riga: .asciz "Inserisci il numero della riga: "
messaggio_colonna: .asciz "Inserisci il numero della colonna: "
messaggio_risultato: .asciz "\nIl valore trovato e': " 
N: .word 13

.text 
main:
    # --- LETTURA RIGA ---
    la a0, messaggio_riga
    li a7, 4
    ecall
    
    li a7, 5
    ecall
    mv t4, a0           # t4 = INDICE RIGA
    
    # --- LETTURA COLONNA ---
    la a0, messaggio_colonna
    li a7, 4
    ecall               # CORREZIONE 1: Aggiunto ecall mancante
    
    li a7, 5 
    ecall
    mv t5, a0           # t5 = INDICE COLONNA

    # --- RIEMPIMENTO MATRICE ---
    la t0, matrice      # t0 = Puntatore corrente
    li t1, 91           # Limite ciclo
    li t2, 0            # Contatore
    li t3, 0            # Valore da inserire
    lw a1, N            # a1 = 13 (colonne)

riempi_loop:
    beq t2, t1, ricerca 
    sw t3, 0(t0)      
    addi t3, t3, 1    
    addi t0, t0, 4    
    addi t2, t2, 1    
    j riempi_loop     
    
ricerca:
    # Calcolo: (i * N) + j
    mul t6, t4, a1      # t6 = i * N 
    add t6, t6, t5      # t6 = (i * N) + j 
    slli t6, t6, 2      # t6 = offset in byte
    
    # Calcolo indirizzo finale
    la t0, matrice      # Ricarico l'indirizzo base in t0!
    add a2, t0, t6      # a2 = Indirizzo Base + Offset
    
    # Caricamento del valore
    lw a3, 0(a2)        # Uso a2 (indirizzo), non t6 (offset)

    # --- STAMPA RISULTATO ---
    # Prima stampo la stringa di testo
    la a0, messaggio_risultato
    li a7, 4
    ecall
    
    # Poi stampo l'intero trovato
    mv a0, a3           # Sposto il valore trovato in a0
    li a7, 1            # Il codice 1 serve per stampare un intero
    ecall

    # Uscita pulita dal programma
    li a7, 10
    ecall