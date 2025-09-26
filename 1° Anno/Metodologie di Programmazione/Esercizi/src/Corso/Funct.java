package Corso;

import java.util.ArrayList;

public class Funct {
	
	private ArrayList <Studente> studenti = new ArrayList<>();
	
	public Funct(ArrayList<Studente> studenti) {
		this.studenti = studenti;
	}
	
	public String scriviLista() {
		String lista = " ";
		for(Studente studente: studenti) {
			if(studente.èPassato()) {
				lista += (studente.getVoto() + studente.getNome() + studente.getCognome() + "è passato \n" );
			}
		}
		
		return lista;
	}
	
	public String scriviListaNonPassata() {
		String lista = " ";
		for(Studente studente: studenti) {
			if(!studente.èPassato()) {
				lista += (studente.getVoto() + studente.getNome() + studente.getCognome() + "non è passato \n" );
			}
		}
		
		return lista;
	}
}