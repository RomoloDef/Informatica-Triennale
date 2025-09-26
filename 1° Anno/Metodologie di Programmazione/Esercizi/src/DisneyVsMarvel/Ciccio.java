package DisneyVsMarvel;

public abstract class Ciccio implements DoppiaVita {
	
	private String identità;
	protected int vita;
	
	public Ciccio(String identità, int vita) {
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
		this.identità = "Ciccionik";
		System.out.println("Mi sono trasformato in Ciccionik!");
	}
	@Override
	public void assumiIdentitaPubblica() {
		this.identità = "Ciccio";
		System.out.println("Sono tornato Ciccio");
	}
	

	public class Ciccionik extends Ciccio implements Supereroe {
		
		protected int vita;
		protected int danno = 12;
		
		public Ciccionik(String identità, int vita) {
			super("Ciccionik", 100);
		}
		
		@Override
		public int attacca() {
			int danno = 12; 
	        System.out.println("Ciccionik attacca, infliggendo " + danno + " punti di danno!");
	        return danno;
		}
		
		public void riceviDanno(int danno) {
			this.danno = danno;
	        this.vita -= danno;
	        System.out.println("Ho ricevuto " + danno + " punti di danno! La mia vita è ora " + this.vita);
	    }
		
	}
}