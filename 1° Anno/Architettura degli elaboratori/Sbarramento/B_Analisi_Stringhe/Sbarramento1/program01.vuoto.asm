##########################################
# INSERIRE I PROPRI DATI QUI
# Nome:	Romolo
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
	
	li t2, 0	# Occorrenze numeri pari
	li t3, 0	# Occorrenze numeri dispari
	
	li a2, 10	# Valore ASCII del carattere: '/n'
	
	# Per escludere il primo carattere vado direttamente avanti con l'indice
	
	addi t0, t0, 1
	
ciclo:

	lb t1, 0(t0)	# Carattere corrente della stringa: buffer[i]
	
	# Primo confronto con la terminazione della stringa
	
	beq t1, a2, fineStringa
	beq t1, zero, fineStringa
	
	# Elimino le occorrenze che non devo considerare
	
	li a3, 50	# Valore ASCII del carattere: '2'
	li a4, 57	# Valore ASCII del carattere: '9'
	
	ble t1, a3, avanza
	bge t1, a4, avanza
	
	# Altrimenti si tratta di un numero che ci interessa, lo elaboro
	
	addi t1, t1, -48
	
	# Verifico se il numero sia pari o dispari
	
	andi t4, t1, 1
	beq t4, zero, è_pari
	
	# Altrimenti è dispari, incremento le occorrenze
	
	addi t3, t3, 1

avanza:

	addi t0, t0, 1
	j ciclo
	
è_pari:

	addi t2, t2, 1
	j avanza

fineStringa:

	# Arrivati a fine stringa posso stampare il numero delle occorrenze
	
	mv a0, t2
	li a7, 1
	ecall
	
	li a0, 10
	li a7, 11
	ecall
	
	mv a0, t3
	li a7, 1
	ecall
	
	# Fine programma
	
	li a7, 10
	ecall
