#include <stdio.h>
#include <string.h>

int main(void){
    int i=0;
	while (i<200){
		char str[100] = {0,};
		scanf(" %[^\n]",str);
		printf("%s\n",str);
        i++;
	}
	return 0;
}
