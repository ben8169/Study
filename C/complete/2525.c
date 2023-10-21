#include <stdio.h>

int main()
{
	int H, M, T;
	scanf("%d %d\n%d",&H,&M,&T);
	M += T;

	if (M>=60){
		H += M/60;
		M %= 60;
		if (H>=24){
			H %= 24;
		}
	}

	printf("%d %d",H,M);
	return 0;
}
