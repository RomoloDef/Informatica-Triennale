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
	
	li t2, 0	# Numero totale di cifre maggiori di 5 su TUTTI i segmenti
	li t3, 0	# Numero totale di segmenti trovati nella stringa
	li t4, 5	# Costante con cui fare il confronto
	
	li t6, 10	# Valore ASCII del carattere: '/n'
	
ciclo:

	lb t1, 0(t0)	# Carattere corrente della stringa: buffer[i]
	
	# Primo confronto con la terminazione della stringa
	
	beq t1, t6, fineStringa
	beq t1, zero, fineStringa
	
	# Carico il carattere speciale
	
	li a2, 63
	
	beq t1, a2, separatore
	
	# Elaboro il bit
	
	addi t1, t1, -48
	
	# Verifico che la cifra sia maggiore di 5
	
	bgt t1, t4, maggioreCinque
	
	# Altrimenti incremento il contatore e non la conto
	
	addi t0, t0, 1
	j ciclo
	
maggioreCinque:

	# Se la cifra è maggiore di cinque allora aumento il numero totale di cifre
	
	addi t2, t2, 1
	
	# Incremento il contatore e continuo il ciclo
	
	addi t0, t0, 1
	j ciclo
	
separatore:

	# Quando l'indice di scorrimento incontra il carattere '?' deve incrementare il contatore di segmenti
	
	addi t3, t3, 1
	
	# Incremento il contatore e continuo il ciclo
	
	addi t0, t0, 1
	j ciclo
	
fineStringa:

	# Alla fine della stringa anche se non è presente il carattere '?' il segmento finale va comunque contato
	# Di conseguenza incremento di uno il contatore di segmenti
	
	addi t3, t3, 1
	
	# Ora posso stampare
	
	mv a0, t2
	li a7, 1
	ecall
	
	# A capo
	
	li a0, 10
	li a7, 11
	ecall
	
	# Seconda stampa
	
	mv a0, t3
	li a7, 1
	ecall
	
exit:

	# Fine programma
	
	li a7, 10
	ecall
	

	

