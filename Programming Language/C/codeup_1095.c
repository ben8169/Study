#include <stdio.h>
#include <stdlib.h>


int main(void){
	int n,min=10001;
	scanf("%d",&n);
	for (int i=0;i<n;i++){
		int input;
		scanf("%d",&input);
		if (input<min){
			min=input;
		}
	}
	printf("%d",min);





	return 0;
}
