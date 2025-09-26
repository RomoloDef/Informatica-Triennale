/*
Scrivere un metodo che, presi in ingresso un testo sotto forma di
stringa e una parola w, trasformi il testo in parole (token) e conti le
occorrenze di w nel testo.
 */ 

import java.util.Scanner;

public class ContaParola{

    public static int Conta(String testo, String parola){
        int count = 0;
        String[] parole = testo.split(" ");
        for (String p : parole){
            if (p.equals(parola)){
                count++;
            }
        }
        return count;
    }

    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.println("Inserisci un testo: ");
        String testo = sc.nextLine();
        System.out.println("Inserisci una parola: ");
        String parola = sc.nextLine();
        System.out.println("La parola " + parola + " compare " + Conta(testo, parola) + " volte nel testo.");
        sc.close();
    }


}
