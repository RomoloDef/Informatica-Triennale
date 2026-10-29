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

	
	mv t0, a0	# Sposto l'indirizzo di base nel registro: t0
	
	li t2, 0	# Accumulatore della coppia
	li t3, 0	# Contatore dei bit
	li t4, 2	# Costante per il confronto ---> 2 per la coppia
	li t5, 0	# Flag per la stampa
	
	li t6, 10	# Valore ASCII: '\n'
	
ciclo:

 	lb  t1, 0(t0)	# Carico il carattere corrente della stringa
 	
 	# Inizio con i primi confronti sulla terminazione della stringa
 	
 	beq t1, t6, fineStringa
 	beq t1, x0, fineStringa
 	
 	# Passo al confronto sul carattere speciale
 	
 	li a3, 47
 	beq t1, a3, separatore
 	
 	# Converto il valore ASCII in carattere numerico
 	addi t1, t1, -48
 	
 	slli t2, t2, 1
 	
 	add t2, t2, t1
 	
 	# Aumento il contatore di bit
 	
 	addi t3, t3, 1
 	
 	# Posso fare il terzo confronto per verificare se la coppia sia completa
 	bne t3, t4, avanza
 	
 	# Se la coppia è completa posso eseguire la stampa
 	mv a0, t2
 	li a7, 1
 	ecall
 	
 	# E qui vado a resettare i registri e a impostare il flag di stampa a 1
 	li t2, 0
 	li t3, 0
 	li t5, 1 
 	
 	
avanza:
 	addi t0, t0, 1
 	j ciclo
 		
separatore:
 	beq t5, x0, skip_newline
 	
 	li a0, 10
 	li a7, 11
 	ecall
 	
skip_newline:

	# Resetto tutto
	li t2, 0
	li t3, 0
	li t5, 0
	addi t0, t0, 1
	j ciclo
 	 
fineStringa: 

	beq t5, x0, esci
	
	li a0, 10
	li a7, 11
	ecall

esci:
	li a7, 10
	ecall
