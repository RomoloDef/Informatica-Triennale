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
	
	mv t0, a0	# Sposto l'indirizzo base della stringa nel registro: t0
	
	li t2, 0	# Accumulatore
	li t3, 0	# Contatore del carattere '1'
	li t4, 2	# Costante con cui fare il confronto per il contatore di caratteri
	li t5, 0	# Sommatoria finale
	
	li t6, 10	# Valore ASCII del carattere: '/n'
	
ciclo:

	lb t1, 0(t0)	# Carattere corrente della stringa: buffer[i]
	
	# Faccio il primo confronto con la terminazione della stringa
	
	beq t1, t6, fineStringa
	beq t1, zero, fineStringa
	
	# Carico il carattere speciale
	
	li a2, 47	# Valore ASCII del carattere: '/'
	
	beq t1, a2, separatore
	
	# Elaboro il bit
	
	addi t1, t1, -48
	
	slli t2, t2, 1
	
	add t2, t2, t1
	
	# Per ogni carattere verifico se sia uno zero o un'uno
	
	li a3, 1 
	
	beq t1, a3, conta_uno
	
	# Se non lo è semplicemente aumento l'indice di scorrimento e vado avanti
	
	addi t0, t0, 1
	
	j ciclo
	
	
conta_uno:

	# Se il carattere è uno aumento il conteggio 
	
	addi t3, t3, 1
	
	# Incremento l'indice e poi vado avanti
	
	addi t0, t0, 1
	j ciclo
	
separatore:

	# Se si ha letto il carattere '/' bisogna verificare che il numero di 1 sia 2 e nel caso aggiungere alla somma
	
	bne t3, t4, reset
	
	# Altrimenti si aggiunge alla somma l'accumulatore
	
	add t5, t5, t2
	
	# Dopo aver fatto ciò si può resettare il tutto e tornare al ciclo
	
reset:
	
	li t2, 0
	li t3, 0
	addi t0, t0, 1
	j ciclo	
	
fineStringa:

	# Verifico anche l'ultimissimo numero!
	bne t3, t4, stampa_finale
	add t5, t5, t2     # Se aveva due '1', lo sommo!
	
stampa_finale:

	# si stampa il valore della sommatoria finale
	
	mv a0, t5
	li a7, 1
	ecall
	
	# Termine programma
	li a7, 10
	ecall
	
