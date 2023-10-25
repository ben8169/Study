#include <stdio.h>

int main(void){
        int arr[28];
        for (int i=0; i<28; i++){
               int n = 0;
                scanf("%d",&n);
                arr[i]=n;
                }

        for (int i=1;i<=30;i++){
                for (int j=0;j<28;j++){
                        if (arr[j] == i)
                                break;
                        if (j==27)
                                printf("%d\n",i);
                }
        }

        return 0;
}
