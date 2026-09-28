# Immagina di avere un array che rappresenta dei punteggi. 
# Vuoi "normalizzare" i dati: ogni volta che trovi un numero negativo, devi sostituirlo con lo zero direttamente nella memoria dell'array.

.globl main 

.data

array: .word 10, -5, 8, -1, 3, -12, 7

.text

main:

	li t0, 0	# t0: Contiene l'iteratore
	li t1, 7	# t1: Contiene la lunghezza dell'array
	la t2, array	# t2: Contiene l'indirizzo base dell'array
	
cicloFor:

	bge t0, t1, endFor      # Se i >= 7, esci
    
    	# Calcolo l'offset
    	slli t4, t0, 2          # t4 = i * 4
    	add  t5, t2, t4         # t5 = Indirizzo base + Offset
    
    	lw t6, 0(t5)            # t6 = array[i]
    	
    	bge t6, zero, positivo
    	
negativo:

	sw zero, 0(t5)

positivo:

	addi t0, t0, 1          # Incrementa SEMPRE l'iteratore
    	j cicloFor              # Torna su
    	
endFor:

	li a7, 10               # Exit
    	ecall