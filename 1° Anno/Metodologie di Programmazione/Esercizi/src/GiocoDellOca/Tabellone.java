package GiocoDellOca;

import java.util.Random;

public class Tabellone {
	
	protected Casella[] tabellone;
	public final int nCaselle;
	
	public Tabellone(int nCaselle) {
		this.nCaselle = nCaselle;
		
		tabellone = new Casella[nCaselle];
		
		tabellone[0] = new CasellaVuota();
		tabellone[nCaselle-1] = new CasellaVuota();
		
		Random r = new Random();
		for(int i = 1; i<nCaselle-1; i++) {
			int rInt = r.nextInt(6);
			
			if(rInt<=3) {
				tabellone[i] = new CasellaVuota();
			} else if(rInt==4) {
				tabellone[i] = new CasellaPunti((r.nextInt(9)+1)*segnoRandom());
			} else if(rInt==5) {
				tabellone[i] = new CasellaSposta((r.nextInt(9)+1)*segnoRandom());
			}
		}
		
	}
	
	public int segnoRandom() {
		Random r = new Random();
		int rInt = r.nextInt(2);
		return (rInt==0)?1:-1;
	}
	
}
	

