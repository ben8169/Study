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
    int n_input = 0;
    int arr[] = a;

    
    for (int i=0;i<n;i++){
        scanf("%d",&n_input);
        if (n_input == -1){
            break;
        }else if (n_input < -1){
            printf("invalid input\n");
            break;
        }else{
            a[i] = n_input;
        }
    }


}
double AverageIntegerArray (int a[], int n){
    int sum = 0;
    for (int i=0;i<n;i++){
        sum += a[i];
    }
    return sum/n;
}