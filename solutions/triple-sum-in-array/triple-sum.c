#include <stdio.h>

int compare(const void * a, const void * b) {
	return (*(int*)a-*(int*)b);
}

int triplesum(int arr[], int N, int X) {
	for(int i=0; i<N-2; i++) {
		int L=i+1, R=N-1;
		while(L<R) {
			int sum=arr[i]+arr[L]+arr[R];
			if(sum==X) {
				return 1;
			}
			else if(sum<X) {
				L++;
			}
			else {
				R--;
			}
		}
	}
	return 0;
}

int main(void) {
	int T;
	scanf("%d", &T);
	while(T--) {
		int N, X;
		scanf("%d%d", &N, &X);
		int arr[N];
		for(int i=0; i<N; i++) {
			scanf("%d", &arr[i]);
		}
		qsort(arr, N, sizeof(int), compare);
		printf("%d\n", triplesum(arr, N, X));
	}
	return 0;
}
