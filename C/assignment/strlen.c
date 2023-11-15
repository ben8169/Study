#include <stdio.h>

int StringLength(char s[]);

int main(void){
    char str[100];
    scanf(" %[^\n]",str);
    printf("%d\n",StringLength(str));

    return 0;
}


int StringLength(char s[]){
    int cnt = 0;
    for (int i=0; s[i]!= '\0'; i++){
        cnt += 1;
    }
    return cnt;

}