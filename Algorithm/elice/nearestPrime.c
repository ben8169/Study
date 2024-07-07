#include <stdio.h>
#include <math.h>

int isPrime(int n) {
    if (n <= 1) return 0;
    if (n == 2) return 1; // 2 is prime
    if (n % 2 == 0) return 0; // Eliminate even numbers

    int sqrt_n = (int) sqrt(n);
    for (int m = 3; m <= sqrt_n; m += 2) {
        if (n % m == 0) {
            return 0;
        }
    }
    return 1;
}

int main(void) {
    int a;
    scanf("%d", &a);
    if (a == 1) {
        printf("2\n");
    } else if (a == 2) {
        printf("3\n");
    } else {
        a--;
        for (; a > 1; a--) {
            if (isPrime(a)) {
                printf("%d\n", a);
                return 0;
            }
        }
    }
    return 0;
}

