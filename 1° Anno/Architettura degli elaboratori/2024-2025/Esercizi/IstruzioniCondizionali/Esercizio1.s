# Scrivere un programma che metta in $t0 1 se il valore di Batman è maggiore di quello di Robin, altrimento metti 0.

.globl main

.data 

Batman: .word 25
Robin: .word 19

.text

main:
	
	# Carico i registri
	la t1, Batman
	la t2, Robin
	
	# Estraggo dagli indirizzi di memoria
	lw t1, 0(t1)
	lw t2, 0(t2)
	
	# Eseguo l'istruzione condizionale IF
	bge t1, t2, else
	li t0, 0
	j esci
	
else:
	li t0, 1

esci:

	li a7, 10
	ecall

	
