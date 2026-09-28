package Libreria;

public class Libro implements Pubblicazione {
	
	private String titolo;
	private String autore;
	private double prezzo;
	
	public Libro(String titolo, String autore, double prezzo) {
		this.titolo = titolo;
		this.autore = autore;
		this.prezzo = prezzo;
	}
	
	public String getTitolo() {
		return titolo;
	}
	
	public String getAutore() {
		return autore;
	}
	
	public double getPrezzo() {
		return prezzo;
	}

	@Override
	public double calcolaPrezzo() {
		return prezzo * 3;
	}
	
	

}
