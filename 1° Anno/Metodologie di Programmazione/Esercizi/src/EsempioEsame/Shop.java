package EsempioEsame;

import java.util.ArrayList;

public class Shop {
	
	private ArrayList<Prodotto> prodotti;
	
	public Shop(ArrayList<Prodotto> prodotti) {
		this.prodotti = prodotti;
	}
	
	public String lists(String prod) {
		String string = "";
		for (Prodotto element: prodotti) {
			if(element.getCategoria().equals(prod)) {
				string += element.getNome() + "" + element.getPrezzo() + "\n"; 
			}
		}
		
		return string;
	}
	
	public float Media(String prod) {
		float media = 0;
		int counter = 0;
		for(Prodotto element: prodotti) {
			if (element.getCategoria().equals(prod)){
				counter++;
				media += element.getPrezzo();
			}
		}
		
		return (media /= counter);
	}
	
	public String printMax() {
		double max = 0;
		for(Prodotto element: prodotti) {
			if(element.getPrezzo() > max) {
				max = element.getPrezzo();
			}
		}
		
		return String.valueOf(max);
	}

}
