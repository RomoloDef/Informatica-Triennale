package DisneyVsMarvel;

public class Magneto implements Supereroe {
	
	private int vita = 100;
	protected int danno = 35;
	
	public void riceviDanno(int danno) {
		this.danno = danno;
        this.vita -= danno;
        System.out.println("Ho ricevuto " + danno + " punti di danno! La mia vita è ora " + this.vita);
    }
	
	@Override
	public int attacca() {
		int danno = 35; 
        System.out.println("Magneto attacca, infliggendo " + danno + " punti di danno!");
        return danno;
	}
	

}
