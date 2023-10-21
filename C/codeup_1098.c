#include <stdio.h>


int main(void){
    int w=0, h=0;
    scanf("%d %d",&h,&w);
    int arr[w][h];

    for (int i=0; i<w; i++){
        for (int j=0; j<h; j++){
            arr[i][j]=0;
        }
    }

    int (*s_pnt)[h] = arr;

    int n=0;
    scanf("%d",&n);

    for (int i=0; i<n;i++){
        int l=0,d=0,x=0,y=0;
        scanf("%d %d %d %d", &l,&d,&x,&y);
        
        // switch (d){
        //     case 0:
        //      for (int i=0; i<l; i++){
        //         *(*(s_pnt+x-1)+y-1+i) = 1;
        //         }
        //     break;

        //     case 1:

        //     break;
        // }

        if (d == 0){
            for (int i=0; i<l; i++){
                *(*(s_pnt+x-1)+y-1+i) = 1;
                }
        }
        else if (d == 1){
            for (int i=0; i<l; i++){
                *(*(s_pnt+x-1+i)+y-1) = 1;
            }        
        }
    }



    // 최종출력

    for (int i=0; i<w; i++){
        for (int j=0; j<h; j++){
            printf("%d  ",arr[i][j]);
        }
        printf("\n");
    }

    return 0;
}