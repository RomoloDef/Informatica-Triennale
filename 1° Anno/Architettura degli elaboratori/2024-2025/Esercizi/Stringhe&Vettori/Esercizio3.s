# Scorri la stringa "Assembler" e sostituisci ogni carattere con quello successivo (A -> B, s -> t, ecc.).

.globl main

.data 

stringa: .asciz "Assembler"

.text

main:

	li t0, 0		# t0: Contiene l'indice i
	la t1, stringa		# t1: Contiene l'indirizzo di memoria della stringa
	
cicloFor:

	add t2, t1, t0		# t2: Indirizzo del carattere i-esimo
	lbu t3, 0(t2)		# t3: stringa[i]
	beq t3, zero, endFor
	
	addi t3, t3, 1		# t4: stringa[i+1]
	sb t3, 0(t2)
	addi t0, t0, 1
	j cicloFor
	
endFor:

	li   a7, 4          
   	la   a0, stringa    # Carico l'indirizzo della stringa modificata
    	ecall

    	li   a7, 10
    	ecall
