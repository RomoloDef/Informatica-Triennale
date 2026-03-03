# Scrivere un programma che dati due numerin (word) che indicano spazio e tempo, calcolare la velocità in $t0

.globl main

.data

spazio: .word 9 
tempo: .word 3

.text

main:

	# Carico gli indirizzi di memoria
	la t1, spazio
	la t2, tempo
	
	# Leggo i valori dagli indirizzo caricati
	lw t1, 0(t1)
	lw t2, 0(t2)
	
	# Effettuo la formula Velocità = Spazio / Tempo
	div t0, t1, t2
	
	# Stampa a schermo
	li a7, 1
	mv a0, t0
	ecall
	li, a7, 10
	ecall