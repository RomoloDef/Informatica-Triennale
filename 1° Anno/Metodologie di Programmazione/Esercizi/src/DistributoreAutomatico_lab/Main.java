package DistributoreAutomatico_lab;

public class Main {
	public static void main(String[] args) {
		DistributoreAutomatico d = new DistributoreAutomatico(7);
		
		d.carica();
		d.InserisciImporto(5);
		
		System.out.println(d.toString());
		
		d.getProdotto("003");
		
		System.out.println(d.toString());
		
	}
}
