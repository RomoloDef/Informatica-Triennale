##########################################
# INSERIRE I PROPRI DATI QUI
# Nome:
# Cognome:
# Matricola: 4324
##########################################

# NON MODIFICARE QUESTA PARTE

.data 
N: .word 0
matrix: .word 0:800

.text

# first value is the size of the square matrix
li a7,5
ecall

la t0,matrix         # t0 is also cursor

sw   a0,N,t1         # put N into memory
mv   t1,a0           # N
mul  t1,t1,t1        # NxN number of elements
slli t1,t1,2         # in bytes
add  t1,t1,t0        # t1 is final position in memory

# store all the elements of the matrix
ww:
	bge t0,t1,endww
	ecall
	sw a0,(t0)
	addi t0,t0,4
j ww

endww:
la a0,matrix          # matrix base address in a0 
la a1,N               # N address is in a1
li t1,0
li t0,0
li a7,0

    
##########################################
## INSERIRE IL PROPRIO CODICE QUI

    jal contaSomma
    li a7, 1       # Set print integer
    ecall          # Print

#	test_infinite_loop_with_correct_output:
#		nop
#		j test_infinite_loop_with_correct_output
    li a7, 10      # Set exit
    ecall
    
#### Functions
########################
# Input:
#   a0: base address of the matrix
#   a1: base address of N
# Output:
#   a0: output of exercise
contaSomma:
#	li a0, 0x1003   # Misaligned address (assuming word-aligned memory model)
#	lw a1, 0(a0)    # Will fail on strict alignment systems

    li t2,0      # t2 <- metto la somma
    lw t6,(a1)   # t6 <- carico N in t6
    
    slli t3,t6,2 # t3 <- è la grandezza di una riga (Nx4)
    mul t1,t6,t3 # NxNx4...
    add t1,t1,a0 # t1 <- NxNx4+ind_base di matrix è l'ultimo byte +1 
    mv t0,a0     # t0 <- contatore corrente

    li t5,2
    bge t6,t5,While # caso N>=2 devo calcolarlo, salto a Whilte
    li t5,1
    bge t6,t5,Caso1 # se N = 1 prendo l'unico elemento
    Caso0:
    li a0,0         # se N = 0 il risultato è zero
    ret
    Caso1:
    lw a0,(a0)
    ret
    
    While:
        bge t0,t1,returnToMain  # esci se finite le righe
        lw t5,(t0)              # primo elemento della riga
        add t2,t2,t5
        
        lw t5,4(t0)             # secondo elemento della riga
        add t2,t2,t5
        
        add t0,t0,t3            # salto alla riga successiva
        j While
 
returnToMain:
    mv a0,t2
    ret                        # Return to main (replacing jr ra)
