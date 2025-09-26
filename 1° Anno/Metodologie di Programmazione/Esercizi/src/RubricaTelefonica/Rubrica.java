package RubricaTelefonica;

import java.util.ArrayList;
 

public class Rubrica {
	
	private ArrayList<Contatto> contatti;
	
	public Rubrica(ArrayList <Contatto> contatti) {
		this.contatti = contatti;
	}
	
	public String ListaRubrica() {
		String lista = " ";
		for (Contatto contatto: contatti) {
			lista += contatto.getNome() + "," + contatto.getCognome() + " :" + contatto.getNumero() + "\n";
		}
		
		return lista;
	}
	
	public void aggiungiContatto(Contatto contatto) {
		contatti.add(contatto);
	}
	
	public void rimuoviContatti(String nome, String cognome) {
		
		for(int i = 0; i < contatti.size(); i++) {
			Contatto contatto = contatti.get(i);
			if (contatto.getNome().equals(nome) && contatto.getCognome().equals(cognome)) {
				contatti.remove(i);
			}
		}
		
	}
	
	

}
