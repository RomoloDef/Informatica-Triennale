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
	
	li t2, 0	# Accumulatore per la coppia di bit
	li t3, 0	# Contatore dei bit della coppia corrente
	li t4, 0	# Sommatoria finale
	
	li a2, 2	# Costante per la formazione di coppie
	
	li a3, 10	# Valore ASCII del carattere: '\n'
	li a4, 47	# Valore ASCII del carattere: '/'
	
ciclo:

	lb t1, 0(t0)	# Carattere corrente della stringa: buffer[i]
	
	# Controllo terminazione della stringa (\n o \0)
	beq t1, a3, fineStringa
	beq t1, zero, fineStringa
	
	# Controllo separatore '/'
	beq t1, a4, separatore
	
	# Elaboro il bit 
	addi t1, t1, -48
	
	slli t2, t2, 1
	add t2, t2, t1
	
	# Incremento il contatore di bit
	addi t3, t3, 1
	
	# Verifico se si sia formata una coppia 
	bne t3, a2, avanza
	
	# Coppia formata:
	add t4, t4, t2
	
	# Resetto accumulatore e contatore per la prossima coppia
	li t2, 0
	li t3, 0
	
avanza:

	addi t0, t0, 1
	j ciclo
	
separatore:

	# Se c'è un bit residuo (t3 == 1), paddato a sinistra diventa '0X'.
	# In base 4, il valore di '0X' è identico a X (già presente in t2).
	beq t3, zero, reset_sep
	add t4, t4, t2

reset_sep:

	li t2, 0
	li t3, 0
	addi t0, t0, 1	# Avanzo oltre il separatore '/'
	j ciclo

fineStringa:

	# Anche a fine stringa, se c'è un residuo va paddato e sommato
	beq t3, zero, stampa
	add t4, t4, t2

stampa:

	# Stampa della somma totale
	mv a0, t4
	li a7, 1
	ecall
	
	# Fine programma
	li a7, 10
	ecall
