// 2022313356 김지헌
#include <stdio.h>

void DisplayTriangle(int h);

int main(void){
    int h = 0;
    printf("높이를 입력하세요 : ");
    scanf("%d",&h);
    DisplayTriangle(h);
    return 0;
}

void DisplayTriangle(int h){
    for (int i=1;i<=h;i++){
        for (int j=h-1;j>=i;j--){
            printf(" ");
        }
        for (int k=0;k<i;k++){
            printf("*");
        }
        printf("\n");
    }
}

