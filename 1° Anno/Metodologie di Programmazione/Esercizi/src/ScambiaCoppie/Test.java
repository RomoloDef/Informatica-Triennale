package ScambiaCoppie;

public class Test {
    public static void main(String[] args) {
        int[] numeri = {1,2,3,4,5,6};
        SequenzaDiInteri sequenza = new SequenzaDiInteri(numeri);

        System.out.println("Prima dello scambio: " + sequenza.toString());
        sequenza.scambia();
        System.out.println("Dopo lo scambio: " + sequenza.toString());
    }
}