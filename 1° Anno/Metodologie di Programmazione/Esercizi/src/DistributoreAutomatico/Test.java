package DistributoreAutomatico;

public class Test {
    public static void main(String[] args) {
        // Creazione di un distributore automatico con 5 prodotti
        DistributoreAutomatico distributore = new DistributoreAutomatico(5);

        // Inserimento di un importo di 5 euro
        distributore.inserisciImporto(5);

        // Acquisto di un prodotto
        Prodotto prodottoSelezionato = distributore.getProdotto();
        if (prodottoSelezionato != null) {
            System.out.println("Hai selezionato un prodotto con prezzo: " + prodottoSelezionato.getPrezzo());
            System.out.println("Saldo rimanente: " + distributore.getSaldo());
        }

        // Calcolo e stampa del resto
        double resto = distributore.getResto();
        System.out.println("Resto dovuto: " + resto);
    }
}
