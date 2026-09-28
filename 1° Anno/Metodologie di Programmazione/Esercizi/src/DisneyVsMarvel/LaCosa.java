package DisneyVsMarvel;

public class LaCosa implements Supereroe {

	private int vita = 100;
	protected int danno = 50;
	
	public void riceviDanno(int danno) {
		this.danno = danno;
        this.vita -= danno;
        System.out.println("Ho ricevuto " + danno + " punti di danno! La mia vita è ora " + this.vita);
    }
	
	@Override
	public int attacca() {
		int danno = 50; 
        System.out.println("La cosa attacca, infliggendo " + danno + " punti di danno!");
        return danno;
	}

}
