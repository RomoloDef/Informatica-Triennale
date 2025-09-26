package EserciziArray;

public class Istogramma {
    private int[] conteggio;

    public Istogramma(int i, int j) {
        conteggio = new int[j - i + 1];
    }

    public void incrementa(int elemento) {
        if (elemento >= 0 && elemento < conteggio.length) {
            conteggio[elemento]++;
        }
    }

    public void stampa() {
        for (int i = 0; i < conteggio.length; i++) {
            System.out.print(i + ": ");
            for (int j = 0; j < conteggio[i]; j++) {
                System.out.print("*");
            }
            System.out.println();
        }
    }
    
    public static void main(String[] args) {
        Istogramma istogramma = new Istogramma(0, 31);

        istogramma.incrementa(5);
        istogramma.incrementa(10);
        istogramma.incrementa(5);
        istogramma.incrementa(20);
        istogramma.incrementa(10);
        istogramma.incrementa(10);

        istogramma.stampa();
    }
}
