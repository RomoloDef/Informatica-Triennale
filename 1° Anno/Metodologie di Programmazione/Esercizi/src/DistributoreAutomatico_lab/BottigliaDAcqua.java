package DistributoreAutomatico_lab;

public class BottigliaDAcqua extends Prodotto {
	
	public BottigliaDAcqua() {
		// super(1, "001"); // prezzo e ID
		this(1);
	}
	
	// Overload del costruttore
	public BottigliaDAcqua(double prezzo) {
		super(prezzo, "001");
	}
}
