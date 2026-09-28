package Animali_lab;

public abstract class Felino extends Mammifero {

	public Felino(String verso, Taglia taglia) {
		super(verso, 4, taglia); // 4 zampe per i felini
	}
	
	public void graffia() {
		System.out.println("Graffia come un felino");
	}

}
