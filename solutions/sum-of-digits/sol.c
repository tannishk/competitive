#include <stdio.h>
long int total(int n)
{
    if(n == 0)
        return 0;
    else
        return (n % 10) + total(n / 10);


}

int main()
{
    int T , N ,i;
    long int sum;
    scanf("%d", &T);
    for(i = 0; i < T; i++ )
    {

        scanf("%d",&N);
        sum = total(N);
        printf("%ld\n", sum);

    }

    return 0;
}
