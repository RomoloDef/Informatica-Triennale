package SistemaFerroviaro;

public class BinarioScambio extends Binario {

	public BinarioScambio(int binarioSuccessivo) {
		super(binarioSuccessivo);
	}
	
	public int scambia(int binarioScambiato) {
			binarioScambiato = binarioSuccessivo;
			return binarioScambiato;
	}
	
	@Override
	public int percorri(Treno treno) {
		return binarioSuccessivo;
	}

}
