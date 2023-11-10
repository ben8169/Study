
#include <stdio.h>

void PrintIntegerArray(int [], int);
int GetIntegerArray(int [], int, int);
double AverageIntegerArray (int [], int);


int main(void){
    int n = 5, s = -1;
    int arr[5];

    GetIntegerArray(arr, n, s);
    PrintIntegerArray(arr, n);
    double avg = AverageIntegerArray(arr, n);
    printf("average = %.2lf", avg);

    return 0;
}

void PrintIntegerArray(int a[], int n){
    for (int i = 0; i < n; i++){
        printf("%d ", a[i]);
    }
}

int GetIntegerArray(int a[], int n, int s){
    int n_input = 0;

    for (int i = 0; i < n; i++){
        scanf("%d", &n_input);
        if (n_input <= -1 * s){
            break;
        }else{
            a[i] = n_input;
        }
    }
    return 0;
}

double AverageIntegerArray(int a[], int n){
    int sum = 0;
    for (int i = 0; i < n; i++){
        sum += a[i];
    }
    return (double)sum / n;
}

