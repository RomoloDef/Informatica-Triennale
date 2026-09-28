.data
	Vettore:	.word	1, 2, 3, 4, 5, 6, 7, 8, 9	# vettore da sommare
	N:		.word	9				# numero di elementi
	Somma:		.word	0				# risultato
.text
	main:		lw	t1, N				# lettura di N
			la	t0, Vettore			# indirizzo di Vettore
			slli	t1, t1, 2			# dimensione = N * 4
			add	t1, t1, t0			# fine = ind.Vettore + dim
			li	t2, 0				# somma = 0
	loop:		bge	t0, t1, fine			# è finito il ciclo?
			lw	t3, (t0)			# lettura di Vettore[i]
			add	t2, t2, t3			# somma += Vettore[i]
			addi	t0, t0, 12			# i += 3 * dim_elemento
			j	loop
	fine:		la 	t0, Somma
			sw	t2, 4(t1)
