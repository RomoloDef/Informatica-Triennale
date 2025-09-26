package Lotto;

import java.util.Random;

public class EstrazioneLotto {
	
	private int[] numeriEstratti = new int[5];
	private String estrazioni = ""; // storico delle estrazioni
	
	// metodo estrai
	public void estrai() {
		Random r = new Random();
		for(int i = 0; i < numeriEstratti.length; i++) {
			int numero = r.nextInt(91);
			numeriEstratti[i] = numero;
			estrazioni = estrazioni + numero + " ";
		}
	}
		
	// metodo getter - getEstrazioni
	public String getEstrazioni() {
		return estrazioni;
	}
	
	// metodo toString
	public String toString() {
		String s = "";
		for(int i = 0; i< numeriEstratti.length; i++) {
			s = s + numeriEstratti[i] + ", ";
		}
		return s;
	}
	
	// metodo numeriContenuti
	public int numeriContenuti(int[] giocata) {
		if(giocata.length > 10) {
			System.out.println("Hai inserito troppi numeri!");
			return -1;
		} else {
			int num = 0;
			for(int i = 0; i < giocata.length; i++) {
				for(int j = 0; j<numeriEstratti.length;j++) {
					if(giocata[i]==numeriEstratti[j]) num++;
				}
			}
			
			return num;
		}
	}
	
	// metodo vincita
	public boolean vincita(int[] giocata) {
		return (numeriContenuti(giocata)>=2)?true:false;
	}
	
	// metodo sommaValoriEstratti
	public int sommaValoriEstratti() {
		int tot = 0;
		String[] valori = estrazioni.split(" ");
		for(int i = 0; i < valori.length; i++) {
			tot += Integer.parseInt(valori[i]);
		}
		return tot;
	}
}
