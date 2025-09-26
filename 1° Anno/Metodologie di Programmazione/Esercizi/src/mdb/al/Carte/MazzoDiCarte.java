package mdb.al.Carte;

import java.util.Random;

public class MazzoDiCarte {
	private Carta[] mazzo = new Carta[52]; // Array di 52 carte
	private int cursore;
	
	// Costruttore 
	public MazzoDiCarte() {
		String[] semi = {"fiori" , "quadri" , "cuori" , "picche"};
		String[] valori = { "Asso" , "2" , "3" , "4", "5" , "6" , "7" , "8" , "9" , "10" , "Jack" , "Donna" , "Re" };
		int indice = 0;
		for (String seme : semi) { // iterare sui semi
            for (String valore : valori) { // iterare sui valori
                mazzo[indice] = new Carta(seme, valore);
                indice++;
            }
        }
		
	}
	
	// Metodo mescola
	public void mescola() {
		Random casuale = new Random();
        for (int i = 0; i < mazzo.length; i++) {
            int j = casuale.nextInt(mazzo.length);
            Carta temporanea = mazzo[i];
            mazzo[i] = mazzo[j];
            mazzo[j] = temporanea;
        }
        cursore = 0;
	}
	
	// Metodo distribuisci
	public Carta distribuisci() {
		if (cursore < mazzo.length) {
            return mazzo[cursore++];
        } else {
            return null; 
        }
	}
	
	// Metodo main
	public static void main(String[] args) {
        MazzoDiCarte mazzo = new MazzoDiCarte();
        mazzo.mescola();
        Carta carta;
        while ((carta = mazzo.distribuisci()) != null) {
            System.out.println(carta);
        }
    }
}
