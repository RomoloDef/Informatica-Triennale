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
.globl main

main:
    	li a7, 8       # Codice per input stringa
    	la a0, buffer  # Carica indirizzo base in a0
    	li a1, 26      # Alloca al massimo 24 caratteri + 
    	ecall          # a0 contiene l'indirizzo base della stringa
# ... A QUI

##########################################
# INSERIRE IL PROPRIO CODICE QUI

	mv t0, a0	# Sposto l'indirizzo di base in t0
	
	li t2, 0	# Accumulatore per il numero binario corrente
	li t3, 0	# Totale complessivo
	li t4, 1	# Segno pendente: 1 per '+', -1 per '-' (il primo numero è +)
	
	li a2, 10	# ASCII '\n'
	li a3, 43	# ASCII '+'
	li a4, 45	# ASCII '-'
	
ciclo:
	lb t1, 0(t0)
	
	# Fine stringa: dobbiamo ancora applicare l'ultimo numero accumulato!
	beq t1, a2, applicaUltimo
	beq t1, zero, applicaUltimo
	
	# Se incontriamo '+' o '-' applichiamo il numero accumulato finora
	beq t1, a3, gestisciPiu
	beq t1, a4, gestisciMeno
	
	# È un bit ('0' o '1'): shift a sinistra e somma
	addi t1, t1, -48
	slli t2, t2, 1
	add t2, t2, t1
	
	addi t0, t0, 1
	j ciclo

gestisciPiu:
	# Applica il numero precedente secondo il segno in t4
	li a5, 1
	beq t4, a5, applicaSommaPiu
	sub t3, t3, t2
	j avantiPiu

applicaSommaPiu:
	add t3, t3, t2

avantiPiu:
	li t2, 0        # Azzero l'accumulatore per il prossimo numero
	li t4, 1        # Il prossimo numero andrà SOMMATO (+)
	addi t0, t0, 1
	j ciclo

gestisciMeno:
	# Applica il numero precedente secondo il segno in t4
	li a5, 1
	beq t4, a5, applicaSommaMeno
	sub t3, t3, t2
	j avantiMeno

applicaSommaMeno:
	add t3, t3, t2

avantiMeno:
	li t2, 0        # Azzero l'accumulatore per il prossimo numero
	li t4, -1       # Il prossimo numero andrà SOTTRATTO (-)
	addi t0, t0, 1
	j ciclo

applicaUltimo:
	# Applica l'ultimo numero rimasto in t2
	li a5, 1
	beq t4, a5, ultimoSomma
	sub t3, t3, t2
	j fineStringa

ultimoSomma:
	add t3, t3, t2

fineStringa:
	mv a0, t3
	li a7, 1
	ecall
	
	li a7, 10
	ecall
