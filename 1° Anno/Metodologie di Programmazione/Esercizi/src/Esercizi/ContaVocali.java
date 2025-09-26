package Esercizi;

public class ContaVocali {
	
	public static void main(String[] args) {
		
		String stringa = "le aiuole sono pulite";
		int conteggioA = 0;
		int conteggioE = 0;
		int conteggioI = 0;
		int conteggioO = 0;
		int conteggioU = 0;
		
		for(int c = 0; c < stringa.length(); c++) {
			char carattere = stringa.charAt(c);
			
			if (carattere == 'a') {
				conteggioA++;
			}
			if (carattere == 'e') {
				conteggioE++;
			}
			if (carattere == 'i') {
				conteggioI++;
			}
			if (carattere == 'o') {
				conteggioO++;
			}
			if (carattere == 'u') {
				conteggioU++;
			}
			
		}
		
		System.out.println(conteggioA);
		System.out.println(conteggioE);
		System.out.println(conteggioI);
		System.out.println(conteggioO);
		System.out.println(conteggioU);
		
	}

}
