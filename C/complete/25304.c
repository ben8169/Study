#include <stdio.h>

int main()
{
	long long X = 0, total = 0;
	int N = 0, a = 0, b = 0;
	scanf("%lld\n%d",&X,&N);
	for (int i = 1; i <= N; i++)
	{
		scanf("%d %d",&a, &b);
		total += a*b;
	}

	if (X == total){
		printf("Yes");
	}
	else{
		printf("No");
	}

	return 0;
}
