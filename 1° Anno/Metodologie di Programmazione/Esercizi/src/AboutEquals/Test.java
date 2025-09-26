package AboutEquals;

public class Test {
	
	public static void main(String[] args) {
		System.out.println(5==6);
		
		String s1 = "Mario";
		String s2 = "Mario";
		
		// comportamento atteso : true
		System.out.println(s1 == s1);
		
		// comportamento atteso: false -- ma torna true
		System.out.println(s1 == s2);
		
		String s3 = new String("Mario");
		
		// comportamento atteso: false
		System.out.println(s1 == s3);
	}
}
