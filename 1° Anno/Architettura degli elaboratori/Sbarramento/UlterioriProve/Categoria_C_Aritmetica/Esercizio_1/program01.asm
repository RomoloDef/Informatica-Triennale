##########################################
# INSERIRE I PROPRI DATI QUI
# Nome: Romolo
# Cognome: Deffereria
# Matricola: 2114887
##########################################

.data
    buffer: .space 26

.text
main:
    li a7, 8       # Syscall per lettura stringa
    la a0, buffer  # Indirizzo base
    li a1, 26      # Lunghezza massima
    ecall

##########################################
# INSERIRE IL PROPRIO CODICE QUI

	mv t0, a0	# Sposto l'indirizzo di base nel registro: t0
	
	li t2, 0	# Accumulatore
	li t3, 0	# Somma
	
	li t4, 10	# Valore ASCII del carattere '/n'
	
ciclo:
	
	lb t1, 0(t0)	# Carattere corrente della stringa: buffer[i]
	
	# Primo confronto sulla terminazione della stringa
	
	beq t1, t4, fineStringa
	beq t1, zero, fineStringa
	
	# Carico il carattere speciale e faccio il secondo confronto
	
	li a3, 43
	
	beq t1, a3, sommatoria
	
	# Elaboro il bit
	
	addi t1, t1, -48
	
	slli t2, t2, 1
	
	add t2, t2, t1
	
	# Incremento il contatore
	
	addi t0, t0, 1
	j ciclo
	
sommatoria:

	add t3, t3, t2
	
	li t2, 0
	addi t0, t0, 1
	j ciclo
	
fineStringa:

	add t3, t3, t2

	mv a0, t3
	li a7, 1
	ecall
	
	li a0, 10
	li a7, 11
	ecall
	
	# Fine Programma
	li a7, 10
	ecall
	
	
