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

	mv t0, a0	# Sposto l'indirizzo di base nel registro: t0
	
	li t3, 0	# Accumulatore
	li t4, 0	# Contatore A
	li t5, 0	# Contatore B
	
	li a2, 10	# Valore ASCII del carattere: '/n'
	
	li a3, 2	# Costante per la formazione di coppie
	li a4, 10	# Costante per la moltiplicazione per il numero decimale
	li a5, 3	# Costante per la verifica di divisibilità
	
ciclo:

	lb t1, 0(t0)	# Carattere corrente della stringa: buffer[i]
	
	# Primo confronto con la terminazione della stringa
	
	beq t1, a2, fineStringa
	beq t1, zero, fineStringa
	
	# Leggo la seconda cifra
	
	lb t2, 1(t0)	# Secondo carattere della stringa: buffer[i+1] 
	
	# Secondo confronto con la terminazione della stringa
	
	beq t2, a2, fineStringa
	beq t2, zero, fineStringa
	
	# Verifico che le cifre non siano dispari
	
	andi t6, t1, 1
	
	bne t6, zero, scarta
	
	andi t6, t2, 1
	
	bne t6, zero, scarta
	
	# Se si è arrivati fin qui entrambe le cifre sono pari quindi:
	# Elaboro i bit
	
	addi t1, t1, -48
	
	addi t2, t2, -48
	
	mul t3, t1, a4
	
	add t3, t3, t2
	
	# Una volta formata la coppia verifico che sia divisibile per tre
	
	rem t6, t3, a5
	
	beq t6, zero, è_divisibile
	
	# Altrimenti 
	
	addi t5, t5, 1
	
	j scarta
	
	
è_divisibile:

	addi t4, t4, 1
	
scarta:

	addi t0, t0, 2
	j ciclo
	
fineStringa:

	mv a0, t4
	li a7, 1
	ecall
	
	li a0, 10
	li a7, 11
	ecall
	
	mv a0, t5
	li a7, 1
	ecall
	
	# Fine programma
	
	li a7, 10
	ecall
	
	

