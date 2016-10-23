import java.util.*;

class SumOfDigits
{
   static int sum(int number)
   {
      int sum = 0;
      while (number != 0)
      {
         sum += number % 10;
         number /= 10;
      }
      return sum;
   }

   public static void main (String args[])
   {
      int t, number;
      Scanner sc = new Scanner(System.in);
      t = sc.nextInt();
      while(t > 0)
      {
         number = sc.nextInt();
         System.out.println(sum(number));
         t--;
     }
   }
}
