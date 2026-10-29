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
## INSERIRE IL PROPRIO CODICE QUI

	jal contaOccorrenze

	# 1. Stampo il primo valore (a1)
	mv a0, a1
	li a7, 1
	ecall
	
	# 2. Vado a capo
	li a0, 10
	li a7, 11
	ecall
	
	# 3. Stampo il secondo valore (a2)
	mv a0, a2       
	li a7, 1
	ecall
	
	# Fine programma
	li a7, 10       
	ecall

contaOccorrenze:

	mv s0, a0	# Sposto il l'indirizzo di base nel registro
	
	li t0, 1	# Visto che devo far partire il ciclo dal secondo carattere, parto con l'indice aumentato di 1
	
	# Carico i valori ASCII che mi servono
	
	li t1, 10	# Valore ASCII del carattere: \n
	
	li t2, 48	# Valore ASCII per la conversione del numero	
	
	# Carico in due registri ciò che serve per l'esercizio
	
	li a1, 0	# Occorrenze pari
	
	li a2, 0	# Occorrenze dispari
	
	# Controllo di sicurezza se la stringa è vuota (buffer[0] == '\n' o '\0')
    	lbu t4, 0(s0)
   	beq t4, t1, fineStringa
   	beq t4, zero, fineStringa
	
ciclo:

	# Calcolo l'indirizzo di buffer[i]
	
	add t3, s0, t0
	
	# Carattere corrente
	
	lbu t4, 0(t3)
	
	# Inizio con i salti per la terminazione della stringa
	
	beq t4, t1, fineStringa
	beq t4, zero, fineStringa
	
	# Converto il carattere in numero intero
	
	sub t5, t4, t2		# t5 = cifra numerica (0..9)
	
	# Se questa cifra rispetta determinate condizioni allora posso fare il conteggio
	
	# Carico i limiti superiori e inferiori per il confronto
	
	li x13, 3
	li x14, 9
	
	# Se il numero è '0', '1', '2' o '9' allora si incrementa l'indice del ciclo
	blt t5, x13, aumenta
	beq t5, x14, aumenta
	
	# Ora posso contare le occorrenze:
	# Se il numero è pari o dispari
	
	andi t6, t5, 1
	beq t6, zero, occorrenzePari
	
	# Altrimenti incrementiamo l'occorrenze dispari:
	
	addi a2, a2, 1
	
	# e dopo averlo fatto incrementiamo l'indice
	j aumenta
	
	
occorrenzePari:
	addi a1, a1, 1
	
aumenta:
	addi t0, t0, 1
	j ciclo
	
fineStringa:
	ret
	
	
