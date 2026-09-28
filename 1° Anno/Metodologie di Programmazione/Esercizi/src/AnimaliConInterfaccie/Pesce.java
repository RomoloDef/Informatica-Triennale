package AnimaliConInterfaccie;

public abstract class Pesce extends Animale implements nuota{

	public Pesce(String verso) {
		super(0, verso);
	}
	
	@Override
	public void nuota() {
		System.out.println("FSHSFHSFHSFHS");
	}
	
}
