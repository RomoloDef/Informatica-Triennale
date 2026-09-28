package Esercizi;

public class StringaVerticale {
    public static void main(String[] args) {
        if (args.length > 0) {
            stampaVerticale(args[0]);
        } else {
            System.out.println("Nessuna stringa fornita come argomento.");
        }
    }

    public static void stampaVerticale(String str) {
        for (int i = 0; i < str.length(); i++) {
            System.out.println(str.charAt(i));
        }
    }
}
