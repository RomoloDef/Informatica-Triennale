# Dato un vettore di dimensione N e un valore di soglia X, scorrere il vettore e per ogni elemento vector[i]:
# - Se vector[i] è minore di Soglia, sostituirlo in memoria con 0
# - Se vector[i] è maggiore o uguale a Soglia, raddoppiare il suo valore

.data

vector: .word 3, 10, -4, 7, 15, 2, 8

N: .word 7

Soglia: .word 7

.text

main:

	# Carico il valore della Soglia con cui fare il confronto
	
	lw t0, Soglia
	
	# Carico l'indirizzo base del vettore
	
	la s0, vector
	
	# Carico la lunghezza del vettore su cui ciclare
	
	lw x10, N
	
	# Carico il numero da cui iniziare a iterare 
	
	li x11, 0	# ovviamente si tratta di 0
	
cicloFor:

	bge x11, x10, endFor
	
	# Calcolo indirizzo e caricamente di vector[i]
	slli t2, x11, 2          # t2 = i * 4
    	add  t2, s0, t2          # indirizzo di memoria di vector[i]
    	lw   x9, 0(t2)           # x9 = vector[i]
    	
    	blt x9, t0, Azzera
    	
    	add x9, x9, x9
    	sw x9, 0(t2)
    	j Incrementa
    	
Azzera:

	# Metto il valore nell'indirizzo di memoria di vector[i]
	sw zero, 0(t2)
	
Incrementa:

	addi x11, x11, 1
	j cicloFor

endFor:
	
	li a7, 10
	ecall
