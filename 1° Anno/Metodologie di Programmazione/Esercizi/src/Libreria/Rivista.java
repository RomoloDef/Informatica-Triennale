package Libreria;

public class Rivista implements Pubblicazione {
	
	private String titolo;
	private String editore;
	private int numero;
	
	public Rivista(String titolo, String editore, int numero) {
		this.titolo = titolo;
		this.editore = editore;
		this.numero = numero;
	}
	
	public String getTitolo() {
		return titolo;
	}
	
	public String getEditore() {
		return editore;
	}
	
	public int getNumero() {
		return numero;
	}
	
	@Override
	public double calcolaPrezzo() {
		return numero * 7;
	}

}
