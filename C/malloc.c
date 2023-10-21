#include <stdio.h>
#include <stdlib.h>

int main(void){
    int num = 10, total_num = 30;
    int* malloc_arr, calloc_arr, realloc_arr;
    malloc_arr = (int*) malloc(num * sizeof(int));
    calloc_arr = (int*) calloc(num, sizeof(int));
    realloc_arr = (int*) realloc(malloc_arr, total_num * sizeof(int));

    return 0;
}