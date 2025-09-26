package AnimaliConInterfaccie;

public class Cane extends Animale implements salta, corre, fedeleA, domestico {

	public Cane(int numeroDiZampe, String verso) {
		super(4, "wofwof");
	}
	
	@Override
	public void salta() {
		System.out.println("Sto saltando");
	}
	@Override
	public void corre() {
		System.out.println("Sto correndo");
	}
	@Override
	public void fedeleA() {
		System.out.println("Sono fedele a Romolo");
	}
	@Override
	public void domestico() {
		System.out.println("Sono un cane domestico");
	}

	
}
