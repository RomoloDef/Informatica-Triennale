package AnimaliConInterfaccie;

public class Uomo extends Animale implements salta,corre,pensa,nuota {

	public Uomo(int numeroDiZampe, String verso) {
		super(4, "Ciao");
	}

	@Override
	public void nuota() {
		System.out.println("Sto nuotando");
		
	}

	@Override
	public void pensa() {
		System.out.println("Sto pensando");
		
	}

	@Override
	public void corre() {
		System.out.println("Sto correndo");
		
	}

	@Override
	public void salta() {
		System.out.println("Sto saltando");
		
	}

}
