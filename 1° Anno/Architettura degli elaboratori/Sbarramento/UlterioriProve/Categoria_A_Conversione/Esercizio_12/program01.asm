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
# INSERIRE IL PROPRIO CODICE QUI

	mv t0, a0	# Sposto l'indirizzo base nel registro: t0
	
	li t2, 0	# Accumulatore
	
	li a2, 10	# Valore ASCII del carattere: '/n'
	
ciclo:

	lb t1, 0(t0)	# Carattere corrente della stringa: buffer[i]
	
	# Primo confronto con la terminazione della stringa
	
	beq t1, a2, fineStringa
	beq t1, zero, fineStringa
	
	# Secondo confronto con il separatore
	
	li a3, 47
	
	beq t1, a3, separatore
	
	# Elaboro il bit - Verifico dapprima se sia una lettera o un numero
	
	li a4, 97
	
	bge t1, a4, è_lettera
	
	# Altrimenti è un numero
	
	addi t1, t1, -48
	
	j accumula
	
avanza:
	
	addi t0, t0, 1
	j ciclo
	
è_lettera:

	addi t1, t1, -87
	
accumula:
	
	slli t2, t2, 4
	add t2, t2, t1
	
	j avanza
	
separatore:

	# Una volta arrivati al separatore bisogna stampare quello che c'era prima (accumulatore)
	
	mv a0, t2
	li a7, 1
	ecall
	
	# Vado a capo
	
	li a0, 10
	li a7, 11
	ecall
	
	# Resetto accumulatore
	
	li t2, 0
	
	# Vado avanti
	
	j avanza
	
fineStringa:

	# Stampo il valore dell'ultimo gruppo 
	
	mv a0, t2
	li a7, 1
	ecall
	
	# Termina esecuzione
	li a7, 10
	ecall
	
	