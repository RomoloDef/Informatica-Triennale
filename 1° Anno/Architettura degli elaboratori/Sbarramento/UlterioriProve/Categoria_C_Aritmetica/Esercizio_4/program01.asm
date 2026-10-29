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

	mv t0, a0	# Sposto l'indirizzo base nel registro: t0
	
	li t2, 0	# Accumulatore
	li t3, 0	# Somma
	
	li t5, 10	# Valore ASCII del carattere: '/n'
	
ciclo:

	lb t1, 0(t0)	# Carattere corrente della stringa buffer[i]
	
	# Primo confronto con la terminazione della stringa
	
	beq t1, t5, fineStringa
	beq t1, zero, fineStringa
	
	# Carico il carattere speciale e faccio il Secondo confronto
	
	li a3, 43
	
	beq t1, a3, verifica
	
	# Elaboro il bit
	
	addi t1, t1, -48
	
	slli t2, t2, 1
	
	add t2, t2, t1
	
	# Incremento il contatore
	
	addi t0, t0, 1
	j ciclo
	
verifica:

	# Verifico che il numero convertito sia maggiore o uguale a 5
	
	li a4, 5
	
	bge t2, a4, sommatoria
	
	# Se cosi non fosse azzero l'accumulatore, incremento il contatore e torno al ciclo
	li t2, 0
	addi t0, t0, 1
	j ciclo
	
sommatoria:

	# Se il numero è maggiore o uguale a 5 lo aggiungiamo alla somma
	add t3, t3, t2
	li t2, 0
	addi t0, t0, 1
	j ciclo
	
fineStringa:

	# Verifico che anche l'ultimo numero sia in t2
	li a4, 5
	
	ble t2, a4, stampa_finale
	
	add t3, t3, t2
	
stampa_finale:

	mv a0, t3
	li a7, 1
	ecall
	
	# fine programma
	
	li a7, 10
	ecall


