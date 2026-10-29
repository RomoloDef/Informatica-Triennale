# Data una stringa di caratteri, terminante con il carattere \0 e un carattere bersaglio, scorrere la stringa e contare quanti caratteri
# sono uguali a quello bersaglio. Salvare il risultato nella variabile conteggio in memoria

.data

stringa:   .asciz "architettura degli elaboratori"
target:    .byte 'a'
conteggio: .word 0

.text

main:

	# Carico l'indirizzo base della stringa
	la s0, stringa
	
	# Carico il valore target
	lb t0, target
	
	# Carico il numero del conteggio in un determinato registro
	li t1, 0
	
	# Carico l'indice per scorrere la stringa
	li x9, 0
	
cicloFor:

	# Non mi serve il costrutto slli perchè si conta di byte in byte e non in word quindi:
	add t2, s0, x9
	
	# Carico di conseguenza il carattere corrente
	lbu t3, 0(t2)
	
	# Controllo se sono arrivato alla fine della stringa
	beq t3, zero, endFor
	
	# Posso fare ora il confronto
	bne t3, t0, Aumenta
	
	# Se il carattere è uguale a quello target allora:
	addi t1, t1, 1
	
Aumenta:
	addi x9, x9, 1
	j cicloFor
	
endFor:
	# Effettuo il salvataggio in memoria
	
	la t4, conteggio
	sw t1, 0(t4)
	
	li a7, 10
	ecall
	
	