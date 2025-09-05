#include <stdio.h>
#include <stddef.h>  // for alignof

int main(void) {
    int arr[4];
    int a, b, c;

    printf("Size of int: %zu\n", sizeof(int));
    printf("Alignment of int: %zu\n", alignof(int));

    for (int i = 0; i <= 3; i++) {
        printf("Address of arr[%d]: %p\n", i, &(arr[i]));
    }

    printf("Address of a: %p\n", &a);
    printf("Address of b: %p\n", &b);
    printf("Address of c: %p\n", &c);

    return 0;
}
