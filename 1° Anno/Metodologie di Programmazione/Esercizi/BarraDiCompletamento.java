// Progettare una classe BarraDiCompletamento i cui oggetti rappresentano una barra di caricamento
// Gli oggetti vengono costruiti con la percentuale di partenza
// La classe espone un metodo incrementa che, data una percentuale in input, incrementa la percentuale di partenza con quella fornita in input(ad es. new BarraDiCompletamento(5).incrementa(10) porta la barra al 15%)
// il metodo toString dell'oggetto restituisce una stringa contenente la percentuale di completamento arrotondata con Math.round()
// il metodo main che crea una barra di completamento che parte da 0, la incrementa prima di 20 punti percentuale e poi di altri 25 e quindi stampa la rappresentazione stringa della barra

public class BarraDiCompletamento {
    
    private int percentuale;

    // Costruttore
    public BarraDiCompletamento(int percentuale) {
        this.percentuale = percentuale;
    }

    // Metodo incrementa
    public int incrementa(int percentuale){  // è una semplice somma tra la barra iniziale e un dato input 
        return this.percentuale += percentuale;
    }

    // Metodo toString
    public String toString(){
        return String.valueOf(Math.round(this.percentuale));
    }

    // Metodo main
    public static void main(String[] args){
        BarraDiCompletamento b = new BarraDiCompletamento(0);
        b.incrementa(20);
        b.incrementa(25);
        System.out.println(b.toString());
    }

}
