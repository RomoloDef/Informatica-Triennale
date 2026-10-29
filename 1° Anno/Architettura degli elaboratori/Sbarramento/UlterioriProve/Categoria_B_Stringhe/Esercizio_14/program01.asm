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
    	li a1, 26      # Alloca al massimo 24 caratteri + \n + \0
    	ecall          # a0 contiene l'indirizzo base della stringa
# ... A QUI

##########################################
# INSERIRE IL PROPRIO CODICE QUI

	mv t0, a0	# Sposto l'indirizzo di base nel registro: t0
	
	li t3, 0	# Totale pari
	li t4, 0	# Totale dispari
	
	li a2, 10	# Valore ASCII del carattere: '/n'
	li a3, 10	# Costante per la creazione del numero decimale
	
ciclo:

	lb t1, 0(t0)	# Carattere corrente della stringa: buffer[i]
	lb t2, 1(t0)	# Carattere successivo della stringa: buffer[i+1]
	
	# Primo confronto con la terminazione della stringa
	
	beq t1, a2, fineStringa
	beq t1, zero, fineStringa
	
	# Secondo confronto con la terminazione della stringa
	
	beq t2, a2, fineStringa
	beq t2, zero, fineStringa
	
	# Elaboro le due cifre
	
	addi t1, t1, -48
	addi t2, t2, -48
	
	# Formo il numero decimale
	
	mul t1, t1, a3
	add t1, t1, t2
	
	# Verifico che questo numero sia pari o dispari
	
	andi t5, t1, 1
	
	beq t5, zero, è_pari
	
	# Altrimenti è dispari
	
	add t4, t4, t1
	
avanza:

	addi t0, t0, 2
	j ciclo
	
è_pari:

	add t3, t3, t1
	j avanza
	
fineStringa:

	# Stampo i totali
	
	mv a0, t3
	li a7, 1
	ecall
	
	li a0, 10
	li a7, 11
	ecall
	
	mv a0, t4
	li a7, 1
	ecall
	
	# Fine programma
	
	li a7, 10
	ecall
	
	
	
	

