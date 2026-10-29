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

	mv t0, a0	# Sposto l'indirizzo base nel registro: t0
	
	li t2, 0	# Contatore di bit
	li t3, 0	# Somma delle 3 cifre
	li t4, 0	# Contatore A: contatore delle somme pari
	li t5, 0	# Contatore B: contatore delle somme dispari
	
	li a2, 3	# Costante per la verifica delle triple
	
	li a3, 10	# Valore ASCII del carattere: '/n'
	
ciclo:

	lb t1, 0(t0)	# Carattere corrente della stringa: buffer[i]
	
	# Primo confronto con la terminazione della stringa
	
	beq t1, a3, fineStringa
	beq t1, zero, fineStringa
	
	# Elaboro il bit
	
	addi t1, t1, -48
	
	# Aggiungo la cifra alla somma, incremento il contatore dei bit e verifico se si sia formata una tripla
	
	add t3, t3, t1
	
	addi t2, t2, 1
	
	beq t2, a2, tripla_formata
	
	# Altrimenti andiamo avanti con il ciclo
	
	j avanza
	
tripla_formata:

	# Se la tripla è stata formata allora lo è anche la somma
	# Verifico se la somma sia pari o dispari
	
	andi t6, t3, 1
	
	beq t6, zero, è_pari
	
	# Altrimenti è dispari e bisogna incrementari il contatore B
	
	addi t5, t5, 1	
	
	# Resetto i registri
	
	li t2, 0
	li t3, 0
	
	j avanza
	
è_pari:

	addi t4, t4, 1
	
	# Resetto i registri
	
	li t2, 0
	li t3, 0
	
avanza:

	addi t0, t0, 1
	j ciclo
	
fineStringa:

	mv a0, t4
	li a7, 1
	ecall
	
	li a0, 10
	li a7, 11
	ecall
	
	mv a0, t5
	li a7, 1
	ecall
	
	# Fine programma
	
	li a7, 10
	ecall
