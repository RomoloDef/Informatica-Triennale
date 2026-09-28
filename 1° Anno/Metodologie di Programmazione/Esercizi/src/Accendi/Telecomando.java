package Accendi;

public class Telecomando implements Accendibile {
	
    private Dispositivo dispositivo;
    
    // Costruttore
    public Telecomando(Dispositivo dispositivo) {
        this.dispositivo = dispositivo;
    }
    
    public void accendi() {
        dispositivo.accendi();
    }

    public void spegni() {
        dispositivo.spegni();
    }
}
