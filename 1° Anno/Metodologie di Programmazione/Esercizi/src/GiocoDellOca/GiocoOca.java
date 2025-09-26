package GiocoDellOca;

public class GiocoOca extends Tabellone{
	
	private Giocatore[] giocatori;
	
	public GiocoOca(int nCaselle, Giocatore ... giocatori) {
		super(nCaselle);
		this.giocatori = giocatori; 
	}
	
	//questo sarebbe il metodo che implementa il caso
	//UltimaCasella
	public boolean posizionaGiocatore(Giocatore g, int lancio) {
		//setto la posizione del giocatore
		g.setPosizione(lancio);
		
		if(g.getPosizione()==nCaselle-1) {
			System.out.println("VITTORIA!");
			return true;
		}
		
		if(g.getPosizione()>tabellone.length-1) {
			int eccedenza = g.getPosizione() - (tabellone.length-1);
			return posizionaGiocatore(g, -eccedenza);
		}
		
		//ora devo capire in che tipo di casella sono
		//per decidere cosa fare
		if(tabellone[g.getPosizione()] instanceof CasellaPunti) {
			g.setPunti(((CasellaPunti) tabellone[g.getPosizione()]).getPunti());
			return false;
		}
		if(tabellone[g.getPosizione()] instanceof CasellaSposta) {
			//sposterai il giocatore dello spostamento della casella
			return posizionaGiocatore(g,
				((CasellaSposta) tabellone[g.getPosizione()]).getSpostamento());
		}
		//sono in una cella vuota diversa dall'ultima
		return false;
	}
	
	public void giocaTurno() {
		for(int i=0;i<giocatori.length;i++) {
			if(posizionaGiocatore(giocatori[i],giocatori[i].tiraDadi())) break;
		}
	}
	
	public Giocatore[] getGiocatori() {
		return(giocatori);
	}

}

