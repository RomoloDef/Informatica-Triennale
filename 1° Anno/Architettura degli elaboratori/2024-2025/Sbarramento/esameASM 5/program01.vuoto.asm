##########################################
# INSERIRE I PROPRI DATI QUI
# Nome:
# Cognome:
# Matricola:
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

