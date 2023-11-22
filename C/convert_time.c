#include <stdio.h>

void ConvertTimeToHMS(int time, int* hour, int* min, int* sec);

int main (void){
    int time, hour, min, sec;
    int* p_hour = &hour, *p_min = &min, *p_sec = &sec;
    printf("시간 입력:");
    scanf("%d",&time);
    ConvertTimeToHMS(time, p_hour, p_min, p_sec);
    printf("%d시 %d분 %d초",hour,min,sec);
    return 0;
}


void ConvertTimeToHMS(int time, int* hour, int* min, int* sec){
    *hour = time / 3600;
    *min = (time % 3600) / 60;
    *sec = time - (*hour)*3600 - (*min)*60;
}