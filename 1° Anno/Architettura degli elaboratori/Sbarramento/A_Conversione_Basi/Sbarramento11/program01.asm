##########################################
# INSERIRE I PROPRI DATI QUI
# Nome:
# Cognome:
# Matricola:
##########################################

# NON MODIFICARE IL CODICE DA QUI...
.data
    buffer: .space 50

.text

main:
    li a7, 8       # Codice per input stringa
    la a0, buffer  # Carica indirizzo base in a0
    li a1, 50      # Alloca al massimo 48 caratteri + \n + \0
    ecall          # a0 contiene l'indirizzo base della stringa di input
# ... A QUI

##########################################
## INSERIRE IL PROPRIO CODICE QUI

