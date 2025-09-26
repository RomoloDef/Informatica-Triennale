package Animali;

public class Test {
    public static void main(String[] args) {
        // Creazione di un animale
        Animale animale = new Animale("media", "gracchia", 2);
        System.out.println("Animale: " + animale);
        
        // Creazione di un gatto
        Animale.Felino felino = animale.new Felino("media", "gracchia", 2);
        Animale.Felino.Gatto gatto = felino.new Gatto("piccola", "miagola", 4);
        System.out.println("Gatto: " + gatto);
        
        // Creazione di una tigre
        Animale.Felino.Tigre tigre = felino.new Tigre("grande", "ruggisce", 4);
        System.out.println("Tigre: " + tigre);
        
        // Creazione di un chihuahua
        Animale.Cane cane = animale.new Cane("piccola", "abbaia", 4);
        Animale.Cane.Chihuahua chihuahua = cane.new Chihuahua("piccola", "abbaia", 4);
        System.out.println("Chihuahua: " + chihuahua);
        
        // Creazione di un beagle
        Animale.Cane.Beagle beagle = cane.new Beagle("media", "abbaia", 4);
        System.out.println("Beagle: " + beagle);
        
        // Creazione di un terranova
        Animale.Cane.Terranova terranova = cane.new Terranova("grande", "abbaia", 4);
        System.out.println("Terranova: " + terranova);
        
        // Creazione di un corvo
        Animale.Uccello uccello = animale.new Uccello("piccola", "gracchia", 2);
        Animale.Uccello.Corvo corvo = uccello.new Corvo("media", "gracchia", 2);
        System.out.println("Corvo: " + corvo);
        
        // Creazione di un passero
        Animale.Uccello.Passero passero = uccello.new Passero("piccola", "gracchia", 2);
        System.out.println("Passero: " + passero);
        
        // Creazione di un millepiedi
        Animale.Uccello.Millepiedi millepiedi = uccello.new Millepiedi("piccola", "gracchia", 2);
        System.out.println("Millepiedi: " + millepiedi);
    }
}

