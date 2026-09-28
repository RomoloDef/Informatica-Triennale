# Creare un programma che scelta la riga, sommi gli elementi di tale riga

.globl main

.data
    matrice: .word 10, 20, 30
             .word 40, 50, 60  # Vogliamo sommare questa riga!
             .word 70, 80, 90

.text
main:
    # 1. Troviamo il primo numero della Riga 1 (il numero 40)
    # Sappiamo che per saltare l'intera Riga 0 (i primi 3 numeri)
    # dobbiamo fare un balzo iniziale di: 3 elementi * 4 byte = 12 byte.
    
    la t0, matrice      # t0 punta all'inizio (al 10)
    addi t0, t0, 24     # Ora t0 punta al primo elemento della Riga 1 (al 40)

    # 2. Prepariamo il ciclo
    li t1, 3            # Il ciclo gira 3 volte (perché la riga è lunga 3 colonne)
    li t2, 0            # Contatore del ciclo
    li t3, 0            # Qui dentro accumuliamo la somma finale

somma_riga:
    beq t2, t1, fine    # Se abbiamo fatto 3 giri, esci
    
    # 3. Leggiamo il numero e lo sommiamo
    lw t4, 0(t0)        # Prendi il numero puntato da t0
    add t3, t3, t4      # Aggiungilo al totale in t3
    
    # 4. IL PASSO (STRIDE) ORIZZONTALE
    # Avanziamo di soli 4 byte per passare alla "stanza" successiva
    addi t0, t0, 4     
    
    # 5. Aggiorniamo il contatore e ripetiamo
    addi t2, t2, 1      
    j somma_riga

fine:
    # t3 ora contiene 150. Lo stampiamo a schermo!
    mv a0, t3
    li a7, 1
    ecall
    
    li a7, 10
    ecall