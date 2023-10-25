// 2022313356 김지헌
#include <stdio.h>

int InputPositiveData(void);
int main(void){
    int age = InputPositiveData();
    if (age>=20)
        printf("성년입니다. 나이:%d살",age);
    else
        printf("미성년입니다. 나이:%d살",age);
    


}

int InputPositiveData(void){
    int n = -1;
    do{
        printf("나이 입력:");
        scanf("%d",&n);
        if (n>=0)
            break;
    }while(n<0);
    return n;
}