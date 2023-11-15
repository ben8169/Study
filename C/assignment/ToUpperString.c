#include <stdio.h>


void ToUpperString(char s[]);

int main (void){
    // char str1[100] = "WhaT Is it?";
    char str1[10000];
    printf("Input string\n");
    scanf(" %[^\n]",str1);
    ToUpperString(str1);


    return 0;
}

void ToUpperString(char s[]){
    for (int i=0; s[i]!='\0'; i++){
        if (s[i] >='a' && s[i]<='z'){
            printf("%c",s[i]+'A'-'a');
        }else{
            printf("%c",s[i]);
        }
    }


}