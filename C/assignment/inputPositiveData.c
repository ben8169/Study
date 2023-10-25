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
    int n = 0;
    while(n>=0){
        printf("나이 입력:");
        scanf("%d",&n);
        if (n<0){
            printf("다시 입력\n");
        }else{
            return n;
        }
    }

}