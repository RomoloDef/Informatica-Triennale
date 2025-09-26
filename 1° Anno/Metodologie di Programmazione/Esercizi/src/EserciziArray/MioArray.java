package EserciziArray;

public class MioArray {
    private int[] arrayDiInteri;

    public MioArray(int[] arrayDiInteri) {
        this.arrayDiInteri = arrayDiInteri;
    }

    public boolean contiene(int intero, int posizione) {
        if (posizione >= 0 && posizione < arrayDiInteri.length) {
            return arrayDiInteri[posizione] == intero;
        } else {
            return false;
        }
    }

    public int somma2() {
        if (arrayDiInteri.length >= 2) {
            return arrayDiInteri[0] + arrayDiInteri[1];
        } else if (arrayDiInteri.length == 1) {
            return arrayDiInteri[0];
        } else {
            return 0;
        }
    }

    public void scambia(int posizione1, int posizione2) {
        if (posizione1 >= 0 && posizione1 < arrayDiInteri.length && posizione2 >= 0 && posizione2 < arrayDiInteri.length) {
            int temp = arrayDiInteri[posizione1];
            arrayDiInteri[posizione1] = arrayDiInteri[posizione2];
            arrayDiInteri[posizione2] = temp;
        } else {
            System.out.println("Le posizioni specificate non sono valide.");
        }
    }

    public int maxTripla() {
        int primo = arrayDiInteri[0];
        int ultimo = arrayDiInteri[arrayDiInteri.length - 1];
        int mezzaPosizione = arrayDiInteri.length / 2;
        int mezzo = arrayDiInteri[mezzaPosizione];

        int primoMassimo = Math.max(primo, ultimo);
        int Max = Math.max(primoMassimo, mezzo);
        return Max;
    }

    public int[] falloInDue() {
        if (arrayDiInteri.length < 2) {
            return null;
        }

        int primo = arrayDiInteri[0];
        int ultimo = arrayDiInteri[arrayDiInteri.length - 1];

        int[] arraySecondo = {primo, ultimo};

        return arraySecondo;
    }

    public static void main(String[] args) {
        int[] array = {1, 2, 3, 4, 5};
        MioArray mioArray = new MioArray(array);

        System.out.println(mioArray.contiene(3, 2));
        System.out.println(mioArray.somma2());
        mioArray.scambia(1, 2);
        System.out.println(mioArray.maxTripla());
        int[] nuovoArray = mioArray.falloInDue();
        if (nuovoArray != null) {
            for (int i : nuovoArray) {
                System.out.println(i);
            }
        }
    }
}

