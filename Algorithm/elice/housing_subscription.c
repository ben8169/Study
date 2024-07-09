#include <stdio.h>

int main(void) {
    int table[3][4] = {
        {300, 600, 1000, 1500},
        {250, 400, 700, 1000},
        {200, 300, 400, 500}
    };
    
    int N, area, residence, payment, cnt = 0;
    scanf("%d", &N);
    
    for (int i = 0; i < N; i++) {
        scanf("%d %d %d", &area, &residence, &payment);
        residence--;
        
        if (area <= 85) {
            area = 0;
        } else if (area <= 102) {
            area = 1;
        } else if (area <= 135) {
            area = 2;
        } else {
            area = 3;
        }
        
        int answer = table[residence][area];
        if (answer <= payment) {
            cnt++;
        }
    }
    
    printf("%d\n", cnt);
    return 0;
}

