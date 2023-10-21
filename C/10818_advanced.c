// https://www.acmicpc.net/status?user_id=ben8169&problem_id=10818&from_mine=1
// 포인터로 풀어보삼
// static 변수 파라미터로 쓰는 경우 한번 만들어보고 질문해봐

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

void MINMAX_Evaluation(int n1, int i, int N);

int main(void){
	unsigned int N;
	int* arr;

	scanf("%u",&N);
	arr = (int*) malloc(N*sizeof(int));
	
	for (int i=0;i<N;i++){
		int n = 0;
		scanf("%d",&n);
		arr[i] = n;
	}

	for (int i=0;i<N;i++){
		MINMAX_Evaluation(arr[i],i,N);
	}
	free(arr);
	return 0;
}
void MINMAX_Evaluation(int n1, int i, int N){
	static int min;
	static int max;
	static bool initialized = false;

        if (!initialized) {
        	min = n1;
	        max = n1;
		initialized = true;
    	}

	if (n1<min)
		min = n1;
	if (n1>max)
		max = n1;
//	printf("min = %d, max = %d, i = %d, N = %d\n", min,max,i,N);
	if (i == N-1)
		printf("%d %d", min, max);
	else
		return;
}


