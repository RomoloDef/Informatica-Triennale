##########################################
# INSERIRE I PROPRI DATI QUI
# Nome: Romolo
# Cognome: Deffereria
# Matricola: 214887
##########################################

# NON MODIFICARE IL CODICE DA QUI...
.data
    buffer: .space 26

.text

main:
    	li a7, 8       # Codice per input stringa
    	la a0, buffer  # Carica indirizzo base in a0
    	li a1, 26      # Alloca al massimo 24 caratteri + \n + \0
    	ecall          # a0 contiene l'indirizzo base della stringa
# ... A QUI

##########################################

	mv t0, a0	# Sposto l'indirizzo di base nel registro: t0
	
	li t2, 0	# Prima cifra della coppia
	li t3, 0	# Numero decimale
	li t4, 0	# Sommatoria totale
	li t5, 0	# Contatore numeri maggiori di 50
	li t6, 0	# Flag di coppia: 0 = cerco la 1ª cifra, 1 = cerco la 2ª
	
	li a2, 10	# Valore ASCII del carattere: '\n'
	li a3, 48	# Valore ASCII del carattere: '0'
	li a4, 57	# Valore ASCII del carattere: '9'
	li a5, 50	# Costante di soglia: 50
	li a6, 10	# Moltiplicatore per 10 (decine)
	
ciclo:

	lb t1, 0(t0)	# Carattere corrente della stringa: buffer[i]
	
	# Primo confronto con la terminazione della stringa
	
	beq t1, a2, fineStringa
	beq t1, zero, fineStringa
	
	# Verifica che la prima cifra sia un decimale
	
	blt t1, a3, avanza
	bgt t1, a4, avanza
	
	# Elaboro i bit
	
	addi t1, t1, -48
	
	# Verifico se bisogna aspettare la seconda cifra
	
	beq t6, zero, prima_cifra
	
	# Seconda cifra
	
	mul t2, t2, a6
	add t2, t2, t1
	
	# Una volta fatto, verifico che sia maggiore di 50
	
	ble t2, a5, reset_coppia
	
	# Altrimenti
	
	addi t5, t5, 1
	add t4, t4, t2
	
reset_coppia:

	li t6, 0
	j avanza
	
prima_cifra:
	
	mv t2, t1
	li t6, 1
	
avanza:

	addi t0, t0, 1
	j ciclo
	
fineStringa:

	# Stampo i valori richiesti
	
	mv a0, t4
	li a7, 1
	ecall
	
	li a0, 10
	li a7, 11
	ecall
	
	mv a0, t5
	li a7, 1
	ecall
	
	# Fine programma
	
	li a7, 10
	ecall
