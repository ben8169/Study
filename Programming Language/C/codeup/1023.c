#include <stdio.h>


int main(void){
	double f;
	int a;
	double b;


	scanf("%lf", &f);
	a = (int)f;
	b = f - (double)a;
	
	printf("%d",a);	
	printf("%lf",b);
	//printf("%6lf",f);






	return 0;	
}
