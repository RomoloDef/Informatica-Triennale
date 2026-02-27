##########################################
# INSERIRE I PROPRI DATI QUI
# Nome:
# Cognome:
# Matricola: 1234
##########################################

# NON MODIFICARE QUESTA PARTE
.data
    buffer: .space 20 # Allocazione di 20 byte per la stringa

.text

main:
    li a7, 8       # Codice per input stringa
    la a0, buffer  # Carica indirizzo base in a0
    li a1, 20      # Alloca al massimo 20 caratteri
    ecall          # a0 contiene l'indirizzo base della stringa


##########################################
## INSERIRE IL CODICE QUI

jal contaOccorrenze

# Stampa somma delle coppie
mv a0, a1             # somma delle coppie
li a7, 1              # stampa intero
ecall

# Stampa newline
li a7, 11             # stampa carattere
li a0, 10             # '\n'
ecall

# Stampa numero di cifre
li a7, 1              # stampa intero
mv a0, a2             # numero cifre
ecall

# Fine
li a7, 10             # exit
ecall	
    

#### Functions
########################
# Input:
#   a0: base address of the string
# Output:
#   a1 = somma delle coppie
#   a2 = numero totale di cifre
contaOccorrenze:
#	li a0, 0x1003   # Misaligned address (assuming word-aligned memory model)
#	lw a1, 0(a0)    # Will fail on strict alignment systems

    mv s0, a0             # s0 = indirizzo corrente (puntatore)
    li a1, 0              
    li a2, 0              
    li t6, 10		  # '\n'

loop:
    lb t0, 0(s0)          # t0 = byte corrente
    beq t0, t6, fineLoop  # se t0 == '\n', esci
    addi a2, a2, 1        # incrementa numero cifre

    lb t1, 1(s0)          # t1 = prossimo carattere
    beq t1, t6, ultimo    # se t1 == '\n', ultimo numero singolo

    # === Calcola valore coppia: t0t1 ===
    addi a2, a2, 1        # incrementa numero cifre
    
    addi t0, t0, -48      # t0 = cifra1
    addi t1, t1, -48      # t1 = cifra2
    li t2, 10
    mul t0, t0, t2        # cifra1 * 10
    add t0, t0, t1        # + cifra2
    add a1, a1, t0        # somma totale += t0

    addi s0, s0, 2        # passa alla prossima coppia
    j loop

ultimo:
    # Ultima cifra singola
    addi t0, t0, -48
    add a1, a1, t0

fineLoop:
    ret