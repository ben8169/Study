#include <stdio.h>

int main()
{	
	int a = 0, b = 0, b1 = 0, b2 = 0, b3 = 0;
	scanf("%d\n%d", &a, &b);
	b1 = b / 100;
	b2 = (b / 10) % 10;
	b3 = b % 10;
	printf("%d\n",a*b3);
	printf("%d\n",a*b2);
	printf("%d\n",a*b1);
	printf("%d\n",a*b);

}

