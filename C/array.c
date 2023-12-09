#include <stdio.h>

#define S_Func(X, Y) (X*2+Y%4)

int main (void){
    int arr[3][3] = {8,2,5,10,4,7,6,9,1};
    int num = S_Func(9-2,*((int*)(arr))-2);
    printf("%d",num);
}