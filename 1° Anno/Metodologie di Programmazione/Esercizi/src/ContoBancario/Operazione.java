package ContoBancario;

public abstract class Operazione {
	
	private double denaro;
	private double conto;
	
	// Costruttore
	public Operazione(double denaro, double conto) {
		this.denaro = denaro;
		this.conto = conto;
	}
	
	// Getters
	public double getDenaro() {
		return denaro;
	}
	
	public double getConto() {
		return conto;
	}
	

}
