package Accendi;

public class Dispositivo implements Accendibile {
	
	@Override
	public void accendi() {
		System.out.println("Benvenuto!");
	}

	@Override
	public void spegni() {
		System.out.println("Arrivederci!");
	}
}
