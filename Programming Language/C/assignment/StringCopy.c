#include <stdio.h>
#include <string.h>

char* StringCopy(char* src);
int main(void){
    char* dst = StringCopy("Hello");
    printf("%s",dst);

    return 0;
}


char* StringCopy(char* src){
    char* dst = src;
    return dst;
}