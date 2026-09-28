.data
	#matrice2D:	.word	0:400			# matrice quadrata di 20x20 word
	matrice2D:	.word 	14,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,16,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-12,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-11,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,26,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-19,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-18
	DIM:		.word	20			# lato della matrice
.text
main:			li	t0, 0			# coordinata y (colonne)
			li	t1, 0			# coordinata x (righe)
			li	t2, 0			# somma iniziale
			lw	t3, DIM			# lato della matrice
			la	t4, matrice2D		# carico matrice2D[x][y]
cicloRighe:		bge	t1, t3, fine		# se finite le righe
cicloColonne:		bge	t0, t3, nextRiga	# se finite le colonne
			bne	t0, t1, continua	# se x != y si continua
			mul	t5, t1, t3		# x*N
			add	t5, t5, t0		# x*N + y
			slli	t5, t5, 2		# word => molt. per 4
			add	t5, t4, t5
			lw 	t5, (t5)
			add	t2, t5, t2		# e lo accumulo
continua:		addi	t0, t0, 1		# x += 1
			j	cicloColonne		# alla colonna successiva
nextRiga:		li	t0, 0			# azzero y
			addi	t1, t1, 1		# x += 1
			j	cicloRighe		# alla riga successiva
fine:			mv	a0, t2			# preparo la stampa
			li	a7, 1			# syscall 1 = print int
			ecall
			li	a7, 10			# syscall 10 = exit
			ecall
