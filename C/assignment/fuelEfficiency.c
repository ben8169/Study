// 2022313356 김지헌
#include <stdio.h>

double FuelEfficiency(double liter, double km);

int main(void){
    char check; double liter,km;
    do{
        printf("주입연료량(리터), 주행거리(km)입력:");
        scanf("%lf %lf",&liter,&km);
        printf("1리터로 주행할 수 있는 거리 = %lfkm\n",FuelEfficiency(liter,km));
        printf("다시 계산하겠습니까?(Y/N)");
        scanf(" %c",&check);
        getchar();
    } while(check == 'Y' || check == 'y');
    printf("프로그램 종료\n");
    return 0;
    }



double FuelEfficiency(double liter, double km){
    return km/liter;
}