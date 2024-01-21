#include <stdio.h>
#include <string.h>

int main(void){
    int T;
    scanf("%d",&T);
    for (int i=0;i<T;i++){
        int R; char str[20];
        scanf("%d",&R);
        scanf("%s",str);
        int n = strlen(str);
        for (int k=0; k<n;k++){
            for (int j=0;j<R;j++){
                printf("%c",*(str+k));
            }
        }
        printf("\n");
    }

    return 0;
}