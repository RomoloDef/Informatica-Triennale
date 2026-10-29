##########################################
# INSERIRE I PROPRI DATI QUI
# Nome:	Romolo
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

	mv t0, a0	# Sposto l'indirizzo di base nel registro: t0
	
	li t2, 0	# Accumulatore
	li t3, 0	# Contatore di bit
	li t4, 3	# Costante per la formazione di terzine
	li t5, 0	# Flag di stampa: 0 se non stampa, 1 se stampa
	
	li a2, 10	# Valore ASCII del carattere: '/n'
	
ciclo:

	lb t1, 0(t0)	# Carattere corrente della stringa: buffer[i]
	
	# Primo confronto con la terminazione della stringa
	
	beq t1, a2, fineStringa
	beq t1, zero, fineStringa
	
	# Secondo confronto con il separatore
	
	li a3, 47
	beq t1, a3, separatore
	
	# Elaboro il bit
	
	addi t1, t1, -48
	
	slli t2, t2, 1
	
	add t2, t2, t1
	
	# Incremento il contatore di bit
	
	addi t3, t3, 1
	
	# Verifico se si sia formata una terzina
	
	bne t3, t4, avanza
	
	# Altrimenti si è formata, la posso stampare!
	
	mv a0, t2
	li a7, 1
	ecall
	
	# Resetto i registri e setto il flag
	
	li t2, 0
	li t3, 0
	li t5, 1
	
avanza:

	addi t0, t0, 1
	j ciclo
	
separatore:

	# Nel caso ci fossero delle triple non complete e quindi non formate bisogna skippare
	
	beq t5, zero, skip
	
	# Vado a capo
	
	li a0, 10
	li a7, 11
	ecall
	
skip:

	li t2, 0
	li t3, 0
	li t5, 0
	
	addi t0, t0, 1
	j ciclo
	
fineStringa:

	# Verifico
	
	beq t5, zero, esci
	
	li a0, 10
	li a7, 11
	ecall
		
esci:

	# Fine programma
	
	li a7, 10
	ecall
	
	
	
		


