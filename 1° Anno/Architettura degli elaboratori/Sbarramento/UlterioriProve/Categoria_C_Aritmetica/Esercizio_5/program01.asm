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

	mv t0, a0	# Sposto l'indirizzo base nel registro: t0
	
	li t2, 0	# Accumulatore
	li t3, 0	# Sommatoria
	
	li t6, 10	# Valore ASCII del carattere: '/n'
	
ciclo:

	lb t1, 0(t0)	# Carattere corrente della stringa: buffer[i]
	
	# Primo confronto con la terminazione della stringa
	
	beq t1, t6, fineStringa
	beq t1, zero, fineStringa
	
	# Carico il carattere speciale
	
	li a2, 43
	
	beq t1, a2, sommatoria
	
	# Elaboro il bit e lo converto in decimale
	
	addi t1, t1, -48
	
	slli t2, t2, 2
	
	add t2, t2, t1
	
	# Avanzo l'indice per lo scorrimento
	
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
	
	# Fine programma
	li a7, 10
	ecall
