##########################################
# INSERIRE I PROPRI DATI QUI
# Nome: Romolo
# Cognome: Deffereria
# Matricola: 2114887
##########################################

# NON MODIFICARE IL CODICE DA QUI...
.data
    bufferIn:  .space 26
    bufferOut: .space 50

.text

main:
    li a7, 8       # Codice per input stringa
    la a0, bufferIn  # Carica indirizzo base in $a0
    li a1, 26      # Alloca al massimo 24 caratteri + \n + \0
    la a2, bufferOut # Carica indirizzo base in $a1
    li a3, 50		# dimensione bufferOut
    ecall          # $a0 contiene l'indirizzo base della stringa
# ... A QUI

##########################################
## INSERIRE IL PROPRIO CODICE QUI

	mv t0, a0           # Indirizzo base della stringa ("120A4")
	li t2, 0            # t2 = numero originale (N)
	li t3, 0            # t3 = MASCHERA dei bit selezionati (M)
	
	li s0, 1            # Costante 1 (ci serve per fare 1 << V)
	li a2, 10           # ASCII '\n'
	li a3, 57           # ASCII '9'

ciclo:
	lb t1, 0(t0)        # Carattere corrente
	
	beq t1, a2, fineStringa
	beq t1, zero, fineStringa
	
	bgt t1, a3, lettera
	
numero:
	addi t4, t1, -48    # t4 = valore numerico V (0-9)
	j elabora
	
lettera:
	addi t4, t1, -55    # t4 = valore numerico V (10-15 per A-F)

elabora:
	# 1. Costruisco il numero originale N
	slli t2, t2, 4      # Moltiplica per 16
	add t2, t2, t4      # N = (N * 16) + V
	
	# 2. Aggiorno la maschera M (nello stesso ciclo!)
	sll s1, s0, t4      # s1 = 1 << V (mette un 1 nella posizione V)
	or t3, t3, s1       # Maschera = Maschera OR (1 << V)
	
	addi t0, t0, 1
	j ciclo

fineStringa:
	# 1. Stampa il numero originale in esadecimale (Riga 1)
	mv a0, t2
	li a7, 34
	ecall
	
	# A capo
	li a0, 10
	li a7, 11
	ecall
	
	# 2. Seleziona i bit tramite AND tra il numero e la maschera (Riga 2)
	and a0, t2, t3      # a0 = N & Maschera
	li a7, 34           # Syscall 34 stampa 0x00000004
	ecall
	
	# A capo finale
	li a0, 10
	li a7, 11
	ecall

	# Fine programma
	li a7, 10
	ecall


