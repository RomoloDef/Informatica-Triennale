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
	li t4, 3	# Costante per il confronto sulla terzina
	
	li t6, 10	# Valore ASCII del carattere: '/'
	
ciclo:

	lb t1, 0(t0)	# Carattere corrente della stringa: buffer[i]
	
	# Primo confronto sulla terminazione della stringa
	
	beq t1, t6, fineStringa
	beq t1, zero, fineStringa
	
	# Elaboro il bit
	
	addi t1, t1, -48 
	
	slli t2, t2, 1
	
	add t2, t2, t1
	
	# Incremento il contatore dei bit
	
	addi t3, t3, 1
	
	# Verifico se si sia formata una tripla
	
	bne t3, t4, avanza
	
	# Tripla formata: si stampa!
	
	mv a0, t2
	li a7, 1
	ecall	
	
	# Resetto i registri
	li t2, 0
	li t3, 0	
	
avanza:

	addi t0, t0, 1
	j ciclo
		
fineStringa:	

	beq t3, zero, esci
	
padding:
	
	beq t3, t4, stampa_ultimo
	# Se si arriva qui allora significa che bisogna paddare
	slli t2, t2, 1
	addi t3, t3, 1
	j padding
	
stampa_ultimo:
	
	# Ora lo posso stampare come ultimo
	mv a0, t2
	li a7, 1
	ecall
	
esci:

	li a7, 10
	ecall
	
