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

	mv t0, a0	# Sposto l'indirizzo base della stringa nel registro: t0
	
	li t3, 0	# Somma aritmetica
	
	li t5, 10	# Valore ASCII del carattere: '/n'
	
ciclo:

	lb t1, 0(t0)	# Carattere corrente stringa: buffer[i]
	
	# Faccio il primo confronto con la terminazione della stringa
	
	beq t1, t5, fineStringa
	beq t1, zero, fineStringa
	
	# Carico anche il secondo carattere della stringa
	
	lb t2, 1(t0)	# buffer[i+1]
	
	# Faccio il secondo confronto per il secondo carattere che se è unico allora è considerata un'unità
	
	beq t2, t5, unità
	beq t2, zero, unità
	
	# Elaboro entrambi i bit
	
	addi t1, t1, -48
	addi t2, t2, -48
	
	# Formo il numero decimale: decine * 10 + unità
	
	li a3, 10
	
	mul t4, a3, t1
	
	add t4, t4, t2
	
	# Avanzo
	addi t0, t0, 2
	j Confronto50
	
unità:
	
	addi t1, t1, -48
	mv t4, t1
	addi t0, t0, 1
	j Confronto50	
	
Confronto50:
	
	# Ora che ho formato il numero posso fare il confronto per la somma
	# Carico il valore da rimuovere
	
	li a4, 50
	
	ble t4, a4, ciclo
	
sommatoria:
	
	add t3, t3, t4
	j ciclo
	
fineStringa:

	mv a0, t3
	li a7, 1
	ecall
	
	# Fine Programma
	li a7, 10
	ecall
