// Progettare una classe Rettangolo i cui oggetti rappresentano un rettangolo e sono costruiti a partire dalle coordinate x, y e dalla lunghezza e altezza del rattngolo
// La classe implementa i seguenti metodi:
// trasla che, dati in input due valori x e y, trasla le coordinate del rattngolo dei valori orizzontali e verticali corrispondenti
// toString che restituisce una stringa del tipo "(x1, y1)->(x2,y2)" con i punti degli angoli in alto a sinistra e in basso a destra del rettangolo"

public class Rettangolo {

    private int x;
    private int y;
    private int lunghezza;
    private int altezza;

    // Costruttore
    public Rettangolo(int x, int y, int lunghezza, int altezza) {
        this.x = x;
        this.y = y;
        this.lunghezza = lunghezza;
        this.altezza = altezza;
    }

    // Metodo trasla
    public void trasla(int dx, int dy){
        this.x += dx;
        this.y += dy;
    }

    // Metodo toString
    public String toString(){
        return "(" + this.x + "," + this.y + ")->(" + (this.x + this.lunghezza) + "," + (this.y + this.altezza) + ")";
    }

    // Metodo main
    public static void main(String[] args) {
        Rettangolo r = new Rettangolo(1, 1, 2, 3);
        System.out.println(r.toString());
        r.trasla(1, 1);
        System.out.println(r.toString());
    }

}


