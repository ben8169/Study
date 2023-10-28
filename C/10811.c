#include <stdio.h>
#include <stdlib.h>


int main(void){
    int N, M;
    scanf("%d %d",&N, &M);
    int *arr = (int *)calloc(N,sizeof(int));
    
    for (int i=0; i<N; i++){
        arr[i] = i+1;
    }
    
    for (int i=0; i<M; i++){
        int a, b, num;
        scanf("%d %d",&a, &b);
        num = b-a+1;
        for (int i=a-1;i<num/2;i++){
            arr[a-1-i] = arr[b-1+i]
        }
        


    }

    return 0;
}