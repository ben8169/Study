#include <stdio.h>
int FindIndex(int [], int, int);

int main(void){
    int n=0;
    int arr[5] = {11, 22, 33, 22, 44};
    int size = sizeof(arr)/sizeof(int);
    scanf("%d",&n);
    int result = FindIndex(arr,n,size);
    if (result == -1){
        printf("%d는 목록에 없습니다\n",n);
    }else{
        printf("%d는 요소 %d에 있습니다\n",n,result);
    }


    return 0;
}


int FindIndex(int a[], int n, int size){
    for (int i=0;i<size;i++){
        if (a[i] == n){
            return i;
        }
    }
    return -1;
}
