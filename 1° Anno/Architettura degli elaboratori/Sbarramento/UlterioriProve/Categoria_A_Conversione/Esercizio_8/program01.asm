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
	
	li t2, 0	# Accumulatore
	li t3, 0	# Sommatoria finale
	
	li a2, 10	# Valore ASCII del carattere: '/n'
	li a3, 47	# Valore ASCII del carattere: '/'
	li a4, 65	# Valore ASCII del carattere: 'A'

ciclo:

	lb t1, 0(t0)	# Carattere corrente della stringa: buffer[i]
	
	# Primo confronto con la terminazione della stringa
	
	beq t1, a2, fineStringa
	beq t1, zero, fineStringa
	
	# Secondo confronto con il separatore
	
	beq t1, a3, separatore
	
	# Terzo confronto per verificare se un carattere sia una cifra o una lettera
	
	bge t1, a4, è_lettera
	
	# Altrimenti è una cifra quindi
	
	addi t1, t1, -48 
	
	slli t2, t2, 4
	
	add t2, t2, t1
	
	# vado avanti
	
	addi t0, t0, 1
	j ciclo
	
è_lettera:

	addi t1, t1, -55
	
	slli t2, t2, 4
	
	add t2, t2, t1	
	
	# vado avanti
	
	addi t0, t0, 1
	j ciclo
	
separatore:

	# Una volta terminato il gruppo di cifre lo aggiungo alla somma
	
	add t3, t3, t2
	
	# Resetto l'accumulatore e passo avanti
	
	li t2, 0
	addi t0, t0, 1
	j ciclo
	
fineStringa:

	mv a0, t3
	li a7, 1
	ecall
	
	# Fine programma
	
	li a7, 10
	ecall

