.data
	#matrice2D:	.word	0:400		# matrice di 20x20 word
	matrice2D:	.word 	14,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,16,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-12,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-11,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,26,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-19,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-18

	DIM:		.word	20			# lato della matrice quadrata
.text	# preparazione degli indirizzi e degli incrementi
main:	# t0 = indirizzo dell’elemento corrente
	# t1 = incremento di una riga + 1 elemento (in byte)
	# t2 = somma parziale
	# t3 = indirizzo finale della matrice (byte seguente)
	la	t0, matrice2D		# indirizzo dell’inizio
	lw	t1, DIM			# lato della matrice
	addi	t3, zero, 400			# DIM * DIM elementi
	slli	t3, t3, 2		# totale DIM^2 * 4 byte
	add	t3, t3, t0		# indirizzo finale
	addi	t1, t1, 1		# DIM + 1
	slli	t1, t1, 2		# incremento = (DIM+1)*4
	li	t2, 0			# somma iniziale
	
	# t0 = indirizzo dell’elemento corrente
	# t1 = incremento di una riga + 1 elemento
	# t2 = somma parziale
	# t3 = indirizzo finale della matrice (subito dopo)
# ciclo che scandisce un elemento ogni DIM+1
ciclo:	bge	t0, t3, fine		# se è finita la matrice esco
	lw	t4, (t0)		# carico matrice2D[x][x]
	add	t2, t4, t2		# e lo accumulo
	add	t0, t0, t1		# x += (DIM+1)*4
	j		ciclo
# stampa del risultato
fine:	mv	a0, t2			# preparo la stampa
	li	a7, 1			# syscall 1 = print int
	ecall
	li	a7, 10			# syscall 10 = stop
	ecall

			
