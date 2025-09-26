// Progettare una classe Colore i cui oggetti rappresentano un colore in modalità RGB e che sono costruiti a partire da tre valori: R(rosso), G(verde), B(blu), ognuno dei quali ammette un valore intero nell'intervallo 0-255.
// La classe Colore espone anche due costanti BIANCO e NERO
// fare in modo che ogni rettangolo (vedi esercizio precedente) abbia associato un Colore di base Nero e che sia possibile impostare il colore di un rettangolo mediante un apposito metodo

public class Colore {
    private int R;
    private int G;
    private int B;
    public static final Colore BIANCO = new Colore(255, 255, 255);
    public static final Colore NERO = new Colore(0, 0, 0);

    // Costruttore
    public Colore(int R, int G, int B) {
        this.R = R;
        this.G = G;
        this.B = B;
    }

    // Metodi getter
    public int getR() { return R; }
    public int getG() { return G; }
    public int getB() { return B; }
}
