# Verificare che un anno precaricato in un registro è divisibile per 4. Usa un'operazione logica (andi) per controllare i due bit meno significativi.
# Se è divisibile per 4, imposta il registro t1 a 1, altrimenti impostalo a 0 usando un salto condizionato.
# Inizializza un registro t0 con il valore dell'anno (es. 2024)

.globl main

.data

anno: .word 2024

.text

main:
	
	# Carico il valore:
	la t2, anno
	lw t0, 0(t2)
	li t3, 0
	
	# Isolo gli ultimi due bit del valore:
	andi t4, t0, 3
	
	# Effettuo un salto:
	bne t4, t3, else
	li t1, 1
else:
	
	li t1, 0
	
	
	