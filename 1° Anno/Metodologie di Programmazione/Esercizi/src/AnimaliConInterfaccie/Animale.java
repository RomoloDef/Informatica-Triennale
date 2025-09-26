package AnimaliConInterfaccie;

public abstract class Animale implements mangia{
	
	private int numeroDiZampe;
	private String verso;
	
	public Animale(int numeroDiZampe, String verso) {
		this.numeroDiZampe = numeroDiZampe;
		this.verso = verso;
	}
	
	public int getNumeroDiZampe() {
		return numeroDiZampe;
	}
	
	public String verso() {
		return verso;
	}
	
	@Override
	public void mangia() {
		System.out.println("GNAMGNAMGNAM");
	}
}
