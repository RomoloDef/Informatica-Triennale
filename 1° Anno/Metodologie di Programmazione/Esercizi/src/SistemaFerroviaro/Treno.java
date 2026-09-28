package SistemaFerroviaro;

public class Treno {
	
	private double velocità;
	private boolean statoPorte;
	
	public Treno(double velocità, boolean statoPorte) {
		this.velocità = velocità;
		this.statoPorte = statoPorte; // se true le porte sono aperte, sennò sono chiuse
	}
	
	public double getVelocità() {
		return velocità;
	}
	
	public boolean getStatoPorte() {
		return statoPorte;
	}

	// metodo frena
	public void frena() {
		this.velocità = 0;
	}
	
	// metodo entraInStazione
	public void entraInStazione(double velocità, boolean statoPorte) {
		this.frena();
	}
	
	// metodo setPorte
	public void setStatoPorte(boolean stato) {
		this.statoPorte = stato;
	}

	
}
