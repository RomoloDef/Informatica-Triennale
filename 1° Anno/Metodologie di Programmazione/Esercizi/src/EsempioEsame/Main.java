package EsempioEsame;

import java.util.ArrayList;
import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;

public class Main {
	
	public static void main(String[] args) {
		Scanner reader;
		try {
			reader = new Scanner(new File("products.txt"));
		} catch (FileNotFoundException exc) {
			System.out.println("file not found");
			return;
		}
		ArrayList <Prodotto> prodotti = new ArrayList <>();
		String[] line;
		while (reader.hasNextLine()) {
			line = reader.nextLine().split(" ");
			prodotti.add(new Prodotto(line[0],line[1], Float.parseFloat(line[2])));
		}
		Shop shop = new Shop(prodotti);
		System.out.println(shop.lists("Shoes"));
		System.out.println(shop.Media("Pants"));
		System.out.println(shop.printMax());
	}

}
