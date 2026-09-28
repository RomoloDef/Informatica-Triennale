# Dati due vettori di interi A e B della stessa dimensione, copia tutti gli elementi di A dentro B, ma in ordine inverso.

.globl main

.data 

vettore1: .word 1, 2, 3, 4, 5
vettore2: .space 20
lunghezza: .word 5               # N = 5

.text
main:
    	la t0, vettore1      # Indirizzo base di A
    	la t1, vettore2      # Indirizzo base di B
    	lw t2, lunghezza     # t2 = 5 (N)
    
    	# Prepariamo gli indici
    	# Per A partiamo dall'ultimo elemento: (N-1) * 4
    	addi t3, t2, -1      # t3 = 4 (Indice i per A)
    	li   t4, 0           # t4 = 0 (Indice j per B)

ciclo_copia:
    	# Condizione di uscita: abbiamo copiato N elementi?
    	# Se l'indice di B (t4) arriva a 5, abbiamo finito
    	bge  t4, t2, fine
    
    	# --- GESTIONE VETTORE A (Lettura dall'ultimo) ---
    	slli t5, t3, 2       # Offset di A = i * 4
    	add  t5, t0, t5      # Indirizzo corrente in A
    	lw   t6, 0(t5)       # Carichiamo l'elemento da A
    
    	# --- GESTIONE VETTORE B (Scrittura dal primo) ---
    	slli a7, t4, 2       # Offset di B = j * 4
    	add  a7, t1, a7      # Indirizzo corrente in B
    	sw   t6, 0(a7)       # Salviamo l'elemento in B
    
   	 # --- AGGIORNAMENTO INDICI ---
    	addi t3, t3, -1      # i va all'indietro (4, 3, 2, 1, 0)
    	addi t4, t4, 1       # j va in avanti (0, 1, 2, 3, 4)
    
    	j ciclo_copia

fine:
    	# Il vettore B ora contiene [5, 4, 3, 2, 1]
    	li a7, 10
    	ecall



	