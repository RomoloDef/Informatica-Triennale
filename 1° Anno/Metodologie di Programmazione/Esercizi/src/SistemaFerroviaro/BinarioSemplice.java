package SistemaFerroviaro;

public class BinarioSemplice extends Binario {

	public BinarioSemplice(int binarioSuccessivo) {
		super(binarioSuccessivo);
	}
	
	@Override
	public int percorri(Treno treno) {
		return binarioSuccessivo;
	}
	
}
