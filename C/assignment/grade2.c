// 2022313356 김지헌
#include <stdio.h>

int InputScore(void);
char GetGrade(int score1, int score2, int score3);

int main(void){
    for (int student_num=1; student_num<=5; student_num++){
        printf("%d번째 학생의 점수 입력\n",student_num);

        int score1=-1, score2=-1, score3=-1;

        do{
            score1 = InputScore();
        }while (score1<0 || score1>100);

        do{
            score2 = InputScore();
        }while (score2<0 || score2>100);

        do{
            score3 = InputScore();
        }while (score3<0 || score3>100);

        printf("%d번째 학생의 학점은 %c\n\n", student_num,GetGrade(score1, score2, score3));
    }
    return 0;
}

int InputScore(void){
    int score=0;
    printf("점수 입력:");
    scanf("%d", &score);
    return score;
}


char GetGrade(int score1, int score2, int score3){
    int average = (score1 + score2 + score3) / 3;
    if (average >= 90){
        return 'A';
    }
    else if (average >= 80){
        return 'B';
    }
    else if (average >= 70){
        return 'C';
    }
    else if (average >= 60){
        return 'D';
    }
    else{
        return 'F';
    }

}