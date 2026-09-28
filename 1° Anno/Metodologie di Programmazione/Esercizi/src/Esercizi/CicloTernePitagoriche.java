package Esercizi;

public class CicloTernePitagoriche {
	    
	    public static void stampaTernePitagoriche(int N) {
	        for (int c = 1; c <= N; c++) {
	            for (int b = 1; b < c; b++) {
	                for (int a = 1; a <= b; a++) {
	                    if (a*a + b*b == c*c) {
	                        System.out.println(a + ", " + b + ", " + c);
	                    }
	                }
	            }
	        }
	    }
	    
	    public static void main(String[] args) {
	        stampaTernePitagoriche(15);
	    }
	}
