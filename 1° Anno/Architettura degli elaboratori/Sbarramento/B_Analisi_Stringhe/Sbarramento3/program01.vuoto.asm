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
    	li a7, 8       # Codice per input stringa
    	la a0, buffer  # Carica indirizzo base in $a0
    	li a1, 20      # Alloca al massimo 20 caratteri
    	ecall         # $a0 contiene l'indirizzo base della stringa
	

##########################################

	mv t0, a0	# Sposto l'indirizzo di base nel registro: t0
	
	li t2, 0	# Occorrenze di 0
	li t3, 0	# Occorrenze di 1
	
	li a2, 10	# Valore ASCII del carattere: '/n'
	li a3, 48	# Valore ASCII del carattere: '0'

ciclo:

	lb t1, 0(t0)	# Carattere corrente della stringa: buffer[i]
	
	# Primo confronto con la terminazione della stringa:
	
	beq t1, a2, fineStringa
	beq t1, zero, fineStringa
	
	# Faccio il confronto con il valore ASCII '0'
	
	beq t1, a3, è_zero
	
	# Altrimenti, visto che la stringa è formata solo da 0 e 1, è un uno
	
	addi t3, t3, 1
	
	# Incremento l'indice posizionale della stringa
	
	addi t0, t0, 1
	j ciclo
	
è_zero:

	# Sommo le occorrenze di 0
	
	addi t2, t2, 1
	
	# Incremento
	
	addi t0, t0, 1
	j ciclo

fineStringa:

	# Stampo
	
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