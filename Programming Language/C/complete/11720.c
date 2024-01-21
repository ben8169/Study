#include <stdio.h>


int main (void){
    int N = 0;
    scanf("%d",&N);
    int sum =0;
    for (int i=0; i<N;i++){
        int n = 0;
        scanf("%1d",&n);
        sum += n;
    }
    printf("%d",sum);



    return 0;
}