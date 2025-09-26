package Esercizi;

public class Negate {
	
	private int a;
	
	public Negate(int a) {
		this.setA(a);
	}
	
	public static int negate(int a) {
		a = -1*a;
		return a;
	}
	
	public static void main(String[] args) {
		int a = 17;
		System.out.println(a);
		int temp = negate(a);
		System.out.println(temp);
	}

	public int getA() {
		return a;
	}

	public void setA(int a) {
		this.a = a;
	}
}
