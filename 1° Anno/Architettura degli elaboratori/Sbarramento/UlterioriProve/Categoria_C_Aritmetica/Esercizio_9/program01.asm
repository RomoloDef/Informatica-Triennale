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

main:
    	li a7, 8       # Codice per input stringa
    	la a0, buffer  # Carica indirizzo base in a0
    	li a1, 26      # Alloca al massimo 24 caratteri + 
	ecall          # a0 contiene l'indirizzo base della stringa
# ... A QUI

##########################################

	mv t0, a0	# Sposto l'indirizzo base nel registro: t0
	
	li t2, 0	# Accumulatore
	li t3, 0	# Sommatoria
	
	li a2, 10	# Valore ASCII del carattere: '/n'
	li a3, 43	# Valore ASCII del carattere: '+'
	
ciclo:

	lb t1, 0(t0)	# Carattere corrente della stringa: buffer[i]
	
	# Primo confronto con la terminazione della stringa
	
	beq t1, a2, fineStringa
	beq t1, zero, fineStringa
	
	# Secondo confronto con il carattere speciale
	
	beq t1, a3, sommatoria
	
	# Elaboro il bit
	
	addi t1, t1, -48
	
	slli t2, t2, 2
	
	add t2, t2, t1
	
	# Incremento e vado avanti
	
	addi t0, t0, 1
	j ciclo
	

sommatoria:
	
	# Aggiungo il valore formato alla sommatoria
	
	add t3, t3, t2
	
	# Resetto l'accumulatore
	
	li t2, 0
	
	# Incremento e vado avanti
	
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
