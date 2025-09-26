package DistributoreAutomatico_lab;

import java.util.Random;

public class DistributoreAutomatico {
	
	private int N;
	private double saldo;
	private Prodotto prodotti[];
	
	// Costruttore
	public DistributoreAutomatico(int N) {
		this.N = N;
		prodotti = new Prodotto[N];
	}
	
	// metodo carica
	public void carica() {
		Random r = new Random();
		
		for(int i = 0; i < N; i++) {
			int rInt = r.nextInt(3);
			switch(rInt) {
			case 0 : prodotti[i] = new BottigliaDAcqua();
				break;
			case 1: prodotti[i] = new BarraDiCioccolato();
				break;
			case 2: prodotti[i] = new GommeDaMasticare();
				break;
			default : prodotti[i] = null;
				System.out.println("SPAZIO VUOTO");	
				break;
			}
		}
	}
	
	// metodo InserisciImporto
	public void InserisciImporto(double importo) {
		saldo += importo;
	}
	
	public boolean isDisponibile(String id) {
		for(int i = 0; i<N; i++) {
			if(prodotti[i] != null && prodotti[i].getId().equals(id)) {
				return true;
			} 
		}
		return false;
	}
	
	private Prodotto rimuoviProdotto(String id, double saldo) {
		if(! isDisponibile(id)) return null; 
		
		for(int i = 0; i < N; i++) {
			if(prodotti[i] != null && prodotti[i].getId().equals(id) && saldo >= prodotti[i].getPrezzo()) {
				Prodotto pApp = prodotti[i];
				prodotti[i] = null;
				return pApp;
			}
			
		}
		
		return null;
		
	}
		
	public Prodotto getProdotto(String id) {
			Prodotto p = rimuoviProdotto(id, saldo);
			if(p != null) {
				saldo -= p.getPrezzo();
			return p;
		}
		return null;
	}
		
	public double getSaldo() {
		return saldo;
	}
	
	public double getResto() {
		double resto = saldo;
		saldo = 0;
		return resto;
	}
	
	public String toString() {
		String s = "";
		for(int i = 0; i<N; i++) {
			if(prodotti[i] == null) {
				s = s + "vuoto" + "\n";
			}
			else {
				s = s + prodotti[i].toString() + "\n";
			}
		}
		return s;
	}
	
}
