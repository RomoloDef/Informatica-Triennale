##########################################
# INSERIRE I PROPRI DATI QUI
# Nome:	Romolo
# Cognome: Deffereria
# Matricola: 2114887
##########################################

# NON MODIFICARE IL CODICE DA QUI...
.data
    bufferIn:  .space 26
    bufferOut: .space 50

.text

main:
    li a7, 8       # Codice per input stringa
    la a0, bufferIn  # Carica indirizzo base in $a0
    li a1, 26      # Alloca al massimo 24 caratteri + \n + \0
    la a2, bufferOut # Carica indirizzo base in $a1
    li a3, 50		# dimensione bufferOut
    ecall          # $a0 contiene l'indirizzo base della stringa
# ... A QUI

##########################################
## INSERIRE IL PROPRIO CODICE QUI

    mv t0, a0           # t0 = puntatore alla stringa
    li t2, 0            # t2 = accumulatore del numero completo (N)
    li t3, 0            # t3 = maschera dei bit da selezionare (M)
    
    li t6, 10           # Valore ASCII per '\n'
    li t5, 57           # Valore ASCII per '9'
    
    li s0, 1            # Costante 1 usata per gli shift della maschera (1 << V)

ciclo:

    lb t1, 0(t0)        # Legge il carattere corrente
    
    # Se il carattere è '\n' o '\0', fine della stringa
    beq t1, t6, fineStringa
    beq t1, x0, fineStringa

    # Converto il carattere ASCII nel suo valore numerico
    bgt t1, t5, lettera # Se t1 > '9' è una lettera (A-F)
    
numero:
    addi t4, t1, -48    # Cifra 0-9. Uso un registro temporaneo t4 per il valore!
    j elaborazione
    
lettera:
    addi t4, t1, -55    # Lettera A-F ('A' = 65 -> 65-55 = 10)

elaborazione:

    # 1. Costruisco il numero originale N 
    slli t2, t2, 4      # Faccio spazio shiftando a sinistra di 4 bit (* 16)
    add t2, t2, t4      # Aggiungo il valore numerico (N = N*16 + V)
    
    # 2. Costruisco la maschera
    # Devo fare (1 << V) e aggiungerlo alla maschera
    sll s1, s0, t4      # s1 = 1 shiftato a sinistra del valore numerico V (t4)
    or t3, t3, s1       # maschera = maschera OR s1
    
    addi t0, t0, 1      # Passo al prossimo carattere
    j ciclo

fineStringa:

    # Se la stringa era vuota, non stampo nulla
    # Come faccio a saperlo? Se t0 è uguale all'indirizzo iniziale a0
    beq t0, a0, esci

    # 1. Stampo il numero originale in esadecimale (syscall 34)
    mv a0, t2
    li a7, 34
    ecall
    
    # Stampo il carattere di andata a capo
    li a0, 10
    li a7, 11
    ecall
    
    # 2. Genero il nuovo numero applicando la maschera: (N AND maschera)
    and a0, t2, t3      # a0 = N & maschera
    
    # Stampo il nuovo numero in esadecimale (syscall 34)
    li a7, 34
    ecall
    
    # Stampo l'accapo finale richiesto per i test
    li a0, 10
    li a7, 11
    ecall

esci:
    li a7, 10
    ecall
