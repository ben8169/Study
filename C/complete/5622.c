#include <stdio.h>
#include <string.h>

int main(void){
    char str[16];
    scanf("%s",str);
    int cnt = strlen(str);

    for (char *i=str;*i!='\0';i++){
        switch(*i){
            case 'A': case 'B': case 'C':
                cnt +=2;
                break;
            case 'D': case 'E': case 'F':
                cnt +=3;
                break;
            case 'G': case 'H': case 'I':
                cnt +=4;
                break;
            case 'J': case 'K': case 'L':
                cnt +=5;
                break;
            case 'M': case 'N': case 'O':
                cnt +=6;
                break;
            case 'P': case 'Q': case 'R': case 'S':
                cnt +=7;
                break;           
            case 'T': case 'U': case 'V':
                cnt +=8;
                break;
            case 'W': case 'X': case 'Y': case 'Z':
                cnt +=9;
                break;           
        }
    }

    printf("%d",cnt);
    return 0;
}