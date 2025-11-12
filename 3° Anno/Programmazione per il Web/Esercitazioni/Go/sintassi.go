package main

import (
	"fmt"
	"math"
)

func main() {
	fmt.Println("Hello, World!")

	// Vediamo le variabili e le costanti
	var i int = 3
	const pi = 3.14

	fmt.Println(i)
	fmt.Println(pi)

	// Se le variabili non sono usate, Go genera un errore di compilazione

	k := 42 // Se si utilizza questa sintassi Go deduce il tipo
	fmt.Println(k)

	// Esiste un solo tipo di ciclo: il for -> sintatticamente non ci sono le parentesi tonde
	var sum int = 0
	for i := 1; i <= 10; i++ {
		sum += i
	}
	fmt.Println("Sum:", sum)

	// Posso impostare il loop come se fosse un while anche se non esiste
	var n int = 1
	for n < 10 {
		n *= 2
	}
	fmt.Println("N:", n)

	// Esempi di uso di pow: stampa diretta e con formattazione
	fmt.Println("funzione pow", pow(2, 3, 10))
	result := pow(2, 10, 1000)
	fmt.Printf("result: %.4f\n", result)
}

func pow(x, n, lim float64) float64 {
	if v := math.Pow(x, n); v < lim {
		return v
	}
	return lim
}
