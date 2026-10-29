##########################################
# INSERIRE I PROPRI DATI QUI
# Nome: Romolo
# Cognome: Deffereria
# Matricola: 2114887
##########################################

# NON MODIFICARE IL CODICE DA QUI...
.data
    buffer: .space 50

.text

main:
    li a7, 8       # Codice per input stringa
    la a0, buffer  # Carica indirizzo base in a0
    li a1, 50      # Alloca al massimo 48 caratteri + \n + \0
    ecall          # a0 contiene l'indirizzo base della stringa di input
# ... A QUI

##########################################
## INSERIRE IL PROPRIO CODICE QUI

	mv t0, a0	# Sposto l'indirizzo base nel registro: t0
	
	li t2, 0	# Accumulatore
	
	li a2, 10	# Valore ASCII per il carattere: '/n'
	
ciclo:

	lb t1, 0(t0)	# Carattere corrente della stringa: buffer[i]
	
	# Primo confronto con la terminazione della stringa
	
	beq t1, a2, fineStringa
	beq t1, zero, fineStringa
	
	# Verifico che il carattere sia una lettera o un numero
	
	li a4, 97	# Valore ASCII del carattere 'a'
	
	bge t1, a4, è_lettera
	
	# Altrimenti è un numero
	
	addi t1, t1, -48
	
	j accumula
	
è_lettera:

	addi t1, t1, -87
	
accumula:

	add t3, t3, t1
	
	# Vado avanti
	
	addi t0, t0, 1
	j ciclo
	
fineStringa:

	li a0, 0x3e
	li a7, 11
	ecall

	mv a0, t3
	li a7, 34
	ecall
	
	# Se la somma ha già una sola cifra terminiamo
	
	li t4, 15
	ble t3, t4, termina
	
	# Altrimenti si riduce	
	
riduci:

	li t5, 0		# t5 = nuova somma delle cifre 
	
estrai_cifre:

	andi t6, t3, 0xF	# t6 = estrae gli ultimi 4 bit (cifra hex da 0 a 15)
	add t5, t5, t6		# somma la cifra
	srli t3, t3, 4		# shifta a destra di 4 bit per la cifra successiva
	
	bne t3, zero, estrai_cifre
	
	mv t3, t5
	
	# Stampa del nuovo risultato intermedio (>0x...)
	li a0, '>'
	li a7, 11
	ecall
	
	mv a0, t3
	li a7, 34
	ecall
	
	# Se la nuova somma è ancora > 15, reitera!
	bgt t3, t4, riduci
	
termina:

	
	li a0, 10
	li a7, 11
	ecall
	
	# Fine programma
	li a7, 10
	ecall
	
	
	
	
	
	
	
	
	
	
	