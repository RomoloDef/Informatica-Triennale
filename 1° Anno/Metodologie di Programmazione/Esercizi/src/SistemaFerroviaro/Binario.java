package SistemaFerroviaro;

public abstract class Binario {
	
	protected int binarioSuccessivo;
	
	public Binario(int binarioSuccessivo) {
		this.binarioSuccessivo = binarioSuccessivo;
	}

	public int getBinarioSuccessivo() {
		return binarioSuccessivo;
	}
	
	public int percorri(Treno treno) {
		return binarioSuccessivo;
	}
	
}
