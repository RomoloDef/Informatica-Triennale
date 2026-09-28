package Lotto;

public class Main {
	
	public static void main(String[] args) {
		EstrazioneLotto e = new EstrazioneLotto();
		e.estrai();
		System.out.println(e.toString());
		
		e.estrai();
		System.out.println(e.toString());
		
		System.out.println(e.getEstrazioni());
		
		System.out.println(e.sommaValoriEstratti());
		
	}
}
