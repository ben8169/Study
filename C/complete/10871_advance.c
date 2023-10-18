// 중복으로 입력될 경우도 거를 수 있음


#include <stdio.h>

int main(void){
	int N, X, arr[10000],arr2[10000];
	scanf("%d %d",&N, &X);
	for (int i=0; i<N; i++){
		int n = 0;
		scanf("%d",&n);
		arr[i] = n;
	};
	
	if (arr[0] < X)
		printf("%d ", arr[0]);	


	for (int i=1;i<N;i++){
		if (arr[i]<X){
			for (int j = i-1; j>=0; j--){
				 if(arr[j] == arr[i]){
					break;
					}
				 if (j == 0)
					printf("%d ",arr[i]);
				}

		}
	}	
	return 0;
}


