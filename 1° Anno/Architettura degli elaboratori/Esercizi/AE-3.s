# selezionare il massimo da un vettore

.data
	vector: .word 4, 3, -5, 500
	salvataggio: .word 0
	
.text

main:

	# Carico l'indirizzo base del vettore
	la s5, vector
	
	# Carico gli elementi del vettore
	lw x9, 0(s5)
	lw x10, 4(s5)
	lw x11, 8(s5)
	lw x12, 12(s5)
	
	# Adesso assumo il primo valore come massimo iniziale
	or t1, zero, x9
	
# Ora posso fare tutti i confronti con i valori del vettore

PrimoCheck:
	blt t1, x10, PrimoUpdate
	jal SecondoCheck
	
PrimoUpdate:
	or t1, zero, x10
	
SecondoCheck:
	blt t1, x11, SecondoUpdate
	jal TerzoCheck
	
SecondoUpdate:
	or t1, zero, x11
	
TerzoCheck: 
	blt t1, x12, QuartoUpdate
	jal End
	
QuartoUpdate:
	or t1, zero, x12
	
End:
	sw  t1, salvataggio, s5  # salviamo il massimo in memoria	
	
	
	
	
	