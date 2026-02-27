##########################################
# INSERIRE I PROPRI DATI QUI
# Nome:
# Cognome:
# Matricola: 1234
##########################################

# NON MODIFICARE IL CODICE DA QUI...
.data
    buffer: .space 26
    output: .byte  0,0,0,0,0,0,0,0,0  # Un carattere extra per la fine della stringa

.text

main:
    li a7, 8       # Codice per input stringa
    la a0, buffer  # Carica indirizzo base in $a0
    li a1, 26      # Alloca al massimo 24 caratteri + \n + \0
    ecall          # $a0 contiene l'indirizzo base della stringa
    la a2, output
# ... A QUI

##########################################
## INSERIRE IL PROPRIO CODICE QUI

#### Inizializzazione
########################

jal codificaOttale

mv t0, a3	# Salva il valore di a3 per dopo

li a7, 4	# Imposta stampa stringa
mv a0, a2	# Carica il risultato per la stampa
ecall		# Stampa la stringa

li a0, 10	# newline
li a7, 11	# Imposta stampa carattere
ecall		# Stampa newline

mv a0, t0	# Carica il risultato per la stampa
li a7, 1	# Imposta stampa intero
ecall		# Stampa intero

li a0, 10	# newline
li a7, 11	# Imposta stampa carattere
ecall		# Stampa newline

mv a0, a4	# Carica il risultato per la stampa
li a7, 1	# Imposta stampa intero
ecall		# Stampa intero


li a7, 10	# Imposta uscita
ecall

#### Funzioni
########################

# Input:
#   a0: indirizzo base della stringa di input
#   a2: indirizzo base della stringa di output
# Output:
#   a3: 0 se tutta la stringa di input e' stata tradotta; altrimenti, 1
#   a4: numero di caratteri nella stringa ottale prodotta
codificaOttale:
  addi sp, sp, -4		 # prepara lo stack per la funzione.
  sw   a2, 0(sp)			
  
  li a3, 0
  li a4, 0         		 
  li t5, 10         		 # '\n'

  loop:
    li t6, 0			 # Inizializza la somma temporanea
    
    li a3, 0              	 # Se la stringa finisce qui, tutti i caratteri sono stati trasposti
    lb t1, 0(a0)		 # Carica primo carattere
    beq  t1, t5, returnToMain	 # Il primo carattere e' '\n'? Esci
    addi t1, t1, -48		 # Trasformalo in intero (da ASCII)
    slli t1, t1, 2		 # Moltiplicalo per 4              
    add t6, t6, t1		 # Aggiungi alla somma la prima cifra ottale
    addi a0, a0, 1		 # Incrementa puntatore memoria
    
    li a3, 1			 # Se la stringa finisce qui o al prossimo carattere, NON tutti sono stati trasposti
    lb t2, 0(a0)		 # Carica secondo carattere
    beq t2, t5, returnToMain	 # Il secondo carattere e' '\n'? Esci
    addi t2, t2, -48		 # Trasformalo in intero (da ASCII)
    slli t2, t2, 1		 # Moltiplicalo per 2              
    add t6, t6, t2		 # Aggiungi alla somma la seconda cifra ottale
    addi a0, a0, 1		 # Incrementa puntatore memoria
    
    lb t3, 0(a0)		 # Carica terzo carattere
    beq  t3, t5, returnToMain	 # Il terzo carattere e' '\n'? Esci
    addi t3, t3, -48		 # Trasformalo in intero (da ASCII)
    add t6, t6, t3		 # Aggiungi alla somma la terza cifra ottale
    addi a0, a0, 1		 # Incrementa puntatore memoria
    
    
    addi t6, t6, 48		 # Trasforma t6 in ASCII (da intero)
    sb t6, 0(a2)		 # Scrivi in memoria il risultato
    addi a2, a2, 1		 # Incrementa il puntatore di scrittura
    addi a4, a4, 1		 # Incrementa il contatore delle cifre ottali
    
    j loop

  returnToMain:         
    lw a2, 0(sp)
    addi sp, sp, 4
    ret
