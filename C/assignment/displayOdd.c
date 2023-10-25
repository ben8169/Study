// 2022313356 김지헌
#include <stdio.h>

void DisplayOdd(int s, int e, int m);

int main(void){
    int s, e, m;
    scanf("%d %d %d",&s, &e, &m);
    DisplayOdd(s,e,m);
    return 0;
}


void DisplayOdd(int s, int e, int m){
    int cnt = 0;
    for (int i=s;i<e;i+=2){
        if (cnt > 10){
            printf("\n");
            cnt = 0;
            }
        if ((i%2)==0)
            i += 1;

        if ((i%m) != 0){
            printf("%d ",i);
            cnt += 1;
        }
    }
}