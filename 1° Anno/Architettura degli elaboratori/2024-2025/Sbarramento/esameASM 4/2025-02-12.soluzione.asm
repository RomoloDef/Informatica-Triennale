##########################################
# INSERIRE I PROPRI DATI QUI
# Nome:
# Cognome:
# Matricola: 123412
##########################################

# NON MODIFICARE QUESTA PARTE

.data
    buffer: .space 20
.text
.globl main
#li a0, 0x1003   # Misaligned address (assuming word-aligned memory model)
#lw a1, 0(a0)    # Will fail on strict alignment systems
main:
    li a7, 8       # Code for string input
    la a0, buffer  # Load base address in a0
    li a1, 20      # Allocate at most 20 characters
    ecall          # a0 contains the base address of the string

    
##########################################
## INSERIRE IL PROPRIO CODICE QUI

    jal contaOccorrenze
    li a7, 1       # Set print integer
    ecall          # Print

    li a0, '\n'
    li a7, 11      # Set print character
    ecall          # Print

    mv a0, a1      # Load result for printing (from a1, which replaced $v1)
    li a7, 1       # Set print integer

    ecall          # Print
    li a7, 10      # Set exit
    ecall
    
#### Functions
########################
# Input:
#   a0: base address of the string
# Output:
#   a0: sum of even occurrences
#   a1: sum of odd occurrences
contaOccorrenze:
    li t1, '\n'                # Newline character
    lb s0, (a0)
    beq s0, t1, returnToMain   # Is it the '\n' character? Exit, otherwise skip first character
    addi a0, a0, 1
    li t2,2
    li t3,9
    li t4,0
    li t5,0
    
 tycle:
    lb s0, (a0)                # Load character
    beq s0, t1, returnToMain   # Is it the '\n' character? Exit
    addi s0, s0, -48           # Transform the number to integer (0x30 = 48)
    
    ble s0, t2, endIf           # Don't count if 0,1,2
    bge s0, t3, endIf           # Don't count if greater than 9
    andi s0, s0, 1             # s0 equals 1 if s0 is odd
    beq s0, zero, pari         # Skip next instruction if even
    addi t5, t5, 1             # Increment counter 1
    j endIf
pari:
    addi t4, t4, 1             # Increment counter 0
endIf:
    addi a0, a0, 1             # Increment byte counter
    j tycle                    # Repeat the cycle
    
returnToMain:
    mv a0,t4
    mv a1,t5
    ret                        # Return to main (replacing jr $ra)
