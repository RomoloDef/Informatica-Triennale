.data
	Vettore:	.word	1, 2, 3, 4, 5, 6, 7, 8, 9	# vettore da sommare
	N:		.word	9							# numero di elementi
	Somma:	.word	0							# risultato
.text
	main:	li		t0, 0				# i = 0
				lw		t1, N				# lettura di N
				li		t2, 0				# somma = 0
	loop:	bge		t0, t1, fine		# è finito il ciclo?
				slli	t3, t0, 2			# offset: i*4
				la		t4, Vettore			# indirizzo di memoria
				add		t3, t3, t4 			# più spiazzamento
				lw		t3, (t3)			# lettura di Vettore[i] (riuso t3)
				add		t2, t2, t3			# somma += Vettore[i]
				addi	t0, t0, 3			# i += 3
				j		loop				# riparte il ciclo
	fine:		sw		t2, Somma, t0			# memorizzo il risultato

