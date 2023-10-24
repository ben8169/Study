#include <stdio.h>

int main(void){
	short arr[9] = {0};	
	short max = 0, max_index = 0;

	for (int i=0; i<9; i++){
		short n = 0;	
		scanf("%hd", &n);
		arr[i] = n;
	}
	
	for (int i=0; i<9; i++){
		if (arr[i]>max){
			max = arr[i];
			max_index =(short)(i+1);
		}
	}
		

	printf("%hd\n%hd",max,max_index);
	return 0;
}


