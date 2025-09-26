package mdb.al.Carte;

public class Carta {
	private String seme;
	private String valore;
	
	// Costruttore
	public Carta(String seme, String valore) {
		this.seme = seme;
		this.valore = valore;
	}
	
	// Metodo getSeme
	public String getSeme() {  // Getter
		return this.seme;
	}
	
	// Metodo getValore
	public String getValore() {  // Getter
		return this.valore;
	}
	
	// Metodo toString
	public String toString() {
	    return this.valore + " di " + this.seme;
	}
}
