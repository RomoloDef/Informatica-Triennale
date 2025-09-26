package DisneyVsMarvel;
import java.util.List;
import java.util.Random;

import DisneyVsMarvel.PeterParker.Spiderman;
import DisneyVsMarvel.Pippo.Superpippo;

public class campo {
    private List<Supereroe> squadraDisney;
    private List<Supereroe> squadraMarvel;
    private Random random = new Random();

    public void Partita(List<Supereroe> squadraDisney, List<Supereroe> squadraMarvel) {
        this.squadraDisney = squadraDisney;
        this.squadraMarvel = squadraMarvel;
    }

    public void eseguiTurno() {
        Supereroe attaccanteDisney = squadraDisney.get(random.nextInt(squadraDisney.size()));
        Supereroe attaccanteMarvel = squadraMarvel.get(random.nextInt(squadraMarvel.size()));

        Supereroe difensoreMarvel = squadraMarvel.get(random.nextInt(squadraMarvel.size()));
        Supereroe difensoreDisney = squadraDisney.get(random.nextInt(squadraDisney.size()));

        int dannoDisney = attaccanteDisney.attacca();
        int dannoMarvel = attaccanteMarvel.attacca();

        difensoreMarvel.riceviDanno(dannoDisney);
        difensoreDisney.riceviDanno(dannoMarvel);

        System.out.println("La vita rimanente di " + ((Spiderman) difensoreMarvel).getIdentità() + " è: " + ((Spiderman) difensoreMarvel).getVita());
        System.out.println("La vita rimanente di " + ((Superpippo) difensoreDisney).getIdentità() + " è: " + ((Superpippo) difensoreDisney).getVita());
    }
}
