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
    li a7, 8       # Codice per input stringa
    la a0, buffer  # Carica indirizzo base in $a0
    li a1, 20      # Alloca al massimo 20 caratteri
    ecall          # $a0 contiene l'indirizzo base della stringa


##########################################
## INSERIRE IL CODICE QUI

#### Inizializzazione
########################

#### Run
########################
jal contaOccorrenze

mv a0, a1		# Carica il risultato per la stampa
li a7, 1		# Imposta stampa intero
ecall			# Stampa

li a0, 10		# newline
li a7, 11		# Imposta stampa carattere
ecall			# Stampa

mv a0, a2		# Carica il risultato per la stampa
li a7, 1			# Imposta stampa intero
ecall			# Stampa


li a7, 10		# Imposta uscita
ecall

#### Funzioni
########################

# Input:
#   a0: indirizzo base della stringa
# Output:
#   a1: occorrenze coppie
#   a2: somma totale
contaOccorrenze:
  li   a1, 0			# Inizializza a1
  li   a2, 0			# Inizializza a2
  li   t5, 10			# ASCII di '\n'

  lb   t0, (a0)			# Carica primo carattere
  beq  t0, t5, returnToMain	# È il carattere '\n'? Esci
  addi t0, t0, -48		# Trasforma il numero in intero
  add a2, a2, t0        		# Aggiungi il valore alla somma
  addi a0, a0, 1			# Incrementa di 1 byte il contatore

  loop:
    lb   t1, 0(a0)		# Carica carattere in posizione successiva a $t0
    beq  t1, t5, returnToMain	# È il carattere '\n'? Esci
    addi t1, t1, -48		# Trasforma il numero in intero
    add a2, a2, t1        	# Aggiungi il valore alla somma
    bne t0, t1, endIf      	# È lo stesso valore del carattere precedente?
    addi a1, a1, 1        	# Se sì, aggiorna il contatore

  endIf:
    mv t0, t1			# Salva il carattere in t0 come nuovo $t0
    addi a0, a0, 1		# Incrementa di 1 (byte) il puntatore
    j loop			# Ripeti il ciclo

  returnToMain:
    ret				# Ritorna a main
