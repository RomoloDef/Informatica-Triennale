##########################################
# INSERIRE I PROPRI DATI QUI
# Nome: Romolo
# Cognome: Deffereria
# Matricola: 2114887
##########################################

# NON MODIFICARE QUESTA PARTE
.data
    buffer: .space 20 # Allocazione di 20 byte per la stringa

.text

main:
    li a7, 8       # Codice per input stringa
    la a0, buffer  # Carica indirizzo base in $a0
    li a1, 20      # Alloca al massimo 20 caratteri
    ecall          # $a0 contiene l'indirizzo base della stringa


##########################################
## INSERIRE IL CODICE QUI

	mv t0, a0	# Sposto l'indirizzo di base nel registro: t0
	
	li t3, 0	# Sommatoria finale
	li t4, 0	# Numero totale di cifre
	
	li a2, 10	# Valore ASCII del carattere: '/n'
	
ciclo:

	lb t1, 0(t0)	# Carattere corrente della stringa: buffer[i]
	
	# Primo confronto con la terminazione della stringa
	
	beq t1, a2, fineStringa
	beq t1, zero, fineStringa
	
	# Elaboro il bit
	
	addi t1, t1, -48
	
	# Carico il carattere successivo della stringa
	
	lb t2, 1(t0)
	
	# Secondo confronto con la terminazione della stringa - se il carattere successivo è '/n' va sommato solo la cifra singola
	
	beq t2, a2, cifra_singola
	beq t2, zero, cifra_singola
	
	# Elaboro il bit
	
	addi t2, t2, -48
	
	# Formo il numero decimale da sommare alla sommatoria finale
	
	li a3, 10	# Costante per la formazione
	
	mul t1, t1, a3
	add t1, t1, t2
	
	# Aggiungo alla sommatoria finale
	
	add t3, t3, t1
	
	# Incremento il numero totale di cifre
	
	addi t4, t4, 2
	
	# Avanzo di coppia in coppia
	
	addi t0, t0, 2
	j ciclo
	
cifra_singola:

	# Se l'ultima cifra è '/n', devo sommare solamente t1
	
	add t3, t3, t1
	
	# Si aggiunge 1
	
	addi t4, t4, 1
	
fineStringa:

	# Stampo i valori richiesti
	
	mv a0, t3
	li a7, 1
	ecall
	
	# Vado a capo
	
	li a0, 10
	li a7, 11
	ecall
	
	# Secondo valore
	
	mv a0, t4
	li a7, 1
	ecall
	
	# Fine programma
	
	li a7, 10
	ecall
	
    


