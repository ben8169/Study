#include <stdio.h>
#include <string.h>

int main(void){
    // /*Study*/
    // char month[] = "hellow"; // 초기화와 동시에 진행하면 사이즈지정 필요없음
    // printf("%d\n",sizeof(month)); //7

    // // 설정한 변수에 대입은 strcpy
    // strcpy(month, "April");
    // printf("%s\n",month); //7

    /*Lab*/
    char director1[100] = "조쉬 본";
    char director2[] = "크리스벅과 제니퍼 리";
    char director3[100];
    strcpy(director3,"로버트 제메키스");

    char movie1[] = "안녕 헤이즐";
    char movie2[] = "겨울왕국";
    char movie3[] = "백투더 퓨처";

    printf("영화 \"%s\"의 감독은 %s입니다\n",director1,movie1);
    printf("영화 \"%s\"의 감독은 %s입니다\n",director2,movie2);
    printf("영화 \"%s\"의 감독은 %s입니다\n",director3,movie3);
    

    return 0;
}