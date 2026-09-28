# Creare un programma in cui l'utente inserisce un numero da tastiera (es. 10). 
# Il programma deve moltiplicare tutti gli elementi della matrice per quel numero e salvare il nuovo risultato al posto del vecchio.

.globl main

.data

matrice: .word 1, 2, 3
	 .word 4, 5, 6
	 .word 7, 8, 9

numero: .asciz "Inserisci il numero da tastiera: "

.text 

main:

	# --- LETTURA VALORE ---
	la a0, numero
	li a7, 4
	ecall
	
	li a7, 5
	ecall
	mv t0, a0
	
	# --- PREPARAZIONE VARIABILI ---
	la t1, matrice				# t1 = PUNTATORE alla memoria
	li t2, 9				# t2 = LIMITE del ciclo
	li t3, 0				# t3 = CONTATORE del ciclo
	
loop_matrice:

	beq t3, t2, fine
	lw t4, 0(t1)
	mul t4, t4, t0
	sw t4, 0(t1)
	
	addi t1, t1, 4
	addi t3, t3, 1
	
	j loop_matrice
	
fine:

	li a7, 10
    	ecall

	

	

	