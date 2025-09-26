package DisneyVsMarvel;

public abstract class Paperino implements DoppiaVita {
	
	private String identità;
	protected int vita;
	
	public Paperino(String identità, int vita) {
		this.identità = identità;
		this.vita = vita;
	}
	
	public String getIdentità() {
		return identità;
	}
	
	public int getVita() {
		return vita;
	}
	
	@Override
	public void assumiIdentitàSegreta() {
		this.identità = "Paperinik";
		System.out.println("Mi sono trasformato in Paperinik!");
	}
	@Override
	public void assumiIdentitaPubblica() {
		this.identità = "Paperino";
		System.out.println("Sono tornato Paperino");
	}
	

	public class Paperinik extends Paperino implements Supereroe {
		
		protected int vita;
		protected int danno = 10;
		
		public Paperinik(String identità, int vita) {
			super("Paperinik", 100);
		}

		@Override
		public int attacca() {
			int danno = 10; 
	        System.out.println("Paperinik attacca, infliggendo " + danno + " punti di danno!");
	        return danno;
		}
		
		public void riceviDanno(int danno) {
			this.danno = danno;
	        this.vita -= danno;
	        System.out.println("Ho ricevuto " + danno + " punti di danno! La mia vita è ora " + this.vita);
	    }
	}
}
