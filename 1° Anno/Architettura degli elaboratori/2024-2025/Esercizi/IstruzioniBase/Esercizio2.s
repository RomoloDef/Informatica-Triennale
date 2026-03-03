# Dato un array di 4 numeri, sovrascrivre il terzo numero con la somma del primo e del secondo numero

.globl main

.data

array: .word 10, 20, 30, 40

.text
 
main:
	
	# Carico i registri dalla memoria
	la t0, array
	lw t1, 0(t0)
	lw t2, 4(t0)
	lw t3, 8(t0)
	lw t4, 12(t0)
	
	# Effettuo operazioni:
	add t5, t2, t1 
	
	# Sovrascrivo
	sw t5, 8(t0) 			# Sarebbe: registro_con_valore_da_salvare, indirizzo di memoria del numero da sovrascrivere
	