package main

import "fmt"

func main() {

	// PUNTATORI
	fmt.Println("Parliamo di puntatori in Go:")
	var p *int                     // dichiaro una variabile p che è un puntatore a un intero
	fmt.Println("Valore di p:", p) // stampa il valore di p (all'inizio sarà nil se non è inizializzato)
	i := 42
	p = &i                                    // p punta all'indirizzo di memoria di i
	fmt.Println("Indirizzo di i:", p)         // stampa l'indirizzo di memoria di i
	fmt.Println("Valore di i tramite p:", *p) // dereferenziazione: ottengo il valore di i tramite p
	*p = 21                                   // imposto il valore della variabile i tramite il puntatore p
	fmt.Println("Nuovo valore di i:", i)      // stampa il nuovo valore di i

	// STRUTTURE
	fmt.Println("\nParliamo di strutture in Go:")
	fmt.Println("Sarebbe una struttura di campi")
	fmt.Println("L'accesso avviene tramite il punto")
	fmt.Println("L'accesso tramite puntatore (*p).campo può essere abbreviato in p.campo")

	type Persona struct {
		Nome string
		Età  int
	}

	var (
		p1 = Persona{"Mario", 30}   // inizializzazione diretta con i valori
		p2 = Persona{Nome: "Luigi"} // inizializzazione solamente con il valore iniziale, il secondo verrà settato a 0
		p3 = Persona{}              // inizializzazione vuota, tutti i campi a zero valori
		p4 = &Persona{"Anna", 25}   // puntatore a una struttura Persona
	)

	// Stampo le persone
	fmt.Println("Persona 1:", p1)
	fmt.Println("Persona 2:", p2)
	fmt.Println("Persona 3:", p3)
	fmt.Println("Persona 4:", *p4) // dereferenzio il puntatore per stampare la struttura

	// ARRAY
	fmt.Println("\nParliamo di array in Go:")
	fmt.Println("Esempio di dichiarazione di array in Go: var a [5]int")
	var a [5]int
	fmt.Println("Valore iniziale di a:", a)

	fmt.Println("Esempio di inizializzazione di array in Go: a := [5]int{1, 2, 3, 4, 5}")
	a = [5]int{1, 2, 3, 4, 5}
	fmt.Println("Valore di a dopo l'inizializzazione:", a)
	// La dimensione di un array è parte del suo tipo ed è fissa

	// SLICE
	// La modifica degli elementi di una slice modifica l'array sottostante e qualsiasi slice corrispondente che punta allo stesso array
	fmt.Println("\nParliamo di slice in Go:")
	s := []int{2, 4, 6, 19, 42} // slice di interi
	fmt.Println("lunghezza:", len(s))
	fmt.Println("capacità:", cap(s))

	// Affettiamo la slice
	s = s[1:4] // slice dall'indice 1 (incluso) all'indice 4 (escluso)
	fmt.Println("Slice dopo l'affettamento s[1:4]:", s)
	fmt.Println("lunghezza dopo l'affettamento:", len(s))
	fmt.Println("capacità dopo l'affettamento:", cap(s))

	// Si può indicizzare oltre la len se si effettua un re-slicing
	fmt.Println("Re-slicing per estendere la slice fino alla capacità")
	fmt.Println(s[:cap(s)][3])

}
