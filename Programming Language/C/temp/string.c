#include <stdio.h>
#include <string.h>

int main(void){
	printf("%lu %lu\n", strlen("Hello"),sizeof("Hello"));
	return 0;
}

strcpy(str1,str2);
strncpy(str1,str2,2);

strcat(str1,str2);
strncat(str1,str2,(sizeof(str1)-strlen(str2)-1));

strcmp(str1,str2); //str1[i]-str2[i];
strncmp(str1,str2,5);

strchr(str,'-');
strstr(str,"chuo");

char ptr* = strtok(str,",+-=*/%");
while (ptr!=NULL){
	puts(ptr);
	ptr = strtok(NULL,',');
}

////////////

Getchar, fgetc
Putchar, fputc

Fgets, scanf
Puts, fputs

Sscanf
Sprint

#ctype.h
Toupper
Tolower

Atoi // to int
Atol // to long
Atoll // to long long 
Atof // to double

Getchar() -> to clear up the input buffer
Fflush() -> to clear up the output buffer





