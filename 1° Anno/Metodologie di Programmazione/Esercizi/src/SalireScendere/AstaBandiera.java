package SalireScendere;

public class AstaBandiera implements SaliScendi {
	
	private Bandiera bandiera;
	
	// Costruttore
	public AstaBandiera(Bandiera bandiera) {
		this.bandiera = bandiera;
	}
	
	// Getter
	public Bandiera getBandiera() {
		if(bandiera.sali()) {
			return bandiera;
		} else {
			return null;
		}
	}

	@Override
	public boolean sali() {
		return true;
	}

	@Override
	public void scendi() {
	}
	
	
	
}
