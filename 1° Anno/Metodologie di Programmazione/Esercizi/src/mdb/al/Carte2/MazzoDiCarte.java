package mdb.al.Carte2;

import java.util.Random;

public class MazzoDiCarte {
    private Carta[] mazzo = new Carta[52]; // Array di 52 carte
    private int cursore;
    
    // Costruttore 
    public MazzoDiCarte() {
        Carta.Seme[] semi = Carta.Seme.values();
        Carta.Valore[] valori = Carta.Valore.values();
        int indice = 0;
        for (Carta.Seme seme : semi) { // iterare sui semi
            for (Carta.Valore valore : valori) { // iterare sui valori
                mazzo[indice] = new Carta(valore, seme);
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