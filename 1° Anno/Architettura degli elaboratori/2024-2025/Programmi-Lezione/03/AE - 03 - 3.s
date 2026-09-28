# selezionare il massimo da un vettore
.globl main

.data
	vector: .word 4, 3, -5, 500
	rez: .word 0
	
.text

main:
	# Carichiamo l'indirizzo di "vector"
	la t5, vector  

	# Carichiamo i valori della memoria nei registri
	lw t0, 0(t5)    # A
	lw t1, 4(t5)    # B
	lw t2, 8(t5)    # C
	lw t3, 12(t5)   # D

	or t4, zero, t0  # assumiamo A come massimo iniziale
CheckB:
	blt t4, t1, UpdateB
	jal CheckC
UpdateB:
	or t4, zero, t1
CheckC:
	blt t4, t2, UpdateC
	jal CheckD
UpdateC:
	or t4, zero, t2
CheckD: 
	blt t4, t3, UpdateD
	jal End
UpdateD:
	or t4, zero, t3
End:
	sw  t4, rez, t5  # salviamo il massimo in memoria
