# Si vuole tradurre in linguaggio assembler questa istruzione: vector[12] = vector[6] + n

.data
vector: .word 1, -2, 3, -4, 5, -6, 7, -8, 9, 10, 11, 12, 13
n: .word 5

.text
main:

	# Carico il valore di n in un registro
	lw t1, n
	
	# Carico l'indirizzo base di vector
	la s5, vector					# questo ora contiene l'indirizzo di vectot[0]
	
	# Carico il valore di vector[6] tramite l'assegnazione e seguendo il vincolo di allineamento
	lw x9, 24(s5)
	
	# Posso sommare il valore dei due registri e posizionarlo momentaneamente in un registro temporaneo
	add x10, x9, t1
	
	# E come ultimo passaggio salvarlo nella locazione di memoria 12 del vettore
	sw x10, 48(s5)
	
# Fine programma

	li a7, 10
	ecall
    
