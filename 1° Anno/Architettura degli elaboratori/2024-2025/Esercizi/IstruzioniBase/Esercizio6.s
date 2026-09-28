# Scrivere un programma che converta un valore da scala Celsius a scala Fahrenheit. Riportare il risultato in $t0

# Formula: °F = (°C × 1,8) + 32.

.globl main

.data

valore_gradi: .word 5 
valore_moltiplicativo: .float 1.8 

.text

main:

	# Carico gli indirizzi di memoria
	la t0, valore_gradi
	la t1, valore_moltiplicativo
	
	# Estraggo i valori dagli indirizzi
	lw t0, 0(t0)
	flw f1, 0(t1)
	
	# Carico l'ultimo valore
	li t2, 32
	
	# Dato che devo effettuare un'operazione tra un intero e un float,
	# converto l'intero in float
	fcvt.s.w f2, t0
	fcvt.s.w f3, t2
	fmul.s f4, f1, f2
	fadd.s f4, f4, f3 
	
	# Stampo a schermo
	li a7, 2           # Codice Syscall per stampare Float (2)
    	fmv.s fa0, f4      # Sposto f4 nel registro speciale fa0
    	ecall
    
    	# Fine del programma
    	li a7, 10
    	ecall