#include <stdio.h>

int main (void){
    int r,g,b, cnt=0;
    scanf("%d %d %d",&r, &g, &b);
    for (int i=0;i<r;i++){
        for (int j=0;j<g;j++){
            for (int k=0;k<b;k++){
                printf("%d %d %d\n",i,j,k);
                cnt++;
            }
        }
    }
    printf("%d",cnt);
    return 0;
}

// #include <stdio.h>

// int main (void){
//     unsigned char r, g, b; // unsigned char로 변경
//     int cnt=0;
//     scanf("%hhu %hhu %hhu", &r, &g, &b); // %hhu를 사용하여 unsigned char 입력 받기
//     for (unsigned char i=0; i<r; i++){ // unsigned char로 변경
//         for (unsigned char j=0; j<g; j++){ // unsigned char로 변경
//             for (unsigned char k=0; k<b; k++){ // unsigned char로 변경
//                 printf("%d %d %d\n", i, j, k); // 출력은 여전히 int 형식으로
//                 cnt++;
//             }
//         }
//     }
//     printf("%d", cnt);
//     return 0;
}
