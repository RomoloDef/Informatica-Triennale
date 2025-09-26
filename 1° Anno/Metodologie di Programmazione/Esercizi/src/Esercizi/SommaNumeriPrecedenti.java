package Esercizi;

public class SommaNumeriPrecedenti {
    
    public static void main(String[] args) {
        int a = 2;
        int b = 3;
        int somma;
        final int N = 6;

        System.out.println(a);
        System.out.println(b);

        for(int i = 0; i<N; i++) {
            somma = a + b;
            System.out.println(somma);
            a = b;
            b = somma;
        }
    }
}