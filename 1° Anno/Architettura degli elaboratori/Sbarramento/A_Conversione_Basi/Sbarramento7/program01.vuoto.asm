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
## INSERIRE IL PROPRIO CODICE QUI


	mv t0, a0	# Sposto l'indirizzo nel registro: t0
	
	li t2, 0	# Accumulatore
	li t3, 0	# Contatore di bit
	li t4, 0	# Numero di cifre prodotte
	li t6, 0	# Flag per la divisibilità della stringa
	
	li a2, 10	# Valore ASCII per il carattere: '/n'
	li a3, 3	# Costante per la verifica di formazione di terzine
	
ciclo:

	lb t1, 0(t0)	# Carattere corrente della stringa: buffer[i]
	
	# Primo confronto con la terminazione della stringa
	
	beq t1, a2, fineStringa
	beq t1, zero, fineStringa
	
	# Elaboro il bit
	
	addi t1, t1, -48
	
	slli t2, t2, 1
	
	add t2, t2, t1
	
	# Aumento il conteggio dei bit
	
	addi t3, t3, 1
	
	# Verifico che si sia formata una terzina

	bne t3, a3, avanza
	
	# Altrimenti la terzina si è formata:
	# 1) Aumento il numero di cifre prodotte
	# 2) La stampo
	# 3) Resetto i registri
	
	addi t4, t4, 1
	
	mv a0, t2
	li a7, 1
	ecall
	
	# Resetto
	
	li t2, 0
	li t3, 0
	
avanza:

	addi t0, t0, 1
	j ciclo
	
fineStringa:

	# Verifico se la stringa è formata da un numero di caratteri multiplo di 3, se non lo fosse faccio padding a destra
	
	beq t3, zero, esci
	
	# Altrimenti setto a 1 il flag e faccio padding
	
	li t6, 1
	
	# Padding:
	
	li a5, 1
	beq t3, a5, pad_due_zeri    # Se hai 1 bit -> mancano 2 zeri
	
	li a6, 2
	beq t3, a6, pad_un_zero     # Se hai 2 bit -> manca 1 zero
	j esci              	    # Se t3 == 0, gruppo vuoto: non fare nulla
	
pad_due_zeri:

	slli t2, t2, 2              # Shift di 2 posizioni a sinistra (due zeri a destra)
	j stampa_residua
	
pad_un_zero:

	slli t2, t2, 1              # Shift di 1 posizione a sinistra (uno zero a destra)
	
stampa_residua:
	
	mv a0, t2
	li a7, 1
	ecall
	
	# Incremento il conteggio però anche
	
	addi t4, t4, 1
	
esci:

	li a0, 10
	li a7, 11
	ecall
	
	mv a0, t6
	li a7, 1
	ecall
	
	li a0, 10
	li a7, 11
	ecall
	
	mv a0, t4
	li a7, 1
	ecall
	
	li a0, 10
	li a7, 11
	ecall
	
	# Fine programma
	
	li a7, 10
	ecall
	
	