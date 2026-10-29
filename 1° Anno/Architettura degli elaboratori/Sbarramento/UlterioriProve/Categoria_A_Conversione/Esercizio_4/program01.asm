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
	
	li t5, 10	# Valore ASCII per il carattere: '/n'
	
ciclo:

	lb t1, 0(t0)	# Carattere corrente della stringa: buffer[i]
	
	# Primo confronto con la terminazione della stringa
	
	beq t1, t5, fineStringa
	beq t1, zero, fineStringa
	
	# Elaboro il bit - essendo esadecimale non posso con slli
	
	addi t1, t1, -48
	
	li a2, 10	# Costante per moltiplicare
	mul t2, t2, a2
	add t2, t2, t1
	
avanza:

	addi t0, t0, 1
	j ciclo
	
fineStringa:

	# Stampo
	
	mv a0, t2
	li a7, 34
	ecall
	
	# Fine programma
	
	li a7, 10
	ecall
	
	
