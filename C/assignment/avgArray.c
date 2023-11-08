#include <stdio.h>

void PrintIntegerArray(int [], int);
int GetIntegerArray(int [], int, int);
double AverageIntegerArray (int [], int);


int main(void){





    return 0;
}



void PrintIntegerArray(int a[], int n){
    for (int i=0;i<n;i++){
        printf("%d ",a[i]);
    }
}

int GetIntegerArray(int a[], int n, int s){
    int x=0,i=0;
    do{ 
    scanf("%d",&x);
    a[i] = x;
    i++;
    }while (x!=-1);




}
double AverageIntegerArray (int a[], int n){
    int sum = 0;
    for (int i=0;i<n;i++){
        sum += a[i];
    }
    return sum/n;
}