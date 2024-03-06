#include <stdio.h>

int main (void){
    int principal;
    int count = 0;
    printf("Enter investment amount:");
    scanf(" %d",&principal);

    principal*=1.12;
    printf("%dth Year's amount = %d$\n", count++, principal);
    principal*=1.12;
    printf("%dth Year's amount = %d$\n", count++, principal);
    principal*=1.12;
    printf("%dth Year's amount = %d$\n", count++, principal);
    principal*=1.12;
    printf("%dth Year's amount = %d$\n", count++, principal);
    principal*=1.12;
    printf("%dth Year's amount = %d$\n", count++, principal);

} 
