package SalireScendere;

public class Ascensore implements SaliScendi {
    private int pianoCorrente;
    private int numeroPiani;

    public Ascensore(int numeroPiani) {
        this.numeroPiani = numeroPiani;
        this.pianoCorrente = 0;
    }

    @Override
    public boolean sali() {
        if (pianoCorrente < numeroPiani) {
            pianoCorrente++;
            return true;
        }
        return false;
    }

    @Override
    public void scendi() {
        if (pianoCorrente > 0) {
            pianoCorrente--;
        }
    }

    public int getPianoCorrente() {
        return pianoCorrente;
    }
}