# Scrivere un programma in linguaggio assembly RISC-V che dato un vettore ingresso vector e la sua dimensione N calcoli due somme dei numeri del vettore:
# 1. La prima somma deve sommare i valori del vettire di indice dispari (Indice parte da 1)
# 2. La seconda somma deve sommare i valori di un vettore con indice pari (Indice parte da 0)

.data 

vector: .word 4, -1, 5, 500, 0, 10000, -256

N: .word 5

SommaDispari: .word 0

SommaPari: .word 0

.text

main:

	# Carico l'indirizzo base del vettore
	
	la s0, vector
	
	# Carico il primo elemento del vettore
	
	lw x9, 0(s0)
	
	# Carico la lunghezza del vettore con cui fare il confronto durante il ciclo e 
	
	lw x10, N
	
	# Carico il valore delle due somme per poi aggiungere i valori
	
	lw t0, SommaDispari
	lw t1, SommaPari
	
	# Carico il numero da cui far partire l'indice
	
	li x11, 0

CicloFor:

    	bge  x11, x10, endFor    # Se i >= N, esci dal ciclo

    	# Calcolo indirizzo e caricamento di vector[i]
    	slli t2, x11, 2          # t2 = i * 4
    	add  t2, s0, t2          # t2 = &vector[i]
    	lw   x9, 0(t2)           # x9 = vector[i]

    	# Controllo indice pari o dispari
    	andi t3, x11, 1          # t3 = i % 2
    	beq  t3, zero, IndicePari

    	# Somma dispari
    	add  t0, t0, x9
    	j    Incrementa

IndicePari:
   	 # Somma pari
    	add  t1, t1, x9

Incrementa:
    	addi x11, x11, 1         # i++
    	j    CicloFor

endFor:
    # Salvo i risultati finali in memoria
    
    la   t4, SommaDispari
    sw   t0, 0(t4)

    la   t5, SommaPari
    sw   t1, 0(t5)

    # Terminazione programma
    li   a7, 10
    ecall

	
	
	
	

