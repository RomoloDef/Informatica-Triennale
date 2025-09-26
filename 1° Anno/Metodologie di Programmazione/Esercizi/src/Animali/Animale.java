package Animali;

public class Animale {
    
    private String taglia;
    private String verso;
    private int numeroZampe;
    
    // Costruttore
    public Animale(String taglia, String verso, int numeroZampe) {
        this.taglia = taglia;
        this.verso = verso;
        this.numeroZampe = numeroZampe;
    }
    

    // metodo emettiVerso
    public String emettiVerso() {
        return this.verso;
    }
    
    // metodo getNumeroZampe
    public int getNumeroZampe() {
        return this.numeroZampe;
    }
    
    public String getTaglia() {
        return this.taglia;
    }
    
    public String toString() {
	    return "Taglia: " + this.taglia + ", Verso: " + this.verso + ", Numero di zampe: " + this.numeroZampe;
	}

	// Sottoclasse Mammifero di Animale
    public class Mammifero extends Animale {
        
        public Mammifero(String taglia, String verso, int numeroZampe) {
            super(taglia, verso, numeroZampe);
        }
    }
    
    // Sottoclasse Felino di Mammifero
    public class Felino extends Mammifero {
        public Felino(String taglia, String verso, int numeroZampe) {
            super(taglia, verso, 4);
        }

        // Sottoclassi di Felino
        public class Gatto extends Felino {
            public Gatto(String taglia, String verso, int numeroZampe) {
                super("piccola", "miagola", 4);
            }
        }
        
        public class Tigre extends Felino {
            public Tigre(String taglia, String verso, int numeroZampe) {
                super("grande", "ruggisce", 4);
            }
        }
    }
    
    // Sottoclasse Cane di Mammifero
    public class Cane extends Mammifero {
        public Cane(String taglia, String verso, int numeroZampe) {
            super(taglia, verso, numeroZampe);
        }
        
        // Sottoclassi di Cane
        public class Chihuahua extends Cane {
            public Chihuahua(String taglia, String verso, int numeroZampe) {
                super("piccola", "abbaia", 4);
            }
        }
        
        public class Beagle extends Cane {
            public Beagle(String taglia, String verso, int numeroZampe) {
                super("media", "abbaia", 4);
            }
        }
        
        public class Terranova extends Cane {
            public Terranova(String taglia, String verso, int numeroZampe) {
                super("grande", "abbaia", 4);
            }
        }
    }
    
    // Sottoclasse Uccello di Mammifero
    public class Uccello extends Mammifero {
    	public Uccello(String taglia, String verso, int numeroZampe) {
    		super(taglia, verso, numeroZampe);
    	}
    	
    	// Sottoclassi di Uccello
    	public class Corvo extends Uccello {
    		public Corvo(String taglia, String verso, int numeroZampe) {
    			super("media", "gracchiare", 2);
    		}
    	}
    	
    	public class Passero extends Uccello {
    		public Passero(String taglia, String verso, int numeroZampe) {
    			super("piccola", "gracchiare", 2);
    		}
    	}
    	
    	public class Millepiedi extends Uccello {
    		public Millepiedi(String taglia, String verso, int numeroZampe) {
    			super("piccola", "gracchiare", 1000);
    		}
    	}
    }
    
}


