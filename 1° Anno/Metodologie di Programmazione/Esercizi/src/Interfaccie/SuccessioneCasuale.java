package Interfaccie;

import java.util.Random;

public class SuccessioneCasuale implements Successione {
	
	private Random rand = new Random();
	
	public int prossimo() {
		return rand.nextInt(100); // restituisco numeri casuali da 0 a 100
	}
}
