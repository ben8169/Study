#include <stdio.h>

typedef struct {
	unsigned int a:32;
	unsigned short b:2;
	unsigned int c:2;
}BitField;

	
int main(void){
	BitField bf;
	printf("%lu\n", sizeof(bf));


	return 0;
}
	
