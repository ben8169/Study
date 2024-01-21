#include <stdio.h>
#include <string.h>



int main(void){
    char str[1000000];
    fgets(str,1000000,stdin);
    // puts(str);
    
    char *pivot = str;
  
    while (*(pivot) == ' '){
        pivot += 1;
    }
    // printf("pivot before start:%p\n",pivot);

    int cnt = 0;
    while (*(pivot) != '\n'){
        // printf("current pivot:%c\n",*pivot);
        if (*(pivot) != ' '){
            pivot += 1;
            // printf("pivot added:%c\n",*pivot);
        }else if (*(pivot) == ' '){
            if (*(pivot+1) == '\n'){
                break;
                }
                pivot +=1;
                cnt +=1;
                // printf("cnt added:%d\n",cnt);
        }
    }
    printf("%d",cnt+1);



    return 0;
}