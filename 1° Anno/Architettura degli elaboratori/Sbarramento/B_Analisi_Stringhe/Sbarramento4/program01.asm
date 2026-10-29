##########################################
# INSERIRE I PROPRI DATI QUI
# Nome: Romolo
# Cognome: Deffereria
# Matricola: 2114887
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

    # Chiamo la funzione contaOccorrenze
    jal contaOccorrenze

    # --- STAMPA NEL MAIN ---
    # 1. Stampo il primo valore (a1 = occorrenze caratteri identici consecutivi)
    mv a0, a1
    li a7, 1        # 1 = Print Int
    ecall

    # 2. Vado a capo stampando il carattere '\n' (ASCII 10)
    li a0, 10       
    li a7, 11       # 11 = Print Char
    ecall
    
    # 3. Stampo il secondo valore sulla nuova riga (a2 = somma cifre)
    mv a0, a2
    li a7, 1        # 1 = Print Int
    ecall

    # 4. Accapo finale richiesto dalla sezione "Risultato atteso" del PDF
    li a0, 10       
    li a7, 11       # 11 = Print Char
    ecall
    
    # Fine Programma
    li a7, 10
    ecall

contaOccorrenze:
    mv s0, a0       # Sposto l'indirizzo base nel registro s0
    
    li t0, 0        # Indice i = 0 per lo scorrimento del ciclo
    li t1, 10       # Valore ASCII del carattere '\n' (fine stringa)
    li t2, 48       # Valore ASCII del carattere '0' (per convertire da ASCII a numero)
    
    li a1, 0        # a1 = Numero di occorrenze (carattere preceduto da uno identico)
    li a2, 0        # a2 = Somma totale dei valori numerici presi una cifra alla volta

ciclo:
    add t3, s0, t0  # Calcolo l'indirizzo di buffer[i]
    lbu t4, 0(t3)   # Carattere corrente buffer[i]
    
    # Controllo se sono arrivato alla fine della stringa ('\n' oppure '\0')
    beq t4, t1, fineStringa
    beq t4, zero, fineStringa
    
    # Converto il carattere corrente da ASCII a valore numerico (t4 - 48) e lo sommo ad a2
    sub t6, t4, t2  # t6 = cifra numerica (0..9)
    add a2, a2, t6  # Aggiorno la somma totale delle cifre
    
    # Carico il carattere successivo buffer[i+1]
    lbu t5, 1(t3)
    
    # Verifico se formano una coppia di caratteri consecutivi identici
    beq t4, t5, conteggioOccorrenze
    
    # Se non sono uguali, avanzo l'indice t0 di 1 e ripeto
    addi t0, t0, 1
    j ciclo

conteggioOccorrenze:
    # Aumento il numero delle coppie uguali E avanzo l'indice t0 di 1
    addi a1, a1, 1
    addi t0, t0, 1
    j ciclo
        
fineStringa:
    ret             # Ritorna al main con i risultati in a1 e a2