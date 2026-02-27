# Leggere tre valori dalla memoria, sommare i primi due, sottrarre il terzo e salvare il risultato finale in una nuova locazione di memoria
# I dati da inserire sono: 15, 25, 10

.globl main

.data 

valori: .word 15, 25, 10
risultato: .word 0

.text 

main:
	
	# Carico i registri dalla memoria:
	la t0, valori
	lw t1, 0(t0)
	lw t2, 4(t0)
	lw t3, 8(t0)
	
	# Effettuo le operazioni:
	
	add t4, t1, t2
	sub t5, t4, t3 
	
	# Salvo quello che ho fatto:
	la t6, risultato
	sw t5, 0(t6)
	
	
	  
