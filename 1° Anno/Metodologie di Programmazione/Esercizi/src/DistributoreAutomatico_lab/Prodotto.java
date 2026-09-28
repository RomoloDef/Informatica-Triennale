package DistributoreAutomatico_lab;

public abstract class Prodotto {
	
	private double prezzo;
	private String id;
	
	// Costruttore 
	public Prodotto(double prezzo, String id) {
		this.prezzo = prezzo;
		this.id = id;
	}
	
	// Getter
	public double getPrezzo() {
		return prezzo;
	}
	
	public String getId() {
		return id;
	}
	
	// Voglio che il toString ritorni: BottigliaDAcqua 001
	@Override
	public String toString() {
		return this.getClass().getSimpleName() + " " + getId(); 
	}
	
}
