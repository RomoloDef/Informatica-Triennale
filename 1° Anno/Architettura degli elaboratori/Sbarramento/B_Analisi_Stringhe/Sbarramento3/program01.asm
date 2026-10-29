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
	li a7, 8        # Syscall per input stringa (codice per leggere stringa)
	la a0, buffer   # Carica indirizzo base in a0
	li a1, 20       # Massimo 20 caratteri
	ecall           # Effettua la chiamata di sistema

##########################################
## INSERIRE IL CODICE QUI

	# Inizializzazioni 
	mv s0, a0       # Sposto l'indirizzo base di buffer in s0
	li t0, 10       # Codice ASCII del carattere '\n' (10)
	li t6, 48       # Codice ASCII del carattere '0' (48, oppure '0')
	
	li t1, 0        # Contatore occorrenze di '0'
	li t2, 0        # Contatore occorrenze di '1'
	li t3, 0        # Indice i per lo scorrimento del ciclo

contaOccorrenze:

	add t4, s0, t3
	lbu t5, 0(t4)   # Carattere corrente della stringa
	
	# Confronto per la terminazione della stringa ('\n' oppure '\0'):
	beq t5, t0, fineStringa
	beq t5, zero, fineStringa
	
	# Confronto con il carattere ASCII '0' (t6 = 48):
	bne t5, t6, contaUno
	
	# Se è uguale a '0':
	addi t1, t1, 1
	j aumenta
	
contaUno:
	# Se non è '0' (ed essendo una stringa binaria è '1'):
	addi t2, t2, 1
	
aumenta:
	# Aggiorno l'indice e torno all'inizio del ciclo
	addi t3, t3, 1
	j contaOccorrenze

fineStringa:
	# Stampo il primo valore (occorrenze di '0')
	mv a0, t1
	li a7, 1        # 1 = Print Int
	ecall

	# Vado a capo stampando il carattere '\n' (ASCII 10)
	li a0, 10       
	li a7, 11       # 11 = Print Char
	ecall
	
	# Stampo il secondo valore sulla nuova riga (occorrenze di '1')
	mv a0, t2
	li a7, 1        # 1 = Print Int
	ecall
	
	# Fine Programma
	li a7, 10
	ecall