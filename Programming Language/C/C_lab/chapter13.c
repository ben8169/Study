#include <stdio.h>

int main(void){
    int N;
    printf("수를 입력하세요:");
    scanf("%d",&N);
    printf("%d는 3으로 나누어떨어%s",N, (N%3)?"지지 않는다\n":"진다\n");
    return 0;
}