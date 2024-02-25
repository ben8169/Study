// // testcase
// 35 20 0
// 12 69 59
// 17 43 39
// 91 64 85
// 64 97 35
// 52 32 76
// 72 64 10
// 40 65 86
// 61 84 27
// 28 69 53

//Upgrade
// 1. minmax를 삼항연산자로 -> 삼항연산자 학습

//Further
// 1. 입력받는 정수 갯수를 늘릴 수 있도록 -> 동적할당 학습

#include <stdio.h>

int find_min(int a, int b, int c);
int find_max(int a, int b, int c);
int find_max_ternary(int a, int b, int c);
int find_min_ternary(int a, int b, int c);



int main (void){
    int a, b, c, iter;
    printf("Iteration:");
    scanf("%d", &iter);
    for (int i=0;i<iter;i++){
        scanf("%d %d %d", &a, &b, &c);
        printf("min:%d, max:%d\n",find_min_ternary(a,b,c),find_max_ternary(a,b,c));
    }
    return 0;
}

int find_min(int a, int b, int c){
    if (a<=b){
        if (a<=c){
            return a;
        }else{
            return c;
        }
    } else {
        if (c<=b){
            return c;
        } else {
            return b;
        }
    }
}

int find_max(int a, int b, int c){
    if (a>=b){
        if (b>=c){
            return a;
        }else{
            if (a>=c){
                return a;
            } else {
                return c;
            }
        }
    } else {
        if (c<=b){
            return b;
        } else {
            return c;
        }
    }
}

int find_max_ternary(int a, int b, int c){
    return (a>=b)?((b>=c)?a:(a>=c)?a:c):((c<=b)?b:c);
}

int find_min_ternary(int a, int b, int c){
    return (a<=b)?((a<=c)?a:c):((c<=b)?c:b);
}
