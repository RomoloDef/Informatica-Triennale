.text
	li t0, 1			# selezioniamo caso 1
	slli t0, t0, 2	 		# A*4
	la t1, dest			# indirizzo primo case
	add t1, t0, t1          	# indirizzo selezionato
	lw t1,  (t1)			# carico indirizzo 
	jr t1				# salto a registro
caso0:					# codice del caso 0
	j endSwitch
caso1:					# codice del caso 1
	j endSwitch
casoN:					# codice del caso N
	j endSwitch
endSwitch:
						# codice seguente
.data
dest: 	.word caso0, caso1, casoN
A: .byte
