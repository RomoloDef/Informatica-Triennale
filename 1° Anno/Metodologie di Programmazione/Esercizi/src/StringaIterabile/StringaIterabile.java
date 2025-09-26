package StringaIterabile;

import java.util.Iterator;

public class StringaIterabile implements Iterable<Character> {
	
	private String s;
	
	public StringaIterabile(String s) {
		this.s = s;
	}

	@Override
	public Iterator<Character> iterator() {
		return new StringIterator();
	}
	
	private class StringIterator implements Iterator<Character> {
		
		private int k = 0;
		@Override
		public boolean hasNext() {
			return k < s.length();
		}

		@Override
		public Character next() {
			if (!hasNext()) {
                return '\0'; // restituisci un carattere vuoto se non ci sono più elementi
            }
            return s.charAt(k++);
		}
		
	}
	
}
