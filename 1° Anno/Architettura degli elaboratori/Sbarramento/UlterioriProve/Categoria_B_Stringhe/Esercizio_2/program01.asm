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
    
    li t2, 0	# Numero di cifre pari
    li t3, 0	# Somma delle cifre pari
    li t4, 10	# Valore ASCII del carattere: '/n'
    
ciclo:

	lb t1, 0(t0)	# Carattere corrente della stringa: buffer[i]
	
	# Primo confronto con la terminazione della stringa
	
	beq t1, t4, fineStringa
	beq t1, zero, fineStringa
	
	# Elaboro il bit
	
	addi t1, t1, -48
	
	# Faccio il secondo confronto considerando se è pari oppure no
	
	andi t5, t1, 1
	
	bnez t5, avanza
	
	addi t2, t2, 1
	add t3, t3, t1
	
avanza:

	addi t0, t0, 1
	j ciclo
	
fineStringa:

	mv a0, t2
	li a7, 1
	ecall
	
	li a0, 10
	li a7, 11
	ecall
	
	mv a0, t3
	li a7, 1
	ecall
	
	# Fine programma
	li a7, 10
	ecall

