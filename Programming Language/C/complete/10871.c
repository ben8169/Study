#include <stdio.h>

int main(void){
	int N, X, arr[10000];
	scanf("%d %d",&N, &X);
	for (int i=0; i<N; i++){
		int n = 0;
		scanf("%d",&n);
		arr[i] = n;
	};
	
	for (int i=0; i<N; i++){
		if (arr[i]<X)
			printf("%d ",arr[i]);
	};
	
	return 0;
}


