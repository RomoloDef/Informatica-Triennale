# Creare un programma che calcoli la somma dei valori presenti sulla diagonale di una matrice data in memoria

.globl main

.data 

matrice: .word 1, 2, 3
	 .word 4, 5, 6
	 .word 7, 8, 9
	 
messaggio_risultato: .asciz "La somma è: "

.text

main:

	# --- Preparazione variabili ---
	la t0, matrice		# t0 = Puntatore in memoria della matrice
	li t1, 3 		# t1 = Limite del ciclo
	li t2, 0		# t2 = Contatore del ciclo
	li t3, 0 		# t3 = Contenitore per la somma
	
loop_diagonale:

	beq t2, t1, fine
	lw t4, 0(t0)		# Lettura valore 
	add t3, t3, t4
	addi t0, t0, 16
	addi t2, t2, 1
	j loop_diagonale
	
fine:

	la a0, messaggio_risultato
    	li a7, 4
    	ecall
    	
    	mv a0, t3         	# Sposto il valore trovato in a0
    	li a7, 1            	# Il codice 1 serve per stampare un intero
    	ecall
    	
    	li a7, 10
    	ecall
	
	