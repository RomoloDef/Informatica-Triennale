##########################################
# INSERIRE I PROPRI DATI QUI
# Nome:
# Cognome:
# Matricola: 1234
##########################################

# NON MODIFICARE QUESTA PARTE
.data
buffer: .space 20

.text

main: 
	li a7, 8        # Syscall per input stringa (codice per leggere stringa)
	la a0, buffer   # Carica indirizzo base in a0
	li a1, 20       # Massimo 20 caratteri
	ecall           # Effettua la chiamata di sistema

##########################################
## INSERIRE IL CODICE QUI