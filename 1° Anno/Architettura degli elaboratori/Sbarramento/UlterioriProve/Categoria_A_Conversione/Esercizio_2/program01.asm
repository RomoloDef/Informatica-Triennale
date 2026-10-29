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
	
	li t2, 0	# Accumulatore
	li t3, 2	# Costante per il confronto sulla coppia: 2
	li t4, 0	# Contatore dei bit
	
	li t5, 10	# Valore ASCII del carattere: '/n'
	
	li t6, 0	# Flag per la stampa
	
ciclo:

	lb t1, 0(t0)	# Carattere corrente della stringa: buffer[i]
	
	# Primo confronto con la terminazione della stringa
	
	beq t1, t5, fineStringa
	beq t1, zero, fineStringa
	
	# Carico il carattere speciale
	
	li a3, 45
	
	beq t1, a3, separatore
	
	# Elaboro il bit
	
	addi t1, t1, -48
	
	slli t2, t2, 1
	
	add t2, t2, t1
	
	# Incremento il contatore dei bit
	
	addi t4, t4, 1
	
	# Verifico se si è formata una coppia
	
	bne t4, t3, avanza
	
	# Se la coppia è formata allora va stampato il valore
	mv a0, t2
	li a7, 1
	ecall
	
	# Resetto
	li t2, 0
	li t4, 0
	li t6, 1
	
	
avanza:
	addi t0, t0, 1
	j ciclo
		
separatore:

	beq t6, zero, skip
	
	li a0, 10
	li a7, 11
	ecall
	
skip:

	li t2, 0
	li t4, 0
	li t6, 0
	j avanza

fineStringa:

	beq t6, zero, esci
	li a0, 10
	li a7, 11
	ecall
	
esci:

	li a7, 10
	ecall

