package GiocoDelQuindici;

import java.util.Random; // importo la libreria random così posso inserire casualmente il numero di caselle da 0 a 15

public class GiocoDelQuindici {
	
	private int [][] tabella;
	
	public enum Direzione{			 // uso le enumerazioni al posto dei caso 1-2-3-4 nello swith/case
		su, giu, sinistra, destra;
	}
	
	// Costruttore
	public GiocoDelQuindici() {
		tabella = new int[4][4];
		Random caso = new Random();
		int numeri[] = new int[15]; // creo un array contente i numeri di caselle da 0 a 15
		
		for(int i = 0; i < numeri.length; i++) {
			numeri[i] = i + 1;
			
		// mischia - sarà usato anche come metodo
			
		for (int k = 0; k < 15; k++) {
			int randomIndex = caso.nextInt(15);
            int temp = numeri[randomIndex];
            numeri[randomIndex] = numeri[i];
            numeri[i] = temp;
        }
		
		// inserisco i numeri all'interno della casella
		int contatore = 0;
		for(int r = 0; r < 4 ; r++) {	// itero per le righe
			for(int c = 0; c < 4; c++) {	// itero per le colonne
				if(contatore < 15) {
					tabella[r][c] = numeri[contatore];
					contatore++;
				} else {
					tabella [r][c] = 0;
				}
				
			}
		}
	        
		}
		
	}
	
	// Metodo mischia
	public void mischia() {
		Random caso = new Random();
		for(int r = 0; r < 4; r++) { 	// itero per le righe
			for(int c = 0; c < 4; c++) {  	// itero per le colonne
				int colonnaRandom = caso.nextInt(4);
				int rigaRandom = caso.nextInt(4);
				// Scambio gli elementi della tabellina
                int temp = tabella[r][c];
                tabella[r][c] = tabella[rigaRandom][colonnaRandom];
                tabella[rigaRandom][colonnaRandom] = temp;
			}
		}
		
	}
	
	// Metodo scorri
	public void scorri(int riga, int colonna, Direzione direzione) {
		int temp;
        int nuovaRiga = riga;
        int nuovaColonna = colonna;
        switch(direzione) {
        case su:	// enum su
        	nuovaRiga--;
        	break;
        case giu:	// enum giu
        	nuovaRiga++;
        	break;
        case sinistra:	// enum sinistra
        	nuovaColonna--;
        	break;
        case destra:	// enum destra
        	nuovaColonna++;
        	break;
        default:
        	System.out.println("Errore");
        }
        
     // Verifico se la nuova posizione è valida
        if (nuovaRiga >= 0 && nuovaRiga < 4 && nuovaColonna >= 0 && nuovaColonna < 4) {
            // Faccio lo spostamento
            temp = tabella[riga][colonna];
            tabella[riga][colonna] = tabella[nuovaRiga][nuovaColonna];
            tabella[nuovaRiga][nuovaColonna] = temp;
        } else {
            System.out.println("Movimento non consentito.");
        }
    }
       
	
	// Metodo vinto
	public Boolean vinto() {
	int numero = 1;
    for (int r = 0; r < 4; r++) {
        for (int c = 0; c < 4; c++) {
            if (tabella[r][c] != numero) {
                return false; // Se il numero non è corretto, restituisce falso
            }
            numero++;
            if (numero == 16) {
                return true; // Se abbiamo controllato tutti i numeri correttamente, restituisce vero
            }
        }
    }
    return false; // Se non ha trovato tutti i numeri da 1 a 15, restituisce falso
}
	

}
