##########################################
# INSERIRE I PROPRI DATI QUI
# Nome: Romolo
# Cognome: Deffereria
# Matricola: 2114887
##########################################

# NON MODIFICARE IL CODICE DA QUI...
.data
    buffer: .space 26
    output: .byte  0,0,0,0,0,0,0,0,0  # Un carattere extra per la fine della stringa

.text

main:
    	li a7, 8       # Codice per input stringa
    	la a0, buffer  # Carica indirizzo base in $a0
    	li a1, 26      # Alloca al massimo 24 caratteri + \n + \0
    	ecall          # $a0 contiene l'indirizzo base della stringa
    	la a2, output
# ... A QUI

##########################################
## INSERIRE IL PROPRIO CODICE QUI

	jal codificaOttale
	
	# 1. Stampo la stringa ottale prodotta in output
	#    (codificaOttale l'ha scritta in memoria a partire da a2)
	mv a0, a2           # a0 = indirizzo della stringa output
	li a7, 4            # syscall 4 = stampa stringa
	ecall
	
	# 2. Vado a capo
	li a0, 10
	li a7, 11
	ecall
	
	# 3. Stampo a3 (0 se nessun bit scartato, 1 se ci sono bit scartati)
	mv a0, a3
	li a7, 1
	ecall
	
	# 4. Vado a capo
	li a0, 10
	li a7, 11
	ecall
	
	# 5. Stampo a4 (numero di cifre ottali prodotte)
	mv a0, a4
	li a7, 1
	ecall
	
	# 6. Accapo finale
	li a0, 10
	li a7, 11
	ecall
	
	# Fine programma
	li a7, 10
	ecall

codificaOttale:

	mv t0, a0           # t0 = puntatore al carattere corrente di buffer
	mv t5, a2           # t5 = puntatore alla posizione corrente in output
	
	li t2, 0            # Accumulatore terzina 
	li t3, 0            # Contatore dei bit nella terzina corrente 
	li t4, 3            # Costante per il confronto: 3 bit
	
	li a3, 0            # Flag bit scartati (0 = no, 1 = sì) — valore di ritorno
	li a4, 0            # Contatore cifre ottali prodotte — valore di ritorno
	
	li t6, 10           # Valore ASCII: '\n'

ciclo:
	lb t1, 0(t0)        # Carico il carattere corrente della stringa buffer

	# Confronti sulla terminazione della stringa
	beq t1, t6, fineStringa  
	beq t1, x0, fineStringa  
	
	# Converto il valore ASCII in valore numerico (0 o 1)
	addi t1, t1, -48    
	
	slli t2, t2, 1 

	add t2, t2, t1      
	
	# Incremento il contatore dei bit
	addi t3, t3, 1
	
	# Confronto: la terzina è completa? 
	bne t3, t4, avanza 
	
	# === Terzina completa! ===
	addi t2, t2, 48     			# La converto in valore ASCII
	
	# Scrivo il carattere in output
	sb t2, 0(t5)        # output[pos] = cifra ottale come carattere
	addi t5, t5, 1      # Avanzo il puntatore di output
	
	# Aggiorno il contatore delle cifre prodotte
	addi a4, a4, 1
	
	# Resetto accumulatore e contatore per la prossima terzina
	li t2, 0
	li t3, 0

avanza:
	addi t0, t0, 1      # Avanzo al prossimo carattere di buffer
	j ciclo

fineStringa:
	# Chiudo la stringa output con '\0' (terminatore)
	sb x0, 0(t5)        # output[pos] = '\0'
	
	# Controllo se ci sono bit residui scartati
	# Se t3 != 0, allora c'erano 1 o 2 bit che non formavano una terzina
	beq t3, x0, nessuno_scarto
	li a3, 1            # Flag = 1 → ci sono bit scartati
	
nessuno_scarto:
	ret                 # Ritorna al main (a3 e a4 contengono i risultati)
