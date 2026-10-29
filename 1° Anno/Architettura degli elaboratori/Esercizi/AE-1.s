.globl main
# (b - c) + (d - e)
# (4 - 3) + (9 - 4)

.data

.text

main:

	# Inserisco i dati negli appositi registri - Caso di valori interi per istruzioni logico-aritmetiche
	
	li x9, 3
	li x10, 4
	li x11, 9
	
	sub x12, x11, x10
	
	sub x13, x10, x9
	
	add x14, x13, x12
	
	# Stampa del risultato
	
	mv a0, x14
	li a7, 1			# stampa sempre il risultato del registro a0 -> quindi devo spostare il risultato in quel registro per farlo stampare
	ecall
	
	# Termine del programma
	
	li a7, 10
	ecall
	
	
	
	

