package ScambiaCoppie;

public class Stringa implements ScambiaCoppie{
	
	private String stringa;
	
	public Stringa(String stringa) {
		this.stringa = stringa;
	}

	public String getStringa() {
		return stringa;
	}
	
	public String toString() {
		return "la stringa è " + stringa; 
	}
	
	@Override
	 public void scambia() {
        char[] chars = stringa.toCharArray();

        for (int i = 0; i < chars.length - 1; i += 2) {
            char temp = chars[i];
            chars[i] = chars[i + 1];
            chars[i + 1] = temp;
        }

        this.stringa = new String(chars);
    }
	
}
