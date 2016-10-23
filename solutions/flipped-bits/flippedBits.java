import java.util.*;

class flippedBits
{
   static int countFlippedBits(int a, int b)
   {
      int axorb = a ^ b, count = 0;
      while(axorb != 0)
      {
         count += axorb & 1;
         axorb >>= 1;
      }
      return count;
   }

   public static void main(String args[])
   {
      int t, a, b;
      Scanner sc = new Scanner(System.in);
      t = sc.nextInt();
      while(t > 0)
      {
         a = sc.nextInt();
         b = sc.nextInt();
         System.out.println(countFlippedBits(a, b));
         t--;
      }
   }
}
