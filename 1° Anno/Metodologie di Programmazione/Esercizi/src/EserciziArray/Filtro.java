package EserciziArray;

public class Filtro {
	
	private int[] array;
	
	// Costruttore
	public Filtro(int[] array) {
		this.array = array;
	}
	
	// metodo passaBasso - restituisce tutti gli elementi <= k nell’ordine iniziale
	public int[] passaBasso(int k) {
        int count = 0;
        for (int elemento : this.array) {
            if (elemento <= k) {
                count++;
            }
        }
        
        int[] filtrati = new int[count];
        
        int index = 0;
        for (int elemento : this.array) {
            if (elemento <= k) {
                filtrati[index] = elemento;
                index++;
            }
        }
        
        return filtrati;
	}
	
	// metodo passaAlto - restituisce tutti gli elementi >= k nell’ordine iniziale
	public int[] passaAlto(int k) {
		int c = 0;
		for(int elemento : this.array) {
			if(elemento >= k) {
				c++;
			}
		}
		
		int[] nuovoArray = new int[c];
		
		int indice = 0;
		for(int i : this.array) {
			if(i >= k) {
				nuovoArray[indice] = i;
				indice++;
			}
		}
		
		return nuovoArray;
	}
	
	// metodo filtra - restituisce l’array iniziale da cui sono state eliminate tutte le occorrenze dell’intero passato in input
	
	}
