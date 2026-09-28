# factorial N!

.data

N: .word 5
rez: .word 0

.text

lw a0,N
jal factorial # these two call F(N)

mv a0,a7
li a7,1
ecall

li a7, 10     # se dimentichiamo questo andiamo in un ciclo infinito
ecall

factorial:
addi sp,sp,-4 # lo stack LO SCRIVO ALLA FINE
sw a0,0(sp)   # In realtà a0 non serve conservarlo!

li a7,1       # neutro per la moltiplicazione

While: 
	beqz a0,EndWhile
	mul a7,a7,a0
	addi a0,a0,-1
	j While
	
EndWhile:
la a6,rez
sw a7,(a6)

lw a0,0(sp)
addi sp,sp,4  # se mi dimentico questo ho un memory leak
ret           # sarebbe jr ra 

