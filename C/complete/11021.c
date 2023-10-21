#include <stdio.h>

int main()
{	
	int T = 0, a = 0, b = 0;
	scanf("%d",&T);
	for (int i=1; i<=T; i++){
		scanf("%d %d",&a,&b);
		printf("Case #%d: %d\n",i,a+b);
	}
	return 0;
}
