package DistributoreAutomatico;

public abstract class Prodotto {
	
	protected double prezzo;
	
	// Costruttore
	public Prodotto(double prezzo) {
		this.prezzo = prezzo;	
	}
	
	// Getter
	public double getPrezzo() {
		return prezzo;
	}
	
	// Devo fare le sottoclassi statiche per richiamarle in un altra classe
	public static class BottigliaDacqua extends Prodotto {
		public BottigliaDacqua(double prezzo) {
			super(prezzo);
		}
	}
	
	public static class BarraDiCioccolato extends Prodotto { 
		public BarraDiCioccolato(double prezzo) {
			super(prezzo);
		}
	}
	
	public static class GommeDaMasticare extends Prodotto {
		public GommeDaMasticare(double prezzo) {
			super(prezzo);
		}
	}
}
