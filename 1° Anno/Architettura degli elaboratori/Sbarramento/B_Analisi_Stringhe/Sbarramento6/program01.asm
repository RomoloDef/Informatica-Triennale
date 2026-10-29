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