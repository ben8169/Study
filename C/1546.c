#include <stdio.h>
#include <stdlib.h>


int main (void){
    int N = 0, sum = 0, max = -1;
    scanf("%d", &N);
    int *arr = (int*)calloc(N,sizeof(int));

    for (int i=0; i<N; i++){
        int input = 0;
        scanf("%d",&input);
        arr[i] = input;
    }

    for (int i=0; i<N; i++){
        sum += arr[i];
    }


    for (int i=0;i<N; i++){
        if (max<arr[i]){
            max = arr[i];;
        }
    }

    printf("%lf", (double)(100*sum/N)/max);

    return 0;
}