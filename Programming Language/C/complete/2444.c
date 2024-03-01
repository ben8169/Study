#include <stdio.h>
void print_star(int N, int s);

int main(void){
    int N;
    scanf("%d",&N);
    
    for (int i=0;i<N;i++){
        print_star(N,i);
        printf("\n");
    }
    for (int i=N-2;i>=0;i--){
        print_star(N,i);
        printf("\n");
    }

    return 0;
}

void print_star(int N, int s){
    int length = 2*N-1;
    int star = 2*s+1;
    int space = (int)(length-star)/2;
    for (int i=0;i<space;i++)
        printf(" ");
    for (int i=0;i<star;i++)
        printf("*");
    for (int i=0;i<space;i++)
        printf(" "); 
}