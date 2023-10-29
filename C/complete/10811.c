#include <stdio.h>
#include <stdlib.h>


int main(void){
    int N, M;
    scanf("%d %d",&N, &M);
    int *arr = (int *)calloc(N+1,sizeof(int));
    
    for (int i=1; i<=N; i++){
        arr[i] = i;
    }
    
    for (int i=0; i<M; i++){
        int a, b, num;
        scanf("%d %d",&a, &b);
        num = b-a+1;
        for (int j=0;j<num/2;j++){
            int tmp = arr[a+j];
            arr[a+j] = arr[b-j];
            arr[b-j] = tmp;
        }
    }

    for (int i=1; i<=N; i++){
        printf("%d ",arr[i]);
    }
    return 0;
}