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
    li a7, 8       # Code for string input
    la a0, buffer  # Load base address in a0
    li a1, 20      # Allocate at most 20 characters
    ecall          # a0 contains the base address of the string

##########################################
## INSERIRE IL PROPRIO CODICE QUI

	jal contaOccorrenze
	
	# --- STAMPE ---
	# 1. Stampo il primo valore (a1 = divisibili per 4)
	mv a0, a1
	li a7, 1
	ecall
	
	# 2. Vado a capo
	li a0, 10
	li a7, 11
	ecall
	
	# 3. Stampo il secondo valore (a2 = non divisibili per 4)
	mv a0, a2       
	li a7, 1
	ecall

	# 4. Accapo finale richiesto dalla sezione "Risultato atteso"
	li a0, 10
	li a7, 11
	ecall
	
	# Fine programma
	li a7, 10       
	ecall

contaOccorrenze:

	mv s0, a0       # Sposto l'indirizzo di base nel registro: s0
	li t0, 0        # Indice i = 0 per lo scorrimento del ciclo
	
	# Carico i valori ASCII che mi servono
	li t1, 10       # Valore ASCII: \n (vale anche 10 per la moltiplicazione!)
	li x13, 57      # CORRETTO: Valore ASCII del carattere '9' (57, non 9!)
	li x14, 48      # Valore ASCII di '0' per la conversione: 48
	li x15, 4       # Divisore 4 (caricato fuori dal ciclo)
	
	# Carico i registri per i risultati del programma
	li a1, 0        # Numero di occorrenze divisibili per 4
	li a2, 0        # Numero di occorrenze non divisibili per 4
	
ciclo:
	add t2, s0, t0  # Calcolo l'indirizzo di buffer[i]
	lbu t3, 0(t2)   # Primo carattere della coppia: buffer[i]
	
	# 1. Faccio SUBITO i controlli di fine stringa sul primo carattere
	beq t3, t1, fineStringa
	beq t3, zero, fineStringa
	
	# 2. Carico il secondo carattere della coppia: buffer[i+1]
	lbu t5, 1(t2)   
	
	# 3. Verifico che il primo carattere non sia '9' (se lo è, scarto la coppia)
	beq t3, x13, aumentaPrima
	
	# Converto il primo carattere in un intero
	sub t4, t3, x14
	
	# 4. Verifico se il secondo carattere è la fine della stringa (cifra spaiata)
	beq t5, t1, cifraSingola
	beq t5, zero, cifraSingola
	
	# 5. Verifico che il secondo carattere non sia '9' (se lo è, scarto la coppia)
	beq t5, x13, aumentaPrima
	
	# Posso ora considerare la coppia completa
	sub t5, t5, x14     
	mul t4, t4, t1      
	add t6, t4, t5      # t6 = decine * 10 + unità
	j elaboraNumero
	
cifraSingola:
	mv t6, t4           # Vale come solo unità
	
elaboraNumero:	
	# Verifico che il numero in t6 sia divisibile per 4
	rem x16, t6, x15
	beq x16, zero, divisibile4
	
	# Altrimenti incremento il conteggio dei non divisibili
	addi a2, a2, 1
	j aumentaPrima
	
divisibile4:
	addi a1, a1, 1

aumentaPrima:
	# Se il secondo carattere t5 era già '\n' o '\0', la stringa è finita!
	beq t5, t1, fineStringa
	beq t5, zero, fineStringa
	
	# Altrimenti passo alla coppia successiva (i = i + 2)
	addi t0, t0, 2	
	j ciclo
	
fineStringa:
	ret