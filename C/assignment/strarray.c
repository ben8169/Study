#include <stdio.h>



int main(void){
    char char_arr[5][10];

    for (int i=0; i<5; i++){
        scanf(" %[^\n]",char_arr[i]);
    }

    for (int i=0; i<5; i++){
        printf("%s\n",char_arr[i]);
    }
}