# Scrivere un programma che permetta di calcolare la somma di tutti gli elementi presenti in una specifica colonna scelta dall'utente.

.globl main

.data
    matrice: .word 10, 20, 30
             .word 40, 50, 60
             .word 70, 80, 90

.text
main:
    # 1. Troviamo il primo numero della Colonna 1 (il numero 20)
    # Sappiamo che si trova all'indice 1 (è il secondo elemento).
    # Indice 1 * 4 byte = offset di 4 byte.
    la t0, matrice      # t0 punta all'inizio (al 10)
    # IN BASE AL NUMERO CHE SI METTE QUI (0-4-8, in base al byte), si accede ad una colonna diversa
    addi t0, t0, 4     # Ora t0 punta al primo elemento della Colonna 1 (al 20)

    # 2. Prepariamo il ciclo
    li t1, 3            # Il ciclo deve girare 3 volte (perché ci sono 3 righe)
    li t2, 0            # Contatore del ciclo
    li t3, 0            # Qui dentro accumuliamo la somma finale

somma_colonna:
    beq t2, t1, fine    # Se abbiamo fatto 3 giri, esci dal ciclo
    
    # 3. Leggiamo il numero e lo sommiamo
    lw t4, 0(t0)        # Prendi il numero puntato da t0 (al primo giro sarà 20)
    add t3, t3, t4      # Aggiungilo al totale in t3
    
    # 4. IL TRUCCO DEL SALTO!
    # Avanziamo di 12 byte per "scendere" alla riga successiva, rimanendo nella stessa colonna
    addi t0, t0, 12     
    
    # 5. Aggiorniamo il contatore e ripetiamo
    addi t2, t2, 1      # Abbiamo fatto un giro
    j somma_colonna

fine:
    # Qui t3 contiene la somma: 20 + 50 + 80 = 150!
    # Stampiamolo
    mv a0, t3
    li a7, 1
    ecall
    
    li a7, 10
    ecall