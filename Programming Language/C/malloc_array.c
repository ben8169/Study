#include <stdio.h>
#include <stdlib.h>


int* CreateArray(int n);
int main(void){
    int *arr = CreateArray(100);
    printf("%d\n%d\n",arr[100],arr[0]);
    return 0;
}


int* CreateArray(int n){
    int* list = (malloc(sizeof(int) * n));
    list[100] = 98765;
    return list;

}
