package SistemaFerroviaro;

public class BinarioStazione extends Binario {

	public BinarioStazione(int binarioSuccessivo) {
		super(binarioSuccessivo);
		
	}
	
	@Override 
	public int percorri(Treno treno) {
		treno.entraInStazione(0, false);
		return binarioSuccessivo;
	}
	
}
