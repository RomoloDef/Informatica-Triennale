package mdb.al.frasepalindroma;

public class FrasePalindroma {
	
	    public static boolean èPalindroma(String stringa) {
	        int lunghezza = stringa.length();
	        for(int i = 0; i < lunghezza / 2; i++) {
	            if (stringa.charAt(i) != stringa.charAt(lunghezza - 1 - i)) {
	                return false;
	            }
	        }
	        return true;
	    }
	}


	

	

