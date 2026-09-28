package Esercizi;

public class Cat {
	
	String name;
	int numberOfEars;
	
	// Costruttore 1
	public Cat(String name) {
		this.name = name;
		this.numberOfEars = 2;
	}
	
	// Costruttore 2
	public Cat(String name, int numberOfEars) {
		this.name = name;
		this.numberOfEars = numberOfEars;
	}
	
	String miao() {
		return "miaoo";
	}
	
	
	
	
}
