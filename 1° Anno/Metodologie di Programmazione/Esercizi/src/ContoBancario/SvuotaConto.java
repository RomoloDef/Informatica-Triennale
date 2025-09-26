package ContoBancario;

public class SvuotaConto extends Operazione {

	public SvuotaConto(double denaro, double conto) {
		super(5, 100);
	}
	
	public double Svuota(double conto) {
		conto = 0;
		return conto;
	}

}
