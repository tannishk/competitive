import java.util.*;
class queue{
    Stack<Integer> ol = new Stack<Integer>();
    Stack<Integer> ne = new Stack<Integer>();
    void push(int n)
    {
        ol.push(n);
    }
    int pop()
    {
        int v;
        while(!ol.empty())
        {
            ne.push(ol.pop());
        }
        v=ne.pop();
        
        while(!ne.empty())
        {
            ol.push(ne.pop());
        }
        return v;
    }
    
}
public class HelloWorld{

     public static void main(String []args){
        queue q = new queue();
        q.push(1);
        q.push(2);
        q.push(3);
        q.push(4);
        System.out.println(q.pop());
        System.out.println(q.pop());
        
     }
}
