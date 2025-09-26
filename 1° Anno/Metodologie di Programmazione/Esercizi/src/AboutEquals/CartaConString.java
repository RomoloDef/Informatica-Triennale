package AboutEquals;

public class CartaConString {
	
	String seme;
	String valore;
	
	public CartaConString(String seme, String valore) {
		this.seme = seme;
		this.valore = valore;
	}
	
	@Override
	public String toString() {
		return "Seme: "+seme+" Valore: "+valore;
	}
	
	public String getSeme() {
		return seme;
	}
	
	public String getValore() {
		return valore;
	}
	
	@Override
	public boolean equals(Object o) {
		// se sto confrontando lo stesso riferimento in memoria -> true
		if(this==o) return true;
		if(o == null || !this.getClass().equals(o.getClass())) return false;
		// i campi devono essere uguali
		if(seme.equals( ((CartaConString)o).getSeme()) && 
		 valore.equals( ((CartaConString)o).getValore())) return true;
		return false;
	}
	
}
