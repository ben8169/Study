#include <stdio.h>

int main()
{
	int H, M, new_H, new_M;
	scanf("%d %d",&H, &M);
	new_M = M-45;
	if (new_M<0){
		new_M += 60;
		new_H = H - 1;
		if (new_H < 0){
			new_H = 23;
		}
	}
	else{
		new_H = H;
	}
	printf("%d %d",new_H,new_M);
	return 0;
}
