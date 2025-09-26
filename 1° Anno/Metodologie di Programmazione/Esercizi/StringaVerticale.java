/*
Scrivere un metodo che legge una stringa da console
(ovvero da input args) e la stampa in verticale un
carattere per linea
 */

public class StringaVerticale {
    
    public static void main(String[] args){
        for(int c = 0; c < args.length ;c++){
            System.out.println(args[c]);
        }
    }
}
