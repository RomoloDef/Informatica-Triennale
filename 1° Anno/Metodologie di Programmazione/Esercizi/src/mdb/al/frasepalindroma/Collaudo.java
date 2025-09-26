package mdb.al.frasepalindroma;

public class Collaudo {
    public static void main(String[] args) {
        String fraseUno = "angelalavalalegna";
        if (FrasePalindroma.èPalindroma(fraseUno)) {
            System.out.println("La frase è palindroma.");
        } else {
            System.out.println("La frase non è palindroma.");
        }
    }
}

