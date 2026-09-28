package DistributoreAutomatico_lab;

public class BarraDiCioccolato extends Prodotto {
	
	private static int kBarre;
	
	public BarraDiCioccolato() {
		super(1.5,"002");
		kBarre++;
		if(kBarre == 3) {
			System.out.println("GOLDEN TICKET!");
			
		}
	}
	
	
}
