# Scrivere un programma che, preso un intero n in memoria, calcola la somma dei primi n interi

.globl main

.data

N: .word 5

.text

main:

	# Carico i registri
	xor t0, t0, t0 			# Lo uso per l'indice i
	la t1, N			# Inserisco N
	
	# Estraggo i valori dagli indirizzi di memoria
	lw t1, 0(t1)

	li t2, 0            # t2 = L'accumulatore per la somma (parte da 0)

    	
cicloFor:

	bgt t0, t1 endFor
	add t2, t2, t1 
	addi t0, t0, 1
	j cicloFor
	
endFor:

	# Stampa a terminale
	li a7, 1
	mv a0, t2
	ecall
	
	# Fine programma
	li a7, 10
	ecall
	