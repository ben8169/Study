#include <stdio.h>

int main (void){
//	char name[] = "string size calculatable?";
//	char name[] = "한글이";
//	char name[] = "ひらがな";
	char name[] = "私";
	int arr[]={1,2,3,4,5,6,7};

	printf("%lu\n",sizeof(name));
	printf("%lu\n",sizeof(arr));

	return 0;
}
