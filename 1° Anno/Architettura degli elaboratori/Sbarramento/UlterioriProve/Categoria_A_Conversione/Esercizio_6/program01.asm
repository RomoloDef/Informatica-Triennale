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

	mv t0, a0	# Sposto l'indirizzo di base nel registro: t0
	
	li t2, 0	# Accumulatore
	li t3, 0	# Contatore di bit
	li t4, 3	# Costante per il confronto sui terzetti di bit
	li t5, 0	# Flag di stampa
	li t6, 0	# Flag per i bit ignorati
	
	li a2, 0	# Numero di cifre ottali prodotte
	
	li a3, 10	# Valore ASCII per il carattere: '/n'
	
ciclo:

	lb t1, 0(t0)	# Carattere corrente della stringa: buffer[i]
	
	# Primo confronto con la terminazione della stringa
	
	beq t1, a3, fineStringa
	beq t1, zero, fineStringa
	
	# Elaboro il bit
	
	addi t1, t1, -48
	slli t2, t2, 1
	add t2, t2, t1
	
	# Incremento il contatore di bit
	
	addi t3, t3, 1
	
	# Verifico se si sia formato un terzetto
	
	bne t3, t4, avanza
	
	# Terzetto formato, stampo la cifra ottale e incremento il numero di cifre prodotte
	
	mv a0, t2
	li a7, 1
	ecall
	
	addi a2, a2, 1
	
	# Resetto i registri
	li t2, 0
	li t3, 0
	li t5, 1	# Flag di stampa = 1: Ha stampato!
	
avanza:

	addi t0, t0, 1
	j ciclo
	
fineStringa:

	# 1. Controllo se ci sono bit spaiati ignorati in coda
	# Se il contatore t3 non è zero, significa che abbiamo lasciato dei bit in sospeso!
	beq t3, zero, stampa_tutto
	
	# Ci sono bit spaiati: setto il flag t6 a 1
	li t6, 1
	
stampa_tutto:
	
	# Vado a capo (stacca l'output ottale da quello che segue)
	li a0, 10
	li a7, 11
	ecall
	
	# 2. Stampo t6 (il flag dei bit spaiati: 0 oppure 1)
	mv a0, t6
	li a7, 1
	ecall
	
	# Vado a capo
	li a0, 10
	li a7, 11
	ecall
	
	# 3. Stampo a2 (Il numero totale di cifre ottali prodotte)
	mv a0, a2
	li a7, 1
	ecall
	
	# Vado a capo per l'ultima volta
	li a0, 10
	li a7, 11
	ecall
	
esci:
	# Fine programma
	li a7, 10
	ecall

	
	

	
	
	


	
