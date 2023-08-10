#include <stdio.h>

int main()
{	
	int a = 0, b1 = 0, b2 = 0, b3 = 0;
	scanf("%d\n%d%d%d", &a, &b1, &b2, &b3);
	printf("%d\n",a*b1);
	printf("%d\n",a*b2);
	printf("%d\n",a*b3);
	printf("%d\n", a*b1 + 10*a*b2 + 100*a*b3);
	
}

