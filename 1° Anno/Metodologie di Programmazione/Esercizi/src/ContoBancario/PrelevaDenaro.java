package ContoBancario;

public class PrelevaDenaro extends Operazione{

	public PrelevaDenaro(double denaro, double conto) {
		super(5, 100);
	}
	
	public double Preleva(double denaro, double conto) {
		conto = conto - denaro;
		return conto;
	}
}
