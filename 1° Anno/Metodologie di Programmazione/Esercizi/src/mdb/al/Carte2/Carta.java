package mdb.al.Carte2;

public class Carta {
    
    public enum Seme{
        Cuori(1), Quadri(2), Fiori(3), Picche(4);
        private int seme;
        
        Seme(int seme){
            this.seme = seme;
        }
        public int toInt() {
            return seme;
        }
    }
        
    public enum Valore{
        Asso(1), Due(2), Tre(3), Quattro(4), Cinque(5), Sei(6), Sette(7), Otto(8), Nove(9), Dieci(10), Jack(11), Donna(12), Re(13);
        private int valore;
        
        Valore(int valore){
            this.valore = valore;
        }

        public String toString() {
            return String.valueOf(valore);
        }
    }

    private Valore valore;
    private Seme seme;

    public Carta(Valore valore, Seme seme) {
        this.valore = valore;
        this.seme = seme;
    }
    
    public String toString(){
        return this.valore + " di " + this.seme;
    }
}