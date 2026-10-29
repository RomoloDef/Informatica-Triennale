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
    	la a0, buffer  # Carica indirizzo base in $a0
    	li a1, 26      # Alloca al massimo 24 caratteri + \n + \0
    	ecall          # $a0 contiene l'indirizzo base della stringa
# ... A QUI

##########################################
## INSERIRE IL PROPRIO CODICE QUI

	mv t0, a0	# Sposto l'indirizzo base nel registro: t0
	
	li t2, 0	# Accumulatore
	li t3, 0	# Somma delle cifre convertite
	
	li t4, 10	# Valore ASCII del carattere: '/n'
	
ciclo:

	lb t1, 0(t0)	# Carattere corrente della stringa: buffer[i]
	
	# Faccio subito il primo confronto
	
	beq t1, t4, fineStringa
	beq t1, zero, fineStringa
	
	# Carico e faccio il secondo confronto
	
	li a3, 43			# Valore ASCII del carattere: '+'
	beq t1, a3, separatore
	
	# Elaboro il bit
	addi t1, t1, -48
	
	slli t2, t2, 1
	
	add t2, t2, t1
	
	# Incremento il contatore
	
	addi t0, t0, 1
	j ciclo
	
separatore:
	
	add t3, t3, t2
	
	# Resetto accumulatore per il prossimo gruppo
	li t2, 0
	addi t0, t0, 1
	j ciclo
	
fineStringa:

	add t3, t3, t2		# Aggiungo l'ultimo numero alla somma totale

	mv a0, t3
	li a7, 1
	ecall
	
	li a0, 10
	li a7, 11
	ecall
	
	li a7, 10
	ecall


	
	

