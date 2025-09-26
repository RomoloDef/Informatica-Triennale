// Progettare una classe Cerchio i cui oggetti rappresentano un cerchio
// La classe è dotata dei metodi getCirconferenza e getArea(si usi la costante Math.PI)
// La classe espone anche un metodo main che crea due cerchi(di raggio 1 e di raggio 5) e ne stampa la circonferenza(per il primo) e l'area(per il secondo)


public class Cerchio {

    private int raggio;
    public static final double PI = Math.PI;

    // Costruttore
    public Cerchio(int raggio) {
        this.raggio = raggio;
    }

    // Metodo getCirconferenza
    public int getCirconferenza() {
        return (int) (2 * PI * this.raggio);
    }

    // Metodo getArea
    public int getArea() {
        return (int) (PI * this.raggio * this.raggio);
    }

    // Metodo main
    public static void main(String[] args) {
        Cerchio c1 = new Cerchio(1);
        Cerchio c2 = new Cerchio(5);
        System.out.println(c1.getCirconferenza());
        System.out.println(c2.getArea());
    }


    
}
