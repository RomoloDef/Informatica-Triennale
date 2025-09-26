package DisneyVsMarvel;

public abstract class PeterParker implements DoppiaVita {
	
	private String identità;
	private int vita;
	
	public PeterParker(String identità, int vita) {
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
		this.identità = "Spiderman";
		System.out.println("Mi sono trasformato in Spiderman!");
	}
	@Override
	public void assumiIdentitaPubblica() {
		this.identità = "PeterParker";
		System.out.println("Sono un semplice fotografo al Daily Bugle");
	}
	

	public class Spiderman extends PeterParker implements Supereroe {
		
		protected int vita;
		protected int danno = 30;
		
		
		public Spiderman(String identità, int vita) {
			super(identità, vita);
		}
		
		@Override
		public int attacca() {
			int danno = 30; 
	        System.out.println("Spiderman attacca, infliggendo " + danno + " punti di danno!");
	        return danno;
		}
		
		public void riceviDanno(int danno) {
			this.danno = danno;
	        this.vita -= danno;
	        System.out.println("Ho ricevuto " + danno + " punti di danno! La mia vita è ora " + this.vita);
	    }
		
	}
}