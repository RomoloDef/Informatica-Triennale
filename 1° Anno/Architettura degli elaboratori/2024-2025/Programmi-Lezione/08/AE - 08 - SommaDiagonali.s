.data
	matrice:	.word	0:400			# matrice 20x20
	LATO:		.word	20			# lato della matrice
.text
main:		li	a0, 0			# x = 0
		li	a1, 0			# y = 0
		lw	a2, LATO		# lato della matrice
		li	t0, 0			# somma = 0
cicloY:		beq	a1, a2, fine		# se ultima riga
cicloX:		beq	a0, a2, nextY		# se ultima colonna
		jal	is_diagonal		# test se sulla diagonale
		beqz	a0, nextX		# se falso prossima X
		jal	leggi_elemento		# altrimenti leggi
		add	t0, t0, a0		# e somma l’elemento
nextX:		addi	a0, a0, 1		# x += 1 (prossima colonna)
		j	cicloX
nextY:		addi	a1, a1, 1		# y += 1 (prossima riga)
		li	a0, 0			# x = 0  (colonna 0)
		j	cicloY
fine:		mv	a0, t0		# stampo la somma
		li	a7, 1			# syscall 1 = print integer
		ecall
		li	a7, 10			# syscall 10 = fine
		ecall


is_diagonal:
	beq	a0, a1, yes		# se x=y siamo sulla prima diagonale
	add	t0, a0, a1		# altrimenti se la somma x+y+1
	addi	t0, t0, 1		
	beq	t0, a2, yes		# è uguale al lato siamo sulla seconda
	 # altrimenti non siamo sulle due diagonali principali
	li	a3, 0			# il risultato è 0 (falso)
	jr	ra			# ritorno all’istruzione successiva alla chiamata
yes:
	li	a3, 1				# il risultato è 1 (vero)
	jr	ra					# ritorno all’istruzione successiva alla chiamata

leggi_elemento:
	mul	t0, a1, a2		# y*LATO
	add	t0, t0, a0		# x + y*LATO
	slli	t0, t0, 2		# offset = 4 * (x + y * LATO)
	la 	t1, matrice
	add	t0, t0, t1
	lw	t0, (t0)			# leggo matrice[x][y]
	jr	ra				# torno  l’esecuzione al chiamante
