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
.globl main

main:
    	li a7, 8       # Codice per input stringa
    	la a0, buffer  # Carica indirizzo base in a0
    	li a1, 26      # Alloca al massimo 24 caratteri + \n + \0
    	ecall          # a0 contiene l'indirizzo base della stringa
# ... A QUI

##########################################

	mv t0, a0	# Sposto l'indirizzo di base nel registro: t0
	
	li t2, 0	# Accumulatore per il valore decimale del gruppo corrente
	li t3, 1	# Prodotto finale (inizializzato a 1)
	
	li a2, 10	# Valore ASCII del carattere: '\n'
	li a3, 47	# Valore ASCII del carattere: '/'
	li a4, 65	# Valore ASCII del carattere: 'A'
	
ciclo:

	lb t1, 0(t0)	# Carattere corrente della stringa: buffer[i]
	
	# Controllo terminazione della stringa (\n o \0)
	beq t1, a2, fineStringa
	beq t1, zero, fineStringa
	
	# Controllo separatore '/'
	beq t1, a3, separatore
	
	# Verifico se è una cifra ('0'-'9') o una lettera ('A'-'F')
	bge t1, a4, è_lettera
	
	# Caso cifra '0'-'9': sottraggo 48 (ASCII '0' = 48)
	addi t1, t1, -48
	j accumula
	
è_lettera:

	# Caso lettera 'A'-'F': sottraggo 55 (ASCII 'A' = 65 -> 65 - 55 = 10)
	addi t1, t1, -55

accumula:

	# Inserisco la cifra esadecimale nell'accumulatore (shifto di 4 bit e sommo)
	slli t2, t2, 4
	add t2, t2, t1
	
	# Avanzo al carattere successivo
	addi t0, t0, 1
	j ciclo

separatore:

	# Fine di un gruppo: moltiplico il valore accumulato per il totale
	mul t3, t3, t2
	
	# Resetto l'accumulatore per il gruppo successivo
	li t2, 0
	
	# Salto oltre il carattere '/' e continuo
	addi t0, t0, 1
	j ciclo

fineStringa:

	# Moltiplico anche l'ultimo gruppo (dopo l'ultimo '/')
	mul t3, t3, t2
	
	# Stampa del prodotto finale
	mv a0, t3
	li a7, 1
	ecall
	
	# Fine programma
	li a7, 10
	ecall
