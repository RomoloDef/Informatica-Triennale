package SistemaFerroviaro;

public class TAV extends Treno {

	public TAV(double velocità, boolean statoPorte) {
		super(velocità, statoPorte);
		
	}
	
	@Override
	public void entraInStazione(double velocità, boolean statoPorte) {
		this.frena();
		statoPorte = true;
	}

}
