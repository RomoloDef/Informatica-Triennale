package Corso;


public class Studente {
	
	private String matricola;
	private String nome;
	private String cognome;
	private Integer voto;
	
	public Studente(String matricola, String nome, String cognome, int voto) {
		this.matricola = matricola;
		this.nome = nome;
		this.cognome = cognome;
		this.voto = voto;
	}
	
	public Studente(String matricola, String nome, String cognome) {
		this.matricola = matricola;
		this.nome = nome;
		this.cognome = cognome;
	}
	
	public boolean èPassato() {
		return voto != null;
	}
	
	public String getMatricola() {
		return matricola;
	}
	
	public String getNome() {
		return nome;
	}
	
	public String getCognome() {
		return cognome;
	}
	
	public int getVoto() {
		return voto;
	}

}



