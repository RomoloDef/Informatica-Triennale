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

	mv t0, a0
	
	li t2, 0	# Accumulatore
	
	li t4, 10	# Valore ASCII: '\n'
	
ciclo:

	lb t1, 0(t0)	# Carattere corrente della stringa buffer[i]
	
	# Primo confronto sulla terminazione della stringa
	
	beq t1, t4, fineStringa
	beq t1, zero, fineStringa
	
	# Confronto con il carattere '/'
	
	li a3, 47
	beq t1, a3, separatore
	
	# Elaborazione della cifra esadecimale
	
	li t5, 57           # ASCII di '9' (valore 57)
    bgt t1, t5, lettera # Se t1 > 57 ('9'), allora è una lettera (A-F)
    
numero:

    addi t1, t1, -48    # È una cifra 0-9 (es: '0' 48-48 = 0)
    j fine_conversione
    
lettera:

   	addi t1, t1, -55    # È una lettera A-F (es: 'A' 65-55 = 10)
   	 
fine_conversione:
	
	slli t2, t2, 4      # Moltiplica per 16 facendo spazio a destra
	
	add t2, t2, t1      # Aggiunge il valore numerico
	
	# Incremento il contatore
	addi t0, t0, 1
	j ciclo
	
separatore:
    	# Stampa il numero accumulato (che è GIÀ in decimale!)
    	mv a0, t2
    	li a7, 1
    	ecall
    	
    	# Vai a capo
    	li a0, 10
    	li a7, 11
    	ecall
    	
    	# Resetta l'accumulatore per il prossimo gruppo
    	li t2, 0
    	addi t0, t0, 1      # salta il '/'
    	j ciclo
    
fineStringa:
    	
    	li a7, 10
    	ecall
