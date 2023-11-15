#include <stdio.h>

void StringConcat(char s1[], char s2[]);
int main(void){
    char s1[10000],s2[10000];
    printf("Input s1\n");
    scanf(" %[^\n]",s1);
    printf("Input s2\n");
    scanf(" %[^\n]",s2);

    StringConcat(s1,s2);

    printf("%s",s1);

    return 0;
}


void StringConcat(char s1[], char s2[]){
    int s1_len = 0;
    while (s1[s1_len] != '\0'){
        s1_len++;
    }

    for (int i=0; s2[i]!= '\0'; i++)
        s1[s1_len+i] = s2[i];

}