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

	mv t0, a0	# Sposto l'indirizzo base nel registro: t0
	
	li t2, 0	# Accumulatore
	li t3, 0	# Sommatoria totale
	li t4, 0	# Flag: '0' se devo fare la somma, '1' se devo fare la differenza
	
	li a2, 10	# Valore ASCII del carattere: '/n'
	
ciclo:

	lb t1, 0(t0)	# Carattere corrente della stringa: buffer[i]
	
	# Primo confronto con la terminazione della stringa
	
	beq t1, a2, fineStringa
	beq t1, zero, fineStringa
	
	# Secondo confronto con il separatore
	
	li a3, 45	# Valore ASCII del carattere: '-'
	
	beq t1, a3, separatore
	
	# Elaboro il bit
	
	addi t1, t1, -48
	
	slli t2, t2, 1
	
	add t2, t2, t1
	
	# Andiamo avanti
	
	addi t0, t0, 1
	j ciclo
	
separatore:

	beq t4, zero, fai_somma
	
	# Altrimenti devo fare l'operazione di differenza
	
	sub t3, t3, t2
	
	# Resetto l'accumulatore
	
	li t2, 0
	
	# Vado avanti
	
	addi t0, t0, 1
	j ciclo
	
fai_somma:

	add t3, t3, t2
	
	# Setto il flag a 1 per fare d'ora in poi la differenza
	
	li t4, 1
	
	# Resetto l'accumuòatore
	
	li t2, 0
	
	# E posso andare avanti
	
	addi t0, t0, 1
	j ciclo	
	
fineStringa:

	# Alla fine devo comunque fare il controllo sul flag
	
	beq t4, zero, somma
	
	# Altrimenti faccio differenza:
	
	sub t3, t3, t2
	
	j esci
	
	
somma:

	add t3, t3, t2

esci:

	# Ora posso stampare la somma
	
	mv a0, t3
	li a7, 1
	ecall
	
	# Vado a capo
	
	li a0, 10
	li a7, 11
	ecall
	
	# Fine programma
	
	li a7, 10
	ecall

	
	
	
	

	


	
	

