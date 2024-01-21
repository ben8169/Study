#include <stdio.h>
#include <stdlib.h>

void MINMAX_Evaluation(int n, int *min, int *max);

int main(void){
	unsigned int N;
	int *arr, min, max;

	scanf("%u",&N);
	arr = (int*) malloc(N*sizeof(int));
	
	for (int i=0;i<N;i++){
		int n = 0;
		scanf("%d",&n);
		arr[i] = n;
	}
	
	min = arr[0];
	max = arr[0];

	for (int i=0;i<N;i++){
		MINMAX_Evaluation(arr[i],&min,&max);
	}
	printf("%d %d",min,max);
	free(arr);
	return 0;
}

void MINMAX_Evaluation(int n, int *min, int *max){
	if (n<*min)
		*min = n;
	if (n>*max)
		*max = n;
}
