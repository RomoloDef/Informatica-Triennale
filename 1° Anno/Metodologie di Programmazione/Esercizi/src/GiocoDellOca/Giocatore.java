package GiocoDellOca;

import java.util.Random;

public class Giocatore {
	
	private int posizione;
	private int punti;
	private String nome;
	
	public Giocatore(String nome) {
		this.nome = nome;
	}
	
	public int getPosizione() {
		return posizione;
	}
	
	public void setPosizione(int delta) {
		posizione += delta;
	}
	
	public int getPunti() {
		return punti;
	}
	
	public void setPunti(int delta) {
		punti += delta;
	}
	
	@Override
	public String toString() {
		return "Giocatore " + nome;
	}
	
	public int tiraDadi() {
		Random r = new Random();
		
		return (r.nextInt(6)+1)+(r.nextInt(6)+1);
	}
	
	

}
