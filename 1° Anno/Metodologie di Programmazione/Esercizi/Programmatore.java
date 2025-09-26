/*
 * Progettare una classe Programmatore i cui oggetti rappre-
sentano persone che svolgono il lavoro di sviluppo presso un’azienda La classe

implementa i seguenti metodi:
- un costruttore con il nome e cognome della persona.
- un metodo setAzienda che imposta il nome dell’azienda per cui la persona
lavora.
- un metodo addLinguaggio che aggiunge un linguaggio di programmazione a
quelli inizialmente usati dal programmatore.

- i metodi getNome, getCognome e getAzienda che restituiscono i valori cor-
rispondenti.

- un metodo getLinguaggi che restituisce la stringa dei linguaggi (separati da
spazio) noti al programmatore.
 */

public class Programmatore {
    private String nome;
    private String cognome;
    private String azienda;
    private String linguaggi = ""; 

    // Costruttore
    public Programmatore(String nome, String cognome) {
        this.nome = nome;
        this.cognome = cognome;
    }

    // Metodo setAzienda
    public void setAzienda(String azienda) {
        this.azienda = azienda;
    }

    // Metodo addLinguaggio
    public void addLinguaggio(String linguaggio) {
        this.linguaggi += linguaggio + " ";
    }

    // Metodi getNome, getCognome, getAzienda
    public String getNome() {
        return this.nome;
    }

    public String getCognome() {
        return this.cognome;
    }

    public String getAzienda() {
        return this.azienda;
    }

    // Metodo getLinguaggi
    public String getLinguaggi() {
        return this.linguaggi.trim(); 
    }

    public static void main(String[] args) {
        Programmatore p = new Programmatore("Romolo", "Deffereria");
        p.setAzienda("ACME Inc.");
        p.addLinguaggio("Java");
        p.addLinguaggio("Python");
        System.out.println(p.getNome());
        System.out.println(p.getCognome());
        System.out.println(p.getAzienda());
        System.out.println(p.getLinguaggi());
    }
}