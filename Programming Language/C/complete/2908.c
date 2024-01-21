#include <stdio.h>

int change_value(int);
int main (void){
    int a, b;
    scanf("%d %d",&a,&b);

    a = change_value(a);
    b = change_value(b);


    if (a>b)
        printf("%d",a);
    else
        printf("%d",b);

    return 0;



}


int change_value(int n){
    int n1, n2, n3;
    n3 = n %10;
    n2 = (n/10)%10;
    n1 = n / 100;

    return (n1+n2*10+n3*100);

}