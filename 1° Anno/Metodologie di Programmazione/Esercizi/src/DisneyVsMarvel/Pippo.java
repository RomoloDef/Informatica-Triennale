package DisneyVsMarvel;

public abstract class Pippo implements DoppiaVita {
	
	private String identità;
	protected int vita;
	
	public Pippo(String identità, int vita) {
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
		this.identità = "Superpippo";
		System.out.println("Mi sono trasformato in Superpippo!");
	}
	@Override
	public void assumiIdentitaPubblica() {
		this.identità = "Pippo";
		System.out.println("Sono tornato Pippo");
	}
	

	public class Superpippo extends Pippo implements Supereroe {
		
		protected int vita;
		protected int danno = 15;
		
		public Superpippo(String identità, int vita) {
			super("Superpippo", 100);
		}

		@Override
		public int attacca() {
			int danno = 40; 
	        System.out.println("Superpippo attacca, infliggendo " + danno + " punti di danno!");
	        return danno;
		}
		
		public void riceviDanno(int danno) {
			this.danno = danno;
	        this.vita -= danno;
	        System.out.println("Ho ricevuto " + danno + " punti di danno! La mia vita è ora " + this.vita);
	    }
		
	}
}
	
