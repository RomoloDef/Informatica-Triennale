# Sommare i valori di un vettore di interi e calcolare la media aritmetica.

.globl main

.data

vettore: .word 10, 20, 30, 40, 50

.text

main:

	li t0, 0		# t0: Carico l'iteratore
	li t1, 5		# t1: Carico la lunghezza del vettore
	la t2, vettore		# t2: Carico l'indirizzo di memoria
	li a1, 0		# a1: Contiene la somma degli interi
	
cicloFor:

	bge t0, t1, endFor
	slli t3, t0, 2          # t3 = i * 4
    	add  t4, t2, t3         # t4 = Indirizzo base + Offset
    
    	lw t5, 0(t4)            # t5 = array[i]
    	add a1, a1, t5
    	addi t0, t0, 1
    	j cicloFor
    	
endFor:

	li a7, 1
	mv a0, a1               # Carica il risultato in a0
    	ecall
    
    	li a7, 10               # Exit
    	ecall

	

