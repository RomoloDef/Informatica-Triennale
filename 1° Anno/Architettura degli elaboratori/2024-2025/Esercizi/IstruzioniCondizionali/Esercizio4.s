# Dato un array di numeri interi, scrivi un programma che conti quanti numeri pari sono presenti al suo interno.

.globl main

.data
array: .word 7, 4, 11, 8, 2, 9, 10
lunghezza: .word 7

.text 

main:
    	li t0, 0                # t0: Iteratore (i = 0)
    	li t1, 7                # t1: Lunghezza (n = 7)
    	la t2, array            # t2: INDIRIZZO BASE (rimane fisso)
    	li a3, 2                # a3: Divisore
    	li a4, 0                # a4: Contatore numeri pari
    
cicloFor:
    	bge t0, t1, endFor      # Se i >= 7, esci
    
    	# Calcolo l'offset
    	slli t4, t0, 2          # t4 = i * 4
    	add  t5, t2, t4         # t5 = Indirizzo base + Offset (Usa t2, non t3!)
    
    	lw t6, 0(t5)            # t6 = array[i]
    
    	# Controllo se pari
    	rem a2, t6, a3          # a2 = t6 % 2
    	bne a2, zero, dispari   # SE IL RESTO NON E' 0, SALTA l'incremento (è dispari)

pari:
    	addi a4, a4, 1          # Incrementa il contatore dei pari

dispari:
    	addi t0, t0, 1          # Incrementa SEMPRE l'iteratore
    	j cicloFor              # Torna su
    
endFor:
    	li a7, 1                # Stampa il risultato
    	mv a0, a4
    	ecall
    
    	li a7, 10               # Exit
    	ecall

	
	

