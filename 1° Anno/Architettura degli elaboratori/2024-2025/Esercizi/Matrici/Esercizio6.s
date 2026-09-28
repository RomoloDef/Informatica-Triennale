# Creare un programma che data una matrice in memoria, la scorra e trova il massimo.

.globl main

.data

matrice: .word 1, 2, 3
	 .word 4, 5, 6
	 .word 7, 8, 9
	 
messaggio_massimo: .asciz "Il massimo in questa matrice è: "

.text 

main:

	# --- PREPARAZIONE VARIABILI ---
	la t0, matrice				# t0 = Puntatore alla memoria
	li t1, 9 				# t1 = Limite del ciclo
	li t2, 0				# t2 = Contatore del ciclo
	lw t3, 0(t0)				# t3 = Primo elemento della matrice
	
loop_massimo:

	beq t2, t1, fine
	lw t4, 0(t0)
	ble t4, t3, prossimo_numero
	mv t3, t4
	
prossimo_numero:

	addi t0, t0, 4
	addi t2, t2, 1
	j loop_massimo

fine:

    # --- STAMPA RISULTATO ---
    # Prima stampo la stringa di testo
    la a0, messaggio_massimo
    li a7, 4
    ecall
    
    # Poi stampo l'intero trovato
    mv a0, t3         	# Sposto il valore trovato in a0
    li a7, 1            # Il codice 1 serve per stampare un intero
    ecall

    # Uscita pulita dal programma
    li a7, 10
    ecall
	

	
	
	
	