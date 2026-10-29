##########################################
# INSERIRE I PROPRI DATI QUI
# Nome: Romolo
# Cognome: Deffereria
# Matricola: 2114887
##########################################

# NON MODIFICARE QUESTA PARTE
.data
    buffer: .space 20

.text

main:
    	li a7, 8       # Codice per input stringa
    	la a0, buffer  # Carica indirizzo base in $a0
    	li a1, 20      # Alloca al massimo 20 caratteri
    	ecall          # $a0 contiene l'indirizzo base della stringa

##########################################
## INSERIRE IL CODICE QUI

	mv t0, a0	# Sposto l'indirizzo di base nel registro: t0
	
	li t3, 0	# Numero di occorrenze in cui un carattere è preceduto da uno identico
	li t4, 0	# Somma totale dei valori numerici presi una cifra alla volta
	
	li a2, 10	# Valore ASCII del carattere: '/n'
	
ciclo:

	lb t1, 0(t0)	# Carattere corrente della stringa: buffer[i]
	
	# Primo confronto con la terminazione della stringa
	
	beq t1, a2, fineStringa
	beq t1, zero, fineStringa
	
	# Elaboro il bit
	
	addi t1, t1, -48
	
	# Progressivamente calcolo la somma
	
	add t4, t4, t1
	
	# Secondo carattere
	
	lb t2, 1(t0)	# Carattere successivo della stringa: buffer[i+1]
	
	# Elaboro il bit
	
	addi t2, t2, -48
	
	# Verifico se i due simboli sono uguali
	
	beq t1, t2, sono_uguali
	
avanza:
	
	addi t0, t0, 1
	j ciclo
	
sono_uguali:

	addi t3, t3, 1
	j avanza

fineStringa:

	mv a0, t3
	li a7, 1
	ecall
	
	li a0, 10
	li a7, 11
	ecall
	
	mv a0, t4
	li a7, 1
	ecall
	
	# Fine programma
	
	li a7, 10
	ecall


	
