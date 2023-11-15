#include <stdio.h>

void StringCopy(char dst[], char src[]);

int main(void){
    char src[10000], dst[10000];
    scanf(" %[^\n]",src);
    StringCopy(dst,src);
    printf("%s",dst);
    return 0;
}



void StringCopy(char dst[], char src[]){
    for (int i=0; src[i]!='\0'; i++){
        dst[i] = src[i];
    }
}