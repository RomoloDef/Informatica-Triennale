package Prove;

public interface StringLinkedingList extends Iterable<String>{
	
	void addFirst(String element);
	void addLast(String element);
	String removeFirst();
	void insertA(String element, int index);
	
}
