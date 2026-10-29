##########################################
# INSERIRE I PROPRI DATI QUI
# Nome: Romolo
# Cognome: Deffereria
# Matricola: 2114887
##########################################

.data
    buffer: .space 26

.text
main:
    	li a7, 8       # Syscall per lettura stringa
    	la a0, buffer  # Indirizzo base
    	li a1, 26      # Lunghezza massima
    	ecall

##########################################
# INSERIRE IL PROPRIO CODICE QUI

	mv t0, a0	# Indirizzo base stringa
	
	li t3, 0	# Sommatoria finale
	li t2, 0	# Stato: 0 = cerco la prima cifra, 1 = cerco la seconda cifra
	
	li t6, 10	# Valore ASCII di '\n'
	li a2, 57	# Valore ASCII di '9'
	li a3, 48	# Valore ASCII di '0'

ciclo:
	lb t1, 0(t0)	# Carattere corrente
	
	# Controllo terminazione stringa
	beq t1, t6, fineStringa
	beq t1, zero, fineStringa
	
	# Verifico se t1 è una cifra decimale ('0' <= t1 <= '9')
	blt t1, a3, avanza		# Minore di '0': scarta
	bgt t1, a2, avanza		# Maggiore di '9': scarta
	
	# Se è una cifra, converto da ASCII a valore (0-9)
	addi t1, t1, -48
	
	# Verifico se è la prima cifra o la seconda della coppia
	bne t2, zero, seconda_cifra
	
	# --- PRIMA CIFRA (DECINA) ---
	mv s1, t1			# Salvo la prima cifra in s1
	li t2, 1			# Imposto lo stato: ora cerco la seconda cifra
	j avanza

seconda_cifra:
	# --- SECONDA CIFRA (UNITÀ) ---
	mv s2, t1			# Salvo la seconda cifra in s2
	li t2, 0			# Resetto lo stato per la prossima coppia
	
	# Formo il numero a due cifre: s1 * 10 + s2
	li a5, 10
	mul t4, s1, a5
	add t4, t4, s2
	
	# Verifico divisibilità per 4
	li a4, 4
	rem t5, t4, a4
	beq t5, zero, e_divisibile
	
	j avanza

e_divisibile:
	add t3, t3, t4			# Aggiungo alla sommatoria

avanza:
	addi t0, t0, 1			# Avanza al carattere successivo
	j ciclo

fineStringa:
	mv a0, t3
	li a7, 1
	ecall
	
	# Fine programma
	li a7, 10
	ecall
