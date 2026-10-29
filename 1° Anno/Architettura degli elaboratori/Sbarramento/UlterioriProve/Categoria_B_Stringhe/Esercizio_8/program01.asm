##########################################
# INSERIRE I PROPRI DATI QUI
# Nome: Romolo
# Cognome: Deffereria
# Matricola: 2114887
##########################################

# NON MODIFICARE IL CODICE DA QUI...
.data
    buffer: .space 26

.text
.globl main

main:
    	li a7, 8       # Codice per input stringa
    	la a0, buffer  # Carica indirizzo base in a0
    	li a1, 26      # Alloca al massimo 24 caratteri + \n + \0
    	ecall          # a0 contiene l'indirizzo base della stringa
# ... A QUI

##########################################

	mv t0, a0	# Sposto l'indirizzo di base nel registro: t0
	
	li t2, 0	# Flag: prima cifra in attesa
	li t3, 0	# Sommatoria delle coppie di cifre
	li t4, 0	# Contatore delle somme multiple di 3
	li t5, 0	# Contatore delle somme non multiple di 3
	
	li t6, 10	# Valore ASCII del carattere: '/n'
	
	addi t0, t0, 1	# Ignoro il primo carattere della stringa
	
ciclo:

	lb t1, 0(t0)	# Carattere corrente della stringa: buffer[i]
	
	# Primo confronto con la terminazione della stringa
	
	beq t1, t6, fineStringa
	beq t1, zero, fineStringa
	
	# Verifico che non sia una cifra
	# Confronto per vedere se sono carattere non numerici
	
	li a2, 48
	li a3, 57
	
	blt t1, a2, avanza
	bgt t1, a3, avanza
	
	# Elaboro il bit
	
	addi t1, t1, -48
	
	# Ho già una prima cifra in attesa?
	
    	li a4, 0
    	beq t2, a4, prima_cifra    # t2 == -1 → questa è la prima cifra
    	
    	# formo la coppia e sommo
    	
    	add t3, t2, t1
    	
    	# Resetto
    	
    	li t2, 0
    	
    	# Ora posso controllare la divisibilità della somma
    	
    	li a5, 3
    	rem a6, t3, a5
    	beq a6, zero, multiplo
    	addi t5, t5, 1             # B++
    	j avanza
    	
    	
prima_cifra:

    mv t2, t1                  # Salvo la prima cifra in t2
    j avanza	
	
avanza:

	addi t0, t0, 1
	j ciclo
	
multiplo:

	addi t4, t4, 1
	j avanza
	
fineStringa:

	# Stampo il tutto
	
	mv a0, t4
	li a7, 1
	ecall
	
	li a0, 10
	li a7, 11
	ecall
	
	mv a0, t5
	li a7, 1
	ecall
	
	# Fine
	
	li a7, 10
	ecall

	



