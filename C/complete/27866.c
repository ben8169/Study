#include <stdio.h>


int main(void){
	char s[1000];
	scanf("%s",s);
	getchar();
	int i=0;
	scanf("%d",&i);
	printf("%c",*(s+i-1));
	




	return 0;
}
