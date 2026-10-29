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

	mv t0, a0	# Sposto l'indirizzo base nel registro: t0
	
	li t2, 0	# Accumulatore
	li t3, 0	# Contatore dei bit
	li t4, 4	# Costante per fare il confronto con il quartetto di caratteri
	li t5, 0	# Flag per indicare se c'è stata una stampa
	
	li t6, 10	# Valore ASCII per il carattere: '/n'
	
ciclo:
	
	lb t1, 0(t0)	# Carattere corrente della stringa: buffer[i]
	
	# Primo confronto con la terminazione della stringa
	
	beq t1, t6, fineStringa
	beq t1, zero, fineStringa
	
	# Carico il carattere speciale e faccio il Secondo confronto
	
	li a3, 47
	
	beq t1, a3, separatore
	
	# Elaboro il bit - Mi serve un primo piccolo accumulatore temporaneo (la syscall 34 può essere chiamata una volta per gruppo) 
	
	addi t1, t1, -48
	
	slli t2, t2, 1
	
	add t2, t2, t1
	
	# Incremento il contatore dei bit
	
	addi t3, t3, 1
	
	# Verifico se si sia formata una quartina di bit
	
	bne t3, t4, avanza
	
	# Quartina formata quindi la sposto nell'accumulatore piu grande
	
	slli s0, s0, 4		# Una cifra esadecimale
	add s0, s0, t2
	
	# Resetto i registri
	li t2, 0
	li t3, 0
	li t5, 1	# Flag = 1: Ha stampato!

avanza:

	addi t0, t0, 1
	j ciclo

separatore:

	# I bit che non formano una quartina vanno scartati o ignorati
	# Lo si fa resettando i registri e incrementando l'indice
	beq t5, zero, skippa
	
	# Stampo il numero una sola volta
	mv a0, s0
	li a7, 34
	ecall
	
	# Altimenti semplicemente mando a capo
	
	li a0, 10
	li a7, 11
	ecall
	
skippa:

	li s0, 0

	li t2, 0
	li t3, 0
	li t5, 0
	addi t0, t0, 1
	j ciclo

fineStringa:

	beq t5, zero, esci
	
	mv a0, s0
	li a7, 34
	ecall
	
	li a0, 10
	li a7, 11
	ecall
	
esci:
	
	# Fine Programma
	li a7, 10
	ecall
	
