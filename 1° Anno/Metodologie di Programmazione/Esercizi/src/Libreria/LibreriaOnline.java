package Libreria;

import java.util.ArrayList;

public class LibreriaOnline {
	
	private ArrayList<Pubblicazione> collezione = new ArrayList<>();
	
	public LibreriaOnline(ArrayList<Pubblicazione> collezione) {
		this.collezione = collezione;
	}
	
	public void aggiungiPubblicazione(Pubblicazione pubblicazione) {
		collezione.add(pubblicazione);
	}
	
	public double calcolaPrezzoTotale() {
		int somma = 0;
		for(Pubblicazione pubblicazione: collezione) {
			somma += pubblicazione.calcolaPrezzo();
		}
		
		return somma;
	}
	
	public String toString() {
		String libreria = " ";
		for (Pubblicazione pubblicazione: collezione) {
			if (pubblicazione instanceof Libro) {
				Libro libro = (Libro) pubblicazione;
				libreria += libro.getTitolo() + "," + libro.getAutore() + " :" + libro.getPrezzo() + "\n";
			} else {
				if (pubblicazione instanceof Rivista) {
					Rivista rivista = (Rivista) pubblicazione;
					libreria += rivista.getTitolo() + "," + rivista.getEditore() + " :" + rivista.getNumero() + "\n";
				}
			}
		}
		
		return libreria;
		
	}

}
