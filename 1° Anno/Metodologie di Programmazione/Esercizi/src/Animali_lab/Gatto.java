package Animali_lab;

public class Gatto extends Felino {
	
	public Gatto() {
		super("Miao Miao", Taglia.PICCOLA);
	}
	
	@Override
	public void graffia() {
		System.out.println("Graffia come un gatto");
	}	

}
