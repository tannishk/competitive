public class LinkedListNodeCount {

  
  public static void main(String[] args) {

    Node n = new Node("one");
    LinkedList newList = new LinkedList(n);
    newList.addToList("two");
    newList.addToList("three");
    System.out.println(newList.getSize());


  }

    static class Node {
        Node next;
        Object item;
        public Node(Object o) {
            this.item = o;
            this.next = null;
        }
        
        public void setNext(Node n) {
            this.next = n;
        }
        
    }
    
    static class LinkedList {
        Node head;
        int size;
        public LinkedList(Node n) {
            
            this.head = n;
            this.size = 1;
        }
        
        public void addToList(Object o) {
            Node n = new Node(o);
            Node curr = this.head;
            if (head == null) {
                this.head = n;
                this.size += 1;
            }
            else {
                while (curr.next != null) {
                    curr = curr.next;
                }
                curr.next = n;
                this.size += 1;
            }
        }
        
        public int getSize() {
            return this.size;
        }
        
        
        
    }
    
}
