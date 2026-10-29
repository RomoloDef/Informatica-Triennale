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
	
	li t2, 0	# Inizializzo un indice fittizio: i = 1,2,3,4, ..., n
	li t3, 0	# Somma
	
	li t4, 10	# Valore ASCII del carattere: '/n'
	
ciclo:

	lb t1, 0(t0)	# Carattere corrente della stringa[i]
	
	# Primo confronto con la terminazione della stringa
	
	beq t1, t4, fineStringa
	beq t1, zero, fineStringa
	
	# Elaboro il bit
	
	addi t1, t1, -48
	
	# Verifico la posizione pari o dispari dell'indice
	
	andi t5, t2, 1
	
	beq t5, zero, è_pari
	
	# Altrimenti scorri l'indice e ignora la cifra
	
	addi t2, t2, 1
	
	addi t0, t0, 1
	
	j ciclo
	
è_pari:

	# Se è pari va aggiunta la cifra alla somma
	
	add t3, t3, t1
	
	# Incremento l'indice
	
	addi t2, t2, 1
	addi t0, t0, 1
	j ciclo
	
fineStringa:

	mv a0, t3
	li a7, 1
	ecall
	
	li a7, 10
	ecall
	
	
