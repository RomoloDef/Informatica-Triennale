// Progettare una classe Persona i cui oggetti rappresantano una persona e ne memorizzano il nome e il cognome.
// La classe espone un metodo main che crea un'istanza della Persona
// La classe espone anche un metodo stampa che visualizza nome e cognome della persona

public class Persona {
    private String nome;
    private String cognome;

    // Costruttore
    public Persona(String nome, String cognome) {
        this.nome = nome;
        this.cognome = cognome;
    }

    // Metodo per stampare nome e cognome
    public void stampa() {
        System.out.println("Nome: " + this.nome + ", Cognome: " + this.cognome);
    }

    // Metodo main per creare un'istanza della classe Persona
    public static void main(String[] args) {
        Persona persona = new Persona("Mario", "Rossi");
        persona.stampa();
    }
}
