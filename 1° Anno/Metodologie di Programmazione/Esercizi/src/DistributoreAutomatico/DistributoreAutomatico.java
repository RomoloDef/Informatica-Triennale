package DistributoreAutomatico;

// Importo librerie che mi saranno utili
import java.util.Random;
import java.util.Scanner;

public class DistributoreAutomatico {
	
	private Prodotto[] prodotti;
	private int saldo;
	
	// Costruttore
	public DistributoreAutomatico(int N) {
		prodotti = new Prodotto[N];
		carica(); // carico il distributore coi prodotti inseriti
	}
	
	// Metodo Carica
	public void carica() {
        Random random = new Random();
        for (int i = 0; i < prodotti.length; i++) {
            int tipoProdotto = random.nextInt(3);
            switch (tipoProdotto) {
                case 0:
                    prodotti[i] = new Prodotto.BottigliaDacqua(random.nextDouble() * 10);
                    break;
                case 1:
                    prodotti[i] = new Prodotto.BarraDiCioccolato(random.nextDouble() * 10);
                    break;
                case 2:
                    prodotti[i] = new Prodotto.GommeDaMasticare(random.nextDouble() * 10);
                    break;
            }
        }
    }
	
	// Metodo inserisciImporto
	public void inserisciImporto(int importo) {
		saldo += importo;
	}
	
	// Metodo getProdotto
	public Prodotto getProdotto() {
		@SuppressWarnings("resource")
		Scanner scanner = new Scanner(System.in);
		System.out.println("Inserisci il tuo prodotto");
		int prodotto = scanner.nextInt();
		switch (prodotto) {
		case 0:
			saldo -= 1;
			return new Prodotto.BottigliaDacqua(1);
		case 1:
			saldo -= 2;
            return new Prodotto.BarraDiCioccolato(2); 
        case 2:
        	saldo -= 0.5;
            return new Prodotto.GommeDaMasticare(0.5); 
        default:
            System.out.println("Codice prodotto non valido");
            return null;
    }
		
	}
	
	// Metodo getSaldo
	public double getSaldo() {
		return saldo;
	}
	
	// Metodo getResto
	public double getResto() {
		double resto = saldo;
        saldo = 0;
        return resto;
	}
}
		
	
