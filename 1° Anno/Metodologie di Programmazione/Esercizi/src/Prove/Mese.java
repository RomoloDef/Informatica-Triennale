package Prove;

public enum Mese {
	Gen(1), Feb(2), Mar(3), Apr(4), Mag(5), Giu(6), Lug(7), Ago(8), Set(9), Ott(10), Nov(11), Dic(12);


	private int mese;
	
	Mese(int mese){
		this.mese = mese;
	}
	
	public int toInt() {
		return mese;
	}
	
	public static void main(String[] args) {
	    Mese[] mesi = Mese.values();
	    for(int i = 0; i < mesi.length; i++) {
	    	System.out.println(mesi[i] + ": " + mesi[i].toInt());
	    }
	    
	}
	
}
	

