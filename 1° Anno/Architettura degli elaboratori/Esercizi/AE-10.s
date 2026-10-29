# Data una stringa stringa, trasformare tutti i caratteri alfabetici minuscoli ('a' - 'z') nei rispettivi caratteri MAIUSCOLI ('A' - 'Z'),
# lasciando inalterati spazi, numeri o segni di punteggiatura.

.data

stringa: .asciz "ciao Mondo 2026!"

.text

main:

	# Carico l'indirizzo base della stringa
	la s0, stringa
	
	# Carico l'indice per il ciclo for
	li t0, 0
	
	# Carico i codici ASCII corretti di 'a' (97) e 'z' (122)
	li t1, 97
	
	li t2, 122
	
cicloFor:

	add t3, s0, t0
	
	lbu t4, 0(t3)
	
	# Controllo se non si è arrivati alla fine della stringa
	beq t4, zero, endFor
	
	# Controllo se il carattere sia minuscolo:
	# 1. Se è minore di 97 ('a'), come lo spazio (32) o 'M' (77), NON sostituire
	blt t4, t1, nonSostituire
	
	# 2. Se è >= 97 E anche <= 122 ('z'), allora salta a sostituisci
	ble t4, t2, sostituisci
	
nonSostituire:
	# aumenta di uno l'indice
	addi t0, t0, 1
	j cicloFor

sostituisci:

	# Creo il carattere in maiuscolo
	addi t4, t4, -32
	
	# Sostituisco nella stringa
	sb t4, 0(t3)
	
	addi t0, t0, 1
	
	j cicloFor
	
	
endFor:

	mv a0, s0       # a0 = indirizzo base della stringa
	li a7, 4        # 4 = codice ecall per "Print String"
	ecall

	# Fine programma
	li a7, 10
	ecall
	


