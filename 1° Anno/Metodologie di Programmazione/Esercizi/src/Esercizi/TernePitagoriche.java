package Esercizi;

public class TernePitagoriche {
	
	public static void main(String[] args) {
		double a = 3;
		double b = 4;
		double C =  Math.sqrt(Math.pow(a,2)+ Math.pow(b,2));
		double c = Math.pow(C, 2);
		System.out.println(c);
		if(Math.pow(C, 2) == Math.pow(a,2)+ Math.pow(b,2)) {
			System.out.println("è una terna pitagorica");
		}
		
	}
	
}
