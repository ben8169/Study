#include <stdio.h>

int main (void){
    // /*Study*/
    // float cost;
    // unsigned short year,month,date;
    // printf("Cost 입력\n");
    // scanf(" %f",&cost);     // 아하! 이렇게 띄워서 버퍼 비워주는게 좋구나!
    // printf("%f\n",cost);
    // // printf("Cost 입력\n");
    // // scanf(" %f",&cost);
    // // printf("%f\n",cost);
    // // printf("Cost 입력\n");
    // // scanf(" %f",&cost);
    // // printf("%f\n",cost);
    // // printf("Cost 입력\n");
    // // scanf(" %f",&cost);
    // // printf("%f\n",cost);

    // printf("Input date:\n");
    // scanf("%hu/%hu/%hu", &year, &month, &date);  // 강제로 뭔가 입력하게 할 수 있다

    /*Lab*/
    char city[10];
    short date;
    double temperature;

    printf("Where do you live?\n");
    scanf(" %s",city);

    printf("What's the date today?\n");
    scanf(" %hd",&date);

    printf("What is the temperature today?\n");
    scanf(" %lf", &temperature);


    printf("%hdth %.1lf'C, city is %s\n",date,temperature,city);






    return 0;
}