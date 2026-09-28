package EserciziArray;

public class Array {
	
	public static void main(String[] args) {
		String nomi[] = {"mario", "luigi", "wario", "waluigi", "yoshi"};
		String nome = "mario";
		
		boolean ricerca = false;
		int posizione = -1; 
		for(int i = 0; i < nomi.length; i++) {
			if(nomi[i].equals(nome)) {
				ricerca = true;
				posizione = i; 
				break;
			}
		}
		
		if(ricerca) {
			System.out.println("true");
		} else {
			System.out.println("false");
		}
		
		System.out.println(posizione); 
	}
}

