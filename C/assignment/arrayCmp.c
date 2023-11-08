#include <stdio.h>

int ArrayCmp(int [], int [], int);

int main(void){
    int arr1[5] = {1,2,3,4,5};
    int arr2[5] = {1,2,3,4,5};
    ArrayCmp(arr1,arr2,5);

}

int ArrayCmp(int a1[], int a2[], int size){
    for (int i=0;i<size;i++){
        if (a1[i]==a2[i]){
            if (i == size-1){
                printf("same\n");
                break;
            }
            else{
                continue;
            }
        }else{
            printf("diff\n");
            break;
        }
    }
    return 0;
}