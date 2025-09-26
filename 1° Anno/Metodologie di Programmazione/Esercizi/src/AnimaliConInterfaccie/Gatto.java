package AnimaliConInterfaccie;

public class Gatto extends Felino implements domestico {

	public Gatto(int numeroDiZampe, String verso) {
		super(4, "miao miao");
	}
	
	@Override
	public void domestico() {
		System.out.println("Sono un animale domestico"); 
	}

}
