#include <stdio.h>
 
long gcd(long a, long b){
    if (a>b){
        long tmp = a;
        a = b;
        b = tmp;
    }
    long tmp2;
    while (a%b!=0){
        tmp2 = b;
        b = a%b;
        a = tmp2;
    }
    return b;
}

long lcm(long a, long b){
    return a*b/gcd(a,b);
}

long main(void){
    long a, b;
    scanf("%ld %ld",&a, &b);
    printf("%ld %ld",gcd(a,b), lcm(a,b));

}