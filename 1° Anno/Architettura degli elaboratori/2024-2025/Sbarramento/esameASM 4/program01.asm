##########################################
# INSERIRE I PROPRI DATI QUI
# Nome:
# Cognome:
# Matricola:
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

