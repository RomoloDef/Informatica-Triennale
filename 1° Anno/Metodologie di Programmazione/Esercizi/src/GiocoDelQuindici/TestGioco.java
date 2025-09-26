package GiocoDelQuindici;

public class TestGioco {
	public static void main(String[] args) {
		// testiamo se il gioco del quindici funziona
		GiocoDelQuindici gioco = new GiocoDelQuindici();
		gioco.mischia();
		gioco.scorri(1, 3, GiocoDelQuindici.Direzione.su);
		Boolean x = gioco.vinto();
		System.out.println(x);
	}
}
