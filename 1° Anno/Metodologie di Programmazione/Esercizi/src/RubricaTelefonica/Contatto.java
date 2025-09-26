package RubricaTelefonica;

public class Contatto {
	
	private String nome;
	private String cognome;
	private String numero;
	
	public Contatto(String nome, String cognome, String numero) {
		this.nome = nome;
		this.cognome = cognome;
		this.numero = numero;
	}
	
	public String getNome() {
		return nome;
	}
	
	public String getCognome() {
		return cognome;
	}
	
	public String getNumero() {
		return numero;
	}

}
