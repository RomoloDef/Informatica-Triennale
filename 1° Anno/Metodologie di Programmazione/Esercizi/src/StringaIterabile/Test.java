package StringaIterabile;

public class Test {
	
	public static void main(String[] args) {
		String stringhe = "ciao";
		StringaIterabile stringaIterabile = new StringaIterabile(stringhe);
		
		for(Character stringa : stringaIterabile) {
			System.out.println(stringa);
		}
	}
}
