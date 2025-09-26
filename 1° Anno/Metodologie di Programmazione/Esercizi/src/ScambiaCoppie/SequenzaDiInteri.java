package ScambiaCoppie;

import java.util.Arrays;

public class SequenzaDiInteri implements ScambiaCoppie {
    
    private int[] sequenza;
    
    public SequenzaDiInteri(int[] sequenza) {
        this.sequenza = sequenza;
    }
    
    public int[] getSequenza() {
        return sequenza;
    }
    
    @Override
    public String toString() {
        return "la sequenza di interi è " + Arrays.toString(sequenza);
    }

    @Override
    public void scambia() {
        if(sequenza.length < 2) {
            System.out.println("Non è stato possibile effettuare lo scambio");
        } else {
            for(int i = 0; i < sequenza.length - 1; i += 2) {
                int temp = sequenza[i];
                sequenza[i] = sequenza[i+1];
                sequenza[i+1] = temp;
            }
        }
    }
}