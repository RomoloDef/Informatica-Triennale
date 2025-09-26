package Animali_lab;

public abstract class Animale {
	
	protected String verso;
	protected int numeroZampe;
	protected Taglia taglia;
	
	// Costruttore
	public Animale(String verso, int numeroZampe, Taglia taglia) {
		this.verso = verso;
		this.numeroZampe = numeroZampe;
		this.taglia = taglia;
	}
	
	public void emettiVerso() {
		System.out.println(verso);
	}
	
	public int getNumeroZampe() {
		return numeroZampe;
	}
	
	public String getVerso() {
		return verso;
	}
	
	public Taglia getTaglia() {
		return taglia;
	}
	
}
