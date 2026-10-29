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
    	la a0, buffer  # Carica indirizzo base in a0
    	li a1, 26      # Alloca al massimo 24 caratteri + \n + \0
    	ecall          # a0 contiene l'indirizzo base della stringa
# ... A QUI

##########################################
# INSERIRE IL PROPRIO CODICE QUI


	mv t0, a0	# Sposto l'indirizzo base nel registro: t0
	
	li t2, 0	# Accumulatore
	li t3, 0	# Contatore di bit
	li t4, 3	# Costante per la formazione di terzine
	li t5, 0	# Flag per la stampa
	
	li a2, 10	# Valore ASCII per il carattere: '/n'
	li a3, 47	# Valore ASCII per il carattere: '/'
	
ciclo:

	lb t1, 0(t0)	# Carattere corrente della stringa: buffer[i]
	
	# Primo confronto con la terminazione della stringa
	
	beq t1, a2, fineStringa
	beq t1, zero, fineStringa
	
	# Secondo confronto con il separatore
	
	beq t1, a3, separatore
	
	# Elaboro il bit
	
	addi t1, t1, -48
	
	slli t2, t2, 1
	
	add t2, t2, t1
	
	# Incremento il conteggio del contatore di bit
	
	addi t3, t3, 1
	
	# Verifico che la terzina sia formata
	
	bne t3, t4, avanza
	
	# Altrimenti la terzina è formata, posso stamparla
	
	mv a0, t2
	li a7, 1
	ecall
	
	# Resetto i registri e setto il flag
	
	li t2, 0
	li t3, 0
	li t5, 1
	
avanza:

	addi t0, t0, 1
	j ciclo

separatore:
	
	# Verifico innanzitutto se la terzina è stata formata
	bne t3, t4, a_capo
	
	beq t5, zero, skip
	
	# Vado a capo dopo le cifre ottali
	li a0, 10           
    	li a7, 11           
    	ecall
    	
skip:

        li t2, 0            # reset accumulatore
    	li t3, 0            # reset contatore bit
    	li t5, 0            # reset flag ha_cifre
    	addi t0, t0, 1      
    	j ciclo              # continua con il prossimo gruppo      
	

a_capo:

	li a0, 10           
    	li a7, 11           
    	ecall
    	
    	# Resetto i registri 
	
	li t2, 0
	li t3, 0
    	
    	j avanza
	
fineStringa:
		
	beq t5, zero, exit
	li a0, 10
	li a7, 11
	ecall
	
exit:

	# Fine programma
	li a7, 10
	ecall	
				
					
							