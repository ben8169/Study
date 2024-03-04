#include <stdio.h>
#include <string.h>
#include "lab7_1.h"
// #define AGELIMIT 20
// #define MYNAME "Paul"
#define PI 3.1415


int main (void){
    int age;
    char childname[14] = "Thomas";

    printf("\n%s는 %d명의 아이를 가지고 있다.\n",FAMILY,KIDS);
    age = 11;
    printf("First Kid %s is %d years old.\n",childname,age);

    strcpy(childname, "Christoper");
    age = 6;
    printf("Second Kid %s is %d years old.\n",childname,age);

    strcpy(childname, "ABCDE ");
    age = 3;
    printf("Third Kid %s is %d years old.\n",childname,age);

    

    float radius = 5.0;
    // printf("The Area of circle whose radius is %20.2f is %2f.\n",radius,PI*radius*radius);
    printf("The Area of circle whose radius is %-20.2f is %2f.\n",radius,PI*radius*radius);

    return 0;
}