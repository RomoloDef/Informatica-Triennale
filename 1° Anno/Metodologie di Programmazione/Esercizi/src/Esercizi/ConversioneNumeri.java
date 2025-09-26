package Esercizi;

public class ConversioneNumeri {
	
	private int numero;
	
	// Costruttore
	public ConversioneNumeri(int numero) {
		this.numero = numero;
	}
	
	// metodo conversione
	public String conversione() {
		String numeroStringa = String.valueOf(this.numero);
		return numeroStringa;
	}
	
	// metodo main
	public static void main(String[] args) {
		 ConversioneNumeri numeroConvertito = new ConversioneNumeri(123);
	     String numeroStringa = numeroConvertito.conversione();
	     System.out.println(numeroStringa);	
	}
	
}
