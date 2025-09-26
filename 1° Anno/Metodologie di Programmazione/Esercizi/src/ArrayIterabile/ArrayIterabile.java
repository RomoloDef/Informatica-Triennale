package ArrayIterabile;

import java.util.Iterator;

public class ArrayIterabile implements Iterable<Integer> {
    
    private Integer[] array;
    
    public ArrayIterabile(Integer[] array) {
        this.array = array;
    }
    
    @Override
    public Iterator<Integer> iterator() {
        return new ArrayIterator();
    }
    
    private class ArrayIterator implements Iterator<Integer> {
        private int index = 0;

        @Override
        public boolean hasNext() {
            return index < array.length;
        }

        @Override
        public Integer next() {
            if (!hasNext()) {
                return null; // restituisci null se non ci sono più elementi
            }
            return array[index++];
        }

        @Override
        public void remove() {
            throw new UnsupportedOperationException();
        }
    }
}