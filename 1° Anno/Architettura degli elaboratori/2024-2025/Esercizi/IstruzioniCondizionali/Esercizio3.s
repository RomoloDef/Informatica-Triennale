# Dato un array di interi definiti nella sezione .data, scrivi un programma che trovi il valore massimo all'interno dell'array.

.globl main

.data 
array: .word 5, 12, 3, 25, 8, 1
lunghezza: .word 6             		# È meglio definirla qui o usare il valore esatto

.text
main:
	# Caricamento dei registri
	li   t0, 0                		# t0 = Iteratore (i = 0)
	li   t1, 6               		# t1 = Lunghezza (N = 6)
    	la   t3, array            		# t3 = Indirizzo base dell'array

    
    	# Inizializziamo il massimo con il primo elemento o uno molto piccolo
    	lw   t2, 0(t3)           		 # t2 = Massimo (partiamo dal primo elemento: 5)

cicloFor:
    	bge  t0, t1, endfor       		# Se i >= 6, vai alla fine
    
    	# 1. Calcolo l'offset: ogni .word occupa 4 byte
    	# Spostamento = i * 4. In Assembly si può fare con uno shift a sinistra di 2 (slli)
    	slli t4, t0, 2           		# t4 = i * 4
    	add  t5, t3, t4            		# t5 = Indirizzo base + Offset
    
    	# 2. Carica l'elemento corrente
    	lw   t6, 0(t5)            		# t6 = array[i]
    
    	# 3. Confronta con il massimo attuale
    	ble  t6, t2, skip_max     		# Se array[i] <= massimo, salta l'aggiornamento
    	mv   t2, t6               		# Altrimenti, massimo = array[i]

skip_max:
    	addi t0, t0, 1            		# Incrementa l'iteratore
    	j    cicloFor             		# Torna all'inizio del ciclo

endfor:
    	# Qui il valore massimo è in t2. 
    	# Stampa:
    	li a7, 1                  		# Syscall per print_int
    	mv a0, t2                 		# Carica il massimo in a0
    	ecall
    
    	li a7, 10                 # Exit
    	ecall
	
	
