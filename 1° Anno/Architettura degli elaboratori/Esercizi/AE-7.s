# Dati due vettori vetA e vetB e un vettore di destinazione vetC (inizializzato a 0), tutti di dimensione N, 
# eseguire per ogni indice i da 0 a N-1 l'operazione: vetC[i] = vetA[i] + vetB[i]

.data

vetA: .word 10, 20, 30, 40, 50
vetB: .word -5, 15, -10, 0, 25
vetC: .word 0, 0, 0, 0, 0
N:    .word 5

.text

main:

	# Carico l'indirizzo base del vettore A
	la s0, vetA
	
	# Carico l'indirizzo base del vettore B
	la s1, vetB
	
	# Carico l'indirizzo base del vettore C
	la s2, vetC
	
	# Carico la lunghezza 
	lw x10, N
	
	# Carico il numero da cui far partire l'iterazione
	li x11, 0
	
cicloFor:

	bge x11, x10, endFor
	
	# Calcolo indirizzo e caricamento di vetA[i]
	slli t2, x11, 2          # t2 = i * 4
    	add  t2, s0, t2          # indirizzo di memoria di vetA[i]
    	lw   x9, 0(t2)           # x9 = vetA[i]
    	
    	# Calcolo indirizzo e caricamento di vetB[i]
	slli t3, x11, 2          # t2 = i * 4
    	add  t3, s1, t2          # indirizzo di memoria di vetB[i]
    	lw   x8, 0(t3)           # x8 = vetB[i]
    	
    	# Sommo i due elementi
    	add x9, x9, x8
    	
    	# Calcolo indirizzo e caricamento di vetC[i]
	slli t4, x11, 2          # t2 = i * 4
    	add  t4, s2, t2          # indirizzo di memoria di vetB[i]
    	
    	# Salvo in memoria il valore calcolato
    	sw   x9, 0(t4)   
    	
    	addi x11, x11, 1
    	
    	j cicloFor        
    	
endFor:

	li a7, 10
	ecall
