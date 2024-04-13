#include <stdio.h>

int main (void){
    int N, answer = 1;
    printf("Enter N:");
    scanf("%d",&N);

    while (N > 1){
        answer *= N;
        N--;
    }
    printf("%d\n",answer);

    return 0;
}