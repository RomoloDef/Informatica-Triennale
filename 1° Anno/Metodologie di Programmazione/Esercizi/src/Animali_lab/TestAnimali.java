package Animali_lab;

public class TestAnimali {

	public static void main(String[] args) {
		
		Gatto goku = new Gatto();
		goku.emettiVerso();
		goku.graffia();
		
		Animale vegeta = new Gatto();	// dichiarare animale non fa accedere ai metodi delle sottoclassi (nello specifico graffia di Felino/Gatto)
		vegeta.emettiVerso();
		//((Felino) vegeta).graffia();

	}
	
}
