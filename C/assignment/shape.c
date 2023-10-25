#include <stdio.h>

void DisplayTriangle(int h);

int main(void){
    int h = 5;
    DisplayTriangle(h);
    return 0;
}

void DisplayTriangle(int h){
    for (int i=1;i<=h;i++){
        for (int j=h-1;j>=i;j--){
            printf(" ");
        }
        for (int k=0;k<i;k++){
            printf("*");
        }
        printf("\n");
    }
}




// void DisplayTriangle(int h){
//     for (int i=0;i<h;i++){
//         for (int j=0;j<i;j++){
//             for (int k=0;k<j;k++){
//                 printf(" ");
//             }
//             printf("*");
//         }
//         printf("\n");
//     }

// }