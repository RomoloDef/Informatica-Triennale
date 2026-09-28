package Libreria;

import java.util.ArrayList;

public class Test {
	
	public static void main(String[] args) {
		Libro libro = new Libro("Nonloso", "io", 5);
		Rivista rivista = new Rivista("Boh", "tu", 7);
		ArrayList<Pubblicazione> pubblicazioni = new ArrayList<>();
		LibreriaOnline libreria = new LibreriaOnline(pubblicazioni);
		libreria.aggiungiPubblicazione(libro);
		libreria.aggiungiPubblicazione(rivista);
		System.out.println(libreria.toString());
	}

}
