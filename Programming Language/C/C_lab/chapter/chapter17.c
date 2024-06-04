#include <stdio.h>

int main(void){
//	int n;
//	printf("input n\n");
//	scanf(" %d",&n);
//   
//	switch(n){
//	case (1):
//		printf("Hello\n");
//		printf("1\n");
//		break;
//	
//	case (2):
//		printf("Hi\n");
//		printf("2\n");
//		break;
//	case (3):
//		printf("Hola\n");
//		printf("3\n");
//		break;
//	default:
//		printf("default\n");
//		break;
//	}
//
// lab

	int month, year, numdays;
	printf("Input Month\n");
	scanf(" %d",&month);
	
	switch (month){
	case 1: case 3: case 5: case 7: case 8: case 10: case 12:
	{
		numdays = 31;
		break;	
	}
	
	case 4: case 6: case 9: case 11: 
	{
		numdays = 30;
		break;	
	}
	case 2:
	{
		if (((year%4==0) && !(year%100==0)) || (year%400==0)){
			numdays = 29;} else {numdays = 28;}
		break; 
	}	
	default:{
		printf("Wrong Input\n");
		break;
	}
}
	printf("%d has %d days.\n",month, numdays);

 
	return 0;


}
