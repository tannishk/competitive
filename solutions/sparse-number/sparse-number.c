#include <stdio.h>

int main(){
    int n,a,j;
    scanf("%d",&n);
    while(n-->0){
        scanf("%d",&a);
        j = a >> 1;
        if(a & j)
            printf("0\n");
        else
            printf("1\n");

    }

    return 0;
}
