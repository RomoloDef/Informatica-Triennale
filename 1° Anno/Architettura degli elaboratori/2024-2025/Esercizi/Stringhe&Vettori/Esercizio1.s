# Scrivi un programma che calcoli la lunghezza di una stringa definita nel segmento .data.

.globl main

.data 

stringa: .asciz "Assembler"

.text

main:

	li t0, 0 		# t0: Contiene l'iteratore del ciclo i
	la t1, stringa		# t2: Contiene l'indirizzo di memoria di stringa
	
cicloFor:

	add t2, t1, t0		# t2: Indirizzo del carattere i-esimo
	lbu t3, 0(t2)		# t3: stringa[i]
	beq t3, zero, endFor
	addi t0, t0, 1
	j cicloFor
	
endFor:
	
	# Stampo il risultato
	li a7, 1                
    	mv a0, t0
    	ecall
    
    	li a7, 10               # Exit
    	ecall
