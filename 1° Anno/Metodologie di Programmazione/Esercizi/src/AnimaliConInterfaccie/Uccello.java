package AnimaliConInterfaccie;

public abstract class Uccello extends Animale implements vola,becca {

	public Uccello(String verso) {
		super(2, verso);
	}
	
	@Override
	public void vola() {
		System.out.println("Sto volando");
	}
	
	@Override
	public void becca() {
		System.out.println("Sto beccando");
	}
}
