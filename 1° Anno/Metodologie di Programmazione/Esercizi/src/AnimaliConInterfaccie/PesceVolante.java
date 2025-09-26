package AnimaliConInterfaccie;

public class PesceVolante extends Pesce implements vola{

	public PesceVolante(String verso) {
		super("ququauauau");
	}
	
	@Override
	public void vola() {
		System.out.println("Sto volando");
	}
}
