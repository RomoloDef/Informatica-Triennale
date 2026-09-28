package ArrayIterabile;

public class Test {
    public static void main(String[] args) {
        Integer[] numbers = {1, 2, 3, 4, 5};
        ArrayIterabile arrayIterabile = new ArrayIterabile(numbers);

        for (Integer number : arrayIterabile) {
            System.out.println(number);
        }
    }
}