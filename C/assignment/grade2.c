// 2022313356 김지헌
#include <stdio.h>

int InputScore(void);
char GetGrade(int score1, int score2, int score3);

int main(void){
    int score1, score2, score3;
    score1 = InputScore();
    score2 = InputScore();
    score3 = InputScore();
    printf("학점은 %c", GetGrade(score1, score2, score3));
    return 0;
}

int InputScore(void){
    int score=0;
    while (score>=0 && score <=100){
        printf("점수 입력:");
        scanf("%d", &score);
        if (score >= 0 && score <= 100)
            return score;
        else
            printf("잘못된 입력입니다.");
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