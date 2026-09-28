// Progettare una classe Quadrato, i cui oggetti sono costruiti con il lato dello stesso
// La classe è dotata di un metodo getPerimetro che restituisce il perimetro
// E di un metodo main che crea un quadrato di lato 4 e ne stampa a video il perimetro

public class Quadrato {

    private int lato;

    // Costruttore
    public Quadrato(int lato) {
        this.lato = lato;
    }

    // Metodo getPerimetro
    public int getPerimetro() {
        return 4 * this.lato;
    }

    // Metodo main
    public static void main(String[] args) {
        Quadrato q = new Quadrato(4);
        System.out.println(q.getPerimetro());
    }


}
