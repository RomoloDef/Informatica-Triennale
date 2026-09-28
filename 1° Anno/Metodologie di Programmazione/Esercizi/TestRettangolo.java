// Implementare una classe di test testRettangolo che verifica il corretto funzionamento della classe Rettangolo sul rettangolo in posizione (0,0) e di lunghezza 20 e altezza 10, traslandolo di 10 verso destra e 5 in basso

public class TestRettangolo {
    
    public static void main(String[] args){
        Rettangolo r = new Rettangolo(0, 0, 20, 10);
        r.trasla(10, 5);
        System.out.println(r.toString());
    }
}
