package AnimaliConInterfaccie;

public abstract class Felino extends Animale implements salta, corre, faLeFusa {

	public Felino(int numeroDiZampe, String verso) {
		super(4, verso);
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
	public void faLeFusa() {
		System.out.println("gregrerger");
	}
	
	

}
