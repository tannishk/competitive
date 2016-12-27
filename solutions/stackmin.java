import java.util.*;
public class HelloWorld{
Stack<Integer> s = new Stack<Integer>();
Stack<Integer> s1 = new Stack<Integer>();
public void push(int n)
{
    s.push(n);
    if(s1.empty())
    {
        s1.push(n);
    }
    else if(n<=s1.peek())
    {
        s1.push(n);
    }
}
public int pop()
{
    int value = s.pop();
    if(value == s1.peek())
    {
        s1.pop();
    }
    return value;
}
public int min()
{
    return s1.peek();
}
     public static void main(String []args){
       HelloWorld h = new HelloWorld();
         h.push(7);
         System.out.println(h.min());
         h.push(3);
         System.out.println(h.min());
         h.push(1);
         System.out.println(h.min());
         h.push(0);
         System.out.println(h.min());
         h.pop();
         System.out.println(h.min());
         h.pop();
         System.out.println(h.min());
     }
}
