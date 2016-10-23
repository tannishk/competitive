#include<stdio.h>

int countFlippedBits(int, int);

int main()
{
   int a, b, t;
   scanf("%d", &t);
   while(t > 0){
      scanf("%d %d", &a, &b);
      printf("Number of flipped bits to convert %d to %d is %d\n", a, b, countFlippedBits(a, b));
      t--;
   }
   return 0;
}

int countFlippedBits(int a, int b)
{
   int axorb = a ^ b;
   int count = 0;
   while(axorb){
      count += axorb & 1;
      axorb >>= 1;
   }
   return count;
}
