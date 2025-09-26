class A {
    public void print() {
        System.out.println("A");
    }
}

class B extends A {
    public void print() {
        System.out.println("B");
    }
}

public class Test {
    public static void main(String[] args) {
        A obj = new B();
        obj.print();
    }
}