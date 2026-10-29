# Data una stringa salvata in memoria, sostituire tutti i caratteri ' ' con il carattere underscore '_' .
# Lasciare invariati tutti gli altri caratteri. Il ciclo deve fermarsi al terminatore \0.

.data

stringa: .asciz "risc-v assembly e divertente"

.text

main:

	# Carico l'indirizzo di base della stringa
	la s0, stringa
	
	# Carico il codice ASCII del carattere spazio vuoto
	li s1, 32
	
	# Carico il codice ASCII del carattere underscore
	li s2, 95
	
	# Carico il valore per l'indice in modo tale da poter scorrere la stringa
	li x12, 0
	
cicloFor:
	
	add t0, s0, x12
	
	lbu t1, 0(t0)
	
	# Controllo se sono arrivato a fine stringa
	
	beq t1, zero, endFor
	
	# Controllo se il carattere non corrisponde con lo spazio
	
	bne t1, s1, Aumenta
	
	# Se corrisponde allora posso fare il salvataggio
	
	sb s2, 0(t0)
	
Aumenta:
	addi x12, x12, 1
	j cicloFor
	
endFor:

	mv a0, s0       # a0 = indirizzo base della stringa
	li a7, 4        # 4 = codice ecall per "Print String"
	ecall

	# Fine programma
	li a7, 10
	ecall
	
	
	