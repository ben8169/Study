#include <stdio.h>
#include <stdlib.h>

int main(void){
	int N, M;
	scanf("%d %d", &N, &M);
	int *arr = (int *)malloc(N * sizeof(int));
	
	for (int i=0; i<N; i++){
		arr[i] = i+1;
	}	
	
	for (int i=0;i<M;i++){
		int a=0,b=0,tmp=0;
		scanf("%d %d",&a,&b);
		tmp = arr[a-1];
		arr[a-1] = arr[b-1];
		arr[b-1] = tmp;
	}

	for (int i=0; i<N; i++){
		printf("%d ",arr[i]);
	}



	return 0;
}
