#include <stdio.h>


int main(void){
    int arr[10]={0}, cnt = 0;
    for (int i=0;i<10;i++){
        int n=0;
        scanf("%d",&n);
        arr[i]=n%42;
    }


    for (int i=0;i<42;i++){
        for (int j=0;j<10;j++){
            if (arr[j]==i){
                cnt +=1;
                break;
            }
        }

    }

    printf("%d",cnt);

    return 0;
}
