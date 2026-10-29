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
	li t3, 0	# Sottrazione generale = 0
	li t5, 1	# Flag: 1 se è il primo numero, 0 altrimenti
	
	li t4, 10	# Valore ASCII del carattere:  '/n'
	
ciclo:

	lb t1, 0(t0)	# Carattere corrente della stringa: buffer[i]
	
	# Primo confronto con la terminazione della stringa
	beq t1, t4, fineStringa
	beq t1, zero, fineStringa
	
	# Carico il carattere speciale e secondo confronto 
	li a3, 45
	
	beq t1, a3, separatore
	
	# Elaboro il bit
	
	addi t1, t1, -48
	
	slli t2, t2, 1
	
	add t2, t2, t1
	
	# Incremento il contatore
	addi t0, t0, 1
	j ciclo
	
separatore:

	beq t5, zero, fai_sottrazione
	add t3, t3, t2		# È il primo numero: sommo
	li t5, 0		# Azzero il flag per i prossimi numeri
	j reset_accumulatore
	
fai_sottrazione:
	sub t3, t3, t2		# Non è il primo: sottraggo

reset_accumulatore:
	# Resetto accumulatore per il prossimo gruppo
	li t2, 0
	addi t0, t0, 1
	j ciclo
	
fineStringa:

	beq t5, zero, fine_sottrazione
	add t3, t3, t2		# Era l'unico numero: lo sommo
	j stampa
	
fine_sottrazione:
	sub t3, t3, t2		# Ultimo numero: lo sottraggo

stampa:
	mv a0, t3
	li a7, 1
	ecall
	
	li a0, 10
	li a7, 11
	ecall
	
	li a7, 10
	ecall




	


	
	

