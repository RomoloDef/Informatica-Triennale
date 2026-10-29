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

    	li a7, 8       # Code for string input
    	la a0, buffer  # Load base address in a0
    	li a1, 20      # Allocate at most 20 characters
    	ecall          # a0 contains the base address of the string

##########################################

	mv t0, a0	# Sposto l'indirizzo di base nel registro: t0
	
	li t3, 0	# Occorrenze numeri divisibili per 4
	li t4, 0	# Occorrenze numeri non divisibili per 4
	
	li a2, 10	# Valore ASCII del carattere: '/n'
	
ciclo:

	lb t1, 0(t0)	# Carattere corrente della stringa: buffer[i]
	lb t2, 1(t0)	# Carattere successivo della stringa: buffer[i+1]
	
	# Primo controllo sulla terminazione della stringa
	
	beq t1, a2, fineStringa
	beq t1, zero, fineStringa
	
	# Secondo controllo - se il carattere successivo è '/n' allora va elaborata la cifra singola
	
	beq t2, a2, cifra_singola
	beq t2, zero, cifra_singola
	
	# Terzo controllo - le cifre non devono essere '9'
	
	li a3, 57	# Valore ASCII del carattere '9'
	
	beq t1, a3, avanza
	beq t2, a3, avanza
	
	# Ora posso elaborare i due bit
	
	addi t1, t1, -48
	addi t2, t2, -48
	
	# Formo il numero decimale
	
	li a4, 10	# Costante per la formazione del numero
	
	mul t1, t1, a4
	add t1, t1, t2
	
	# Verifico se la coppia sia divisibile per 4 o meno
	
	li a5, 4	# Costante per la verifica
	
	rem t5, t1, a5
	
	beq t5, zero, è_divisibile
	
	# Altrimenti non lo è - incremento le occorrenze 
	
	addi t4, t4, 1
	
avanza:

	addi t0, t0, 2
	j ciclo
	
è_divisibile:

	# Incremento le occorrenze dei divisibili
	
	addi t3, t3, 1
	j avanza
	
cifra_singola:

	# Nel caso fossimo alla fine e non si è formata una coppia, va comunque elaborata la cifra singola (t1)
	
	li a5, 4	# Costante per la verifica
	
	rem t5, t1, a5
	
	beq t5, zero, è_divisibile
	
	# Altrimenti non lo è - incremento le occorrenze 
	
	addi t4, t4, 1
	
fineStringa:

	# Stampo le occorrenze
	
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

	



