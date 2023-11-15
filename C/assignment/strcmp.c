#include <stdio.h>

int StringComp(char s1[], char s2[]);

int main (void){
    char s1[10000];
    char s2[10000];
    printf("Input s1\n");
    scanf(" %[^\n]",s1);
    printf("Input s2\n");
    scanf(" %[^\n]",s2);

    printf("%d\n",StringComp(s1,s2));
    return 0;
}


int StringComp(char s1[], char s2[]){
    int cnt1 = 0, cnt2 = 0;

    for (int i=0; s1[i]!= '\0'; i++){
        cnt1 += 1;
    }
    for (int i=0; s2[i]!= '\0'; i++){
        cnt2 += 1;
    }

    if (cnt1 != cnt2){
        return 1;
    }


    int i=0;
    while (s1[i]!='\0'){
        if (s1[i] != s2[i]){
            return 1;
        }
        i++;
    }

    return 0;





}