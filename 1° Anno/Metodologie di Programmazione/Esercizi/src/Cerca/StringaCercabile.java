package Cerca;

public class StringaCercabile implements Cercabile {
	
	private String stringa;
	
	public StringaCercabile(String stringa) {
		this.stringa = stringa;
	}
	
	// Getter
	public String getStringa() {
		return stringa;
	}
	
	// toString
	public String toString() {
		return "la stringa è" + " ";
		
	}
	
	@Override
	public boolean cerca(char carattere) {
		if (stringa.indexOf(carattere) >= 0) {
            return true;
        } else {
            return false;
        }
    }
}




