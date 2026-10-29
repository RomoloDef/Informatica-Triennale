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

	mv t0, a0	# Sposto l'indirizzo base nel registro: t0
	
	li t2, 0	# Accumulatore
	li t3, 0	# Contatore dei bit
	li t4, 3	# Costante per fare il confronto per la fomrazione delle terzine
	li t5, 0	# Sommatoria finale
	
	li a2, 10	# Valore ASCII del carattere: '/n'
	li a3, 57	# Valore ASCII del carattere: '9'
	li a4, 48	# Valore ASCII del carattere: '0'
	
	li a5, 10	# Costante per la moltiplicazione dell'accumulatore
	
ciclo:

	lb t1, 0(t0)	# Carattere corrente della stringa: buffer[i]
	
	# Primo confronto con la terminazione della stringa
	
	beq t1, a2, fineStringa
	beq t1, zero, fineStringa
	
	# Confronto per verificare che sia un carattere numerico
	
	bgt t1, a3, avanza
	blt t1, a4, avanza
	
	# Elaboro il bit
	
	addi t1, t1, -48
	
	mul t2, t2, a5
	
	add t2, t2, t1
	
	# Incremento il contatore dei bit
	
	addi t3, t3, 1
	
	# Verifico che si sia formata una terzina
	
	bne t3, t4, avanza
	
	# Se si è formata aggiungiamo la terzina alla sommatoria
	
	add t5, t5, t2
	
	# Resetto
	
	li t2, 0
	li t3, 0

avanza:

	addi t0, t0, 1
	j ciclo
	
fineStringa:

	mv a0, t5
	li a7, 1
	ecall
	
	# Fine programma
	
	li a7, 10
	ecall

	

