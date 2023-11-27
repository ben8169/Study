#include <stdio.h>
#include <string.h>


int main(void){
    char str[101];
    scanf("%s",str);
    int n = strlen(str);

    for (char c = 97;c<123;c++){
        for (int i=0;i<n;i++){
            if (c == str[i]){
                printf("%d ",i);
                break;
            }
            if (i == n-1){
                printf("-1 ");
            }
        }

    }


    return 0;
}