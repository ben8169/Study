#include <stdio.h>
#include <stdlib.h>

int main(void){
	char c;
	while(c!=EOF){
		scanf(" %c", &c);
		printf("%c\n", c-32);	
	}
	return 0;
}
