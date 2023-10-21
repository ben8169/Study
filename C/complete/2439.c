#include <stdio.h>

int main()
{
	char N = 0;
	scanf("%d",&N);
	for (int count = 1; count <= N; count++){
		for (int i=1; i<=N-count; i++){
			printf(" ");
		}
		for (int j=1; j<=count; j++){
			printf("*");
		}
		printf("\n");
	}

	}


