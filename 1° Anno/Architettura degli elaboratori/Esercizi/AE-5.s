# Dato un vettore vector di dimensione N:
# 1. Calcolare la somma di tutti gli elementi strettamente maggiori di 0 e salvarla nella variabile SommaPositivi
# 2. Contare quanti sono gli elementi minori di 0 (escludendo quindi lo zero) e salvare il conteggio nella variabile ContaNegativi

.data

vector:	.word 12, -5, 0, 8, -20, 3, -1, 15
N: .word 8
SommaPositivi: .word 0
ContaNegativi: .word 0

.text

main:

	# Carico il valore della somma e del conteggio in due registri
	
	lw t0, SommaPositivi
	lw t1, ContaNegativi
	
	# Carico l'indirizzo base del vettore
	
	la s0, vector
	
	# Carico il valore della lunghezza del vettore
	
	lw x10, N
	
	# Carico il valore da cui far partire l'indice nel ciclo
	
	li x11, 0
	
cicloFor:

	bge x11, x10, endFor
	
	# Calcolo indirizzo e caricamente di vector[i]
	
	slli t2, x11, 2          # t2 = i * 4
    	add  t2, s0, t2          # indirizzo di memoria di vector[i]
    	lw   x9, 0(t2)           # x9 = vector[i]
    	
    	# Controllo se vector[i] sia positivo o negativo
    	blt x9, zero, conteggioNegativi
    	beq x9, zero, Incrementa
    	
    	add t0, t0, x9
    	j Incrementa
    	
conteggioNegativi:
	addi t1, t1, 1		# incremento il conteggio dei negativi
	
Incrementa:
	addi x11, x11, 1	# devo incrementare l'indice
	j cicloFor
	
endFor:

	la t3, SommaPositivi
	sw t0, 0(t3)
	
	la t4, ContaNegativi
	sw t1, 0(t4)
	
	# fine del programma
	
	li a7, 10
	ecall
	