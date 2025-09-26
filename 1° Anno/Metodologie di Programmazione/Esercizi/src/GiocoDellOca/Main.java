package GiocoDellOca;

public class Main {
	
	public static void main(String[] args) {
		
		Giocatore g1 = new Giocatore("Mario");
		Giocatore g2 = new Giocatore("Luigi");
		
		Giocatore[] giocatori = {g1,g2};
		
		GiocoOca go = new GiocoOca(25,giocatori);
		
		go.giocaTurno();
		
		System.out.println(go.getGiocatori()[0].getPosizione());
		System.out.println(go.getGiocatori()[1].getPosizione());
		

		go.giocaTurno();
		
		System.out.println(go.getGiocatori()[0].getPosizione());
		System.out.println(go.getGiocatori()[1].getPosizione());

		
	}


}