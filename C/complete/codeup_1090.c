#include <stdio.h>

int main()
{
	int a, r, n;
	long long answer = 1;
	scanf("%d %d %d",&a, &r, &n);
	answer = a;
	for (int i =0; i<n-1; i++){
		answer *= r;
	}
	printf("%lld",answer);

	return 0;
}
