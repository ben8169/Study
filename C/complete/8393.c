#include <stdio.h>

int main()
{
	int N = 0, total = 0;
	scanf("%d",&N);
	for (int i = 1;i<=N;i++){
		total += i;
	}
	printf("%d",total);
	return 0;
}
