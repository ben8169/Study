#include <stdio.h>

int main()
{
	int a, b, c;
	scanf("%d %d %d",&a,&b,&c);

	if (a == b && b == c){
		printf("%d",10000 + a*1000);
	}

	else if (a != b && b != c && a != c){
		int max = 0;
		max = a;
		if (b>max)
		max = b;
		if (c>max)
		max = c;
		printf("%d",max*100);
	}

	else{
		int same_num = 0;
		if (a == b || a == c)
		same_num = a;
		else if (b == c)
		same_num = b;
		printf("%d",1000 + same_num*100);
	}
	return 0;
}
