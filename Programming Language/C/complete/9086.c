#include <stdio.h>


int main(void){
    int T=0;
    scanf("%d",&T);
    
    for (int i=0;i<T;i++){
        char s[1000];
        scanf("%s",s);
        getchar();
        int j=0;
        printf("%c",s[j]);
        while(s[j+1]!='\0'){
            j++;
        }
        printf("%c",s[j]);
        puts(" ");
    }

    return 0;
}