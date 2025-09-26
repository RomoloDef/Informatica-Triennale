package Cerca;

public class ListaCercabileDiInteri implements Cercabile {
	
	private int[] lista = new int[0];
	private int intero; 
	
	// Costruttore
	public ListaCercabileDiInteri(int[] lista, int intero) {
		this.lista = lista;
		this.intero = intero;
	}
	
	// Getters
	public int[] getLista() {
		return lista;
	}
	
	public int getIntero() {
		return intero;
	}
	
	
	// toString
	public String toString() {
		return "la lista in questione è " + lista + " e l'intero invece è " + intero;
	}
	
	// metodo aggiungi
	public void aggiungi(int intero) {
	    int[] nuovoArray = new int[lista.length + 1];
	    for (int i = 0; i < lista.length; i++) {
	        nuovoArray[i] = lista[i];
	    }
	    nuovoArray[lista.length] = intero;
	    lista = nuovoArray;
	}
	
	
	@Override
	public boolean cerca(char carattere) {
	    int valore = (int) carattere;
	    for (int i = 0; i < lista.length; i++) {
	        if (lista[i] == valore) {
	            return true;
	        }
	    }
	    return false;
	}
}
