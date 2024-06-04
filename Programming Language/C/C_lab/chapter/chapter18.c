#include <stdio.h>
#include <string.h>

int main(void){

//	int i;
//	char msg[] = "C is fun";
//	for (i=0;i<strlen(msg);i++){
//		putchar(msg[i]);
//	}
//	putchar('\n');

// print reversed string.
	int i;
	char msg[25];
	for (i=0;i<25;i++){
		msg[i] = getchar();
		if (msg[i] == '\n'){
			i--;
			break;
		}
	}
	
	for (;i>=0;i--){
		putchar(msg[i]);
	}
	putchar('\n');











    return 0;
}
