#include <stdio.h>

int Delete(int [], int, int);

int main(void){
    int arr[5] = {11,22,33,44,55};
    int size = sizeof(arr)/sizeof(int);

    printf("삭제 전\n");
    for (int i=0;i<size;i++){
        printf("%d\n",arr[i]);
    }
    printf("size:%d\n\n",size);

    printf("삭제 후\n");
    size = Delete(arr,size,3);
    for (int i=0;i<size;i++){
        printf("%d\n",arr[i]);
    }
    printf("size:%d\n\n",size);

    return 0;
}

int Delete(int a[], int s, int p){
    for (int i=p;i<s;i++){
        a[i] = a [i+1];
    }
    return s - 1;
}


