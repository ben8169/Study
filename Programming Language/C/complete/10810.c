#include <stdio.h>
#include <stdlib.h>

void changeNumber(int i, int j, int k, int *arr);

int main(void){
	int n, m;
	scanf("%d %d",&n, &m);
	int *arr = (int*)calloc(n,sizeof(int));
	for (int x=0; x<m; x++){
		int i,j,k;
		scanf("%d %d %d",&i,&j,&k);
		changeNumber(i,j,k,arr);
	}	
	for (int i=0; i<n; i++){
		printf("%d ",arr[i]);
	}

	free(arr);
	return 0;
}


void changeNumber(int i, int j, int k, int *arr){
	for (int x=i-1;x<j; x++){
		arr[x] = k;
	}
	return;
}
