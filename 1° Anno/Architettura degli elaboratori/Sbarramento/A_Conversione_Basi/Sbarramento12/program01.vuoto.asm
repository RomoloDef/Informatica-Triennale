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
    	la a0, buffer  # Carica indirizzo base in $a0
    	li a1, 26      # Alloca al massimo 24 caratteri + \n + \0
    	ecall          # $a0 contiene l'indirizzo base della stringa
# ... A QUI

##########################################

	mv t0, a0	# Sposto l'indirizzo di base nel registro: t0
	
	li t2, 0	# Accumulatore
	
	li a2, 10	# Valore ASCII del carattere: '/n'
	
ciclo:

	lb t1, 0(t0)	# Carattere corrente della stringa: buffer[i]
	
	# Primo confronto con la terminazione della stringa
	
	beq t1, a2, fineStringa
	beq t1, zero, fineStringa
	
	# Secondo confronto con il separatore
	
	li a3, 47	# Valore ASCII del carattere: '/'
	
	beq t1, a3, separatore
	
	# Elaboro il bit - ma devo fare la differenza tra lettere e numeri
	
	li a4, 65	# Valore ASCII del carattere 'A'
	
	bge t1, a4, è_lettera
	
	# Altrimenti è un numero
	
	addi t1, t1, -48
	
accumula:

	slli t2, t2, 4
	
	add t2, t2, t1
	
	# Incremento l'indice posizionale della stringa
	
	addi t0, t0, 1
	j ciclo
	
è_lettera:

	addi t1, t1, -55
	j accumula
	
separatore:
	
	# Quando si arriva al separatore bisogna stampare tutto l'accumulatore presente prima
	
	mv a0, t2
	li a7, 1
	ecall
	
	# Vado a capo
	
	li a0, 10
	li a7, 11
	ecall
	
	# Resetto l'accumulatore
	
	li t2, 0
	
	# Vado avanti con la stringa
	
	addi t0, t0, 1
	j ciclo
	
fineStringa:

	li a7, 10
	ecall

	
	
	
	
	
