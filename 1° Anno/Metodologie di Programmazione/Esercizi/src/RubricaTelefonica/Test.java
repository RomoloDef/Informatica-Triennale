package RubricaTelefonica;

import java.util.ArrayList;

public class Test {
	
	public static void main(String[] args) {
		
		ArrayList<Contatto> contatto = new ArrayList<>();
		Rubrica rubrica = new Rubrica(contatto);
		Contatto contatto1 = new Contatto("Romolo", "Deffereria", "3922044009");
		rubrica.aggiungiContatto(contatto1);
		Contatto contatto2 = new Contatto("Gabriella", "Sebastio", "3383019810");
		rubrica.aggiungiContatto(contatto2);
		System.out.println(rubrica.ListaRubrica());
	}

}
