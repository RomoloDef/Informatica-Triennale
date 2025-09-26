package Esercizi;

public class StringheVerticali {
    public static void main(String[] args) {
        if (args.length >= 3) {
            stampaVerticali(args[0], args[1], args[2]);
        } else {
            System.out.println("Fornire almeno tre stringhe come argomenti.");
        }
    }

    public static void stampaVerticali(String str1, String str2, String str3) {
        int maxLength = Math.max(Math.max(str1.length(), str2.length()), str3.length());
        for (int i = 0; i < maxLength; i++) {
            System.out.print(i < str1.length() ? str1.charAt(i) : " ");
            System.out.print(i < str2.length() ? str2.charAt(i) : " ");
            System.out.println(i < str3.length() ? str3.charAt(i) : " ");
        }
    }
}
