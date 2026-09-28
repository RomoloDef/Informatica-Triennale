package AnimaliConInterfaccie;

public class Pinguino extends Uccello implements nuota {

	
	
	public Pinguino(int numeroDiZampe, String verso) {
		super("grgrgrgr");
	}

	@Override
	public void vola() {

	}

	@Override
	public void nuota() {
		System.out.println("FSHHFSHHHFSHHHHH");
	}

}

