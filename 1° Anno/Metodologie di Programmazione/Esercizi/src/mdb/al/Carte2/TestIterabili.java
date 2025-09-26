package mdb.al.Carte2;

import java.util.Iterator;

public class TestIterabili {
    
	// si puo implementare quesro codice con un iterator come classe interna? Si, ecco il codice
    public static void main(String[] args) {
        MazzoDiCarte mazzo = new MazzoDiCarte();
        
        for(Carta c:mazzo) {
            System.out.println(c.toString());
        }
    }
    
    // Classe interna MazzoDiCarte
    static class MazzoDiCarte implements Iterable<Carta> {
        private Carta[] mazzo = new Carta[52];

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
        
        // Iterator
        @Override
        public Iterator<Carta> iterator() {
            return new Iterator<Carta>() {
                private int indiceCorrente = 0;

                @Override
                public boolean hasNext() {
                    return indiceCorrente < mazzo.length && mazzo[indiceCorrente] != null;
                }

                @Override
                public Carta next() {
                    return mazzo[indiceCorrente++];
                }
            };
        }

    }

    // Classe interna Carta
    static class Carta {
        enum Seme { Cuori, Quadri, Fiori, Picche }
        enum Valore { Asso, Due, Tre, Quattro, Cinque, Sei, Sette, Otto, Nove, Dieci, Jack, Donna, Re}

        private Valore valore;
        private Seme seme;

        public Carta(Valore valore, Seme seme) {
            this.valore = valore;
            this.seme = seme;
        }

		public Valore getValore() {
			return valore;
		}

		public Seme getSeme() {
			return seme;
		}
		
		@Override
		public String toString() {
		    return "Carta{" +
		            "valore=" + valore +
		            ", seme=" + seme +
		            '}';
		}

    }
}