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

	mv t0, a0	# Sposto l'indirizzo base nel registro: t0
	
	li t2, 0	# l'accumulatore della terzina
	li t3, 0	# contatore dei bit = 0
	li t4, 3	# costante 3 --> utile per il confronto se la terzina è completa
	li t5, 0	# flag = 0
	
	li t6, 10	# Valore ASCII: '\n'
	
ciclo:

	lb t1, 0(t0)	# Carattere corrente della stringa
	
	# Primo confronto sulla terminazione della stringa
	beq t1, t6, fineStringa
	beq t1, zero, fineStringa
	
	# Confronto sul separatore '/'
	li a3, 47
	beq t1, a3, separatore
	
	# Elaborazione dei bit 
	addi t1, t1, -48		# Converto il valore ASCII in carattere numerico
	
	slli t2, t2, 1			# accumulatore <<= 1 (equivale a moltiplicare per 2)
	
	add t2, t2, t1			# accumulatore += bit
	
                         		# Esempio con bit 1,1,1:
                         		#   Inizio: t2=0
                         		#   Bit 1: t2 = (0<<1) + 1 = 1      (binario: 1)
                         		#   Bit 1: t2 = (1<<1) + 1 = 3      (binario: 11)
                         		#   Bit 1: t2 = (3<<1) + 1 = 7      (binario: 111)
                         		
        # E ora conto i bit
        addi t3, t3, 1			# Incremento il conteggio dei bit
        
       	# Verifico se la terzina sia completa o no
       	bne t3, t4, avanza
       	
       	# La terzina è completa: si stampa la cifra
       	mv a0, t2
       	li a7, 1
       	ecall
       	
       	# Resetto i registri
       	li t2, 0
       	li t3, 0
       	li t5, 1		# flag = 1 (abbiamo stampato qualcosa)
       	
avanza:

	addi t0, t0, 1
	j ciclo
	
separatore:

	beq t5, x0, skip_newline  # se ha_cifre == 0, niente da chiudere
    
    	# Stampa '\n' per andare a capo dopo le cifre ottali
    	li a0, 10           # a0 = '\n' (ASCII 10)
    	li a7, 11           # syscall 11 = stampa singolo carattere
    	ecall               # stampa newline
    	
skip_newline:

    	li t2, 0            # reset accumulatore
    	li t3, 0            # reset contatore bit
    	li t5, 0            # reset flag ha_cifre
    	addi t0, t0, 1      
    	j ciclo              # continua con il prossimo gruppo
	
fineStringa:

	# Fine dell'input
    	# Se l'ultimo gruppo aveva cifre stampate, serve un '\n' finale
    	beq t5, x0, exit    # se non abbiamo stampato nulla nell'ultimo gruppo, esci
    	li a0, 10           # a0 = '\n' 
    	li a7, 11           # syscall 11 = stampa carattere
    	ecall               # stampa newline finale
    	
exit:
    li a7, 10           
    ecall               # termina il programma
    
    
    
    