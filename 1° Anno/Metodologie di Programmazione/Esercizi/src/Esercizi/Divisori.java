package Esercizi;

public class Divisori {

	public static void main(String[] args) {
		int numero = 20;
		for(int i = 1; i<numero; i++) 
		{
			if((numero%i) == 0) 
			{
				System.out.println(i);
			}
		}
	}
}
