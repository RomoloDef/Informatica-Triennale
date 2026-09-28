# Creare un programma che faccia sostituire un valore specifico all'interno della matrice in base alle scelte dell'utente.

.globl main

.data 

messaggio_riga: .asciz "Inserisci il numero della riga: "
messaggio_colonna: .asciz "Inserisci il numero della colonna: "
valore: .asciz "Inserisci il valore che desideri sostituire: "

matrice: .word 0 0 0 0
	 .word 0 0 0 0 
	 .word 0 0 0 0 
	 .word 0 0 0 0 
	 
N: .word 4

.text

main:
	# --- LETTURA VALORE ---
	la a0, valore
	li a7, 4
	ecall
	
	li a7, 5
	ecall
	mv t0, a0

	# --- LETTURA RIGA ---
    	la a0, messaggio_riga
    	li a7, 4
    	ecall
    
    	li a7, 5
    	ecall
    	mv t1, a0           # t0 = INDICE RIGA
    
    	# --- LETTURA COLONNA ---
    	la a0, messaggio_colonna
    	li a7, 4
    	ecall               
    
    	li a7, 5 
    	ecall
    	mv t2, a0           # t1 = INDICE COLONNA
    	
    	# --- LETTURA MATRICE ---
    	la a0, matrice    # Indirizzo base della matrice in a0
    	lw t3, N          # Numero totale di colonne (N = 4)
    	# Formula per calcolare l'offset: (Riga * N + Colonna) * 4
    	mul t4, t1, t3
    	add t4, t4, t2
    	slli t4, t4, 2	# Offset in byte (moltiplico per 4)
    	
 	add t5, a0, t4	# a2 = Indirizzo esatto della cella (Base + Offset)
 	
 	# --- SALVATAGGIO DEL VALORE ---
    	# Prendiamo il valore salvato in t0 e lo mettiamo nella memoria all'indirizzo a2
    	sw t0, 0(t5)
    	
    	# --- FINE PROGRAMMA ---
    	li a7, 10
    	ecall
    	
    	
    	

