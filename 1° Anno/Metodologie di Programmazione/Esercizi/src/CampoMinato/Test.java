package CampoMinato;

public class Test {

	    public static void main(String[] args) {
	        // Crea un nuovo campo minato 5x5 con 5 mine
	        CampoMinato campo = new CampoMinato(5, 5, 5);

	        // Stampa il campo iniziale
	        System.out.println(campo);

	        // Scopri alcune caselle e stampa il campo dopo ogni mossa
	        campo.scopri(0, 0);
	        System.out.println(campo);
	        campo.scopri(1, 1);
	        System.out.println(campo);
	        campo.scopri(2, 2);
	        System.out.println(campo);

	        // Stampa lo stato del gioco
	        System.out.println(campo.vinto());
	    }
	}

