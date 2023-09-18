#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define TEXT  "string도 선언 가능."     // 심볼릭 상수
const char TEXT2[] = "이런 str도 선언 가능!";
int glbl = 12345;   // 전역변수

int main (void){
    // // printf 안에 여러 "" 들어갈 수 있다.
    // printf("h""e""l""l""o""\n");
    // printf(TEXT"\n");

    // // 이스케이프 시퀀스
    // printf("\' \" \? \\");
    // printf("\a \b \n");

    // // 서식지정자
    // printf("%c\n",'a');
    // printf("%s\n",TEXT);
    // printf("%d\n",-420000000);
    // printf("%i\n",-420000000);
    // long n1 = -420000200;
    // printf("%ld\n",n1);
    // long long n2 = -23245342532500000;
    // printf("%lld\n",n2);
    // printf("%u\n",420000000);
    // printf("%f\n",1.23456789);
    // printf("%.10f\n",1.23456789);
    // printf("%e\n",1.23456789);
    // printf("%E\n",1.23456789);
    // printf("%o\n",10);
    // printf("%x\n",1234);
    // printf("%X\n",1234);
    // printf("%d%%\n",100);

    // // type cast
    // int a = 3;
    // float b = 4;
    // prinft("%lf",(double)a/b);

    // // ternary operator
    // (10 > 5) ? printf("True!!\n") : printf("False!!\n");
    // // max값 구하는 코드
    // int a = 10, b = 7, c = 5;
    // int x = (a >= b) ? ((a >= c) ? a : c) : ((b >=c) ? b : c);
    // printf("%d",x)드



    // // 연산자 우선순위
    //========================
    // 1. 식, 후위
    // 2#. 단항연산자, 전위
    // 3. 곱하기
    // 4. 더하기
    // 5. 비트시프트

    // 6. 비교
    // 7. 등위

    // 8. 비트 &
    // 9. 비트 ^
    // 10. 비트 |

    // 11. 논리연산자 && ||
    // 12#. 삼항연산자 ? :

    // 13#. 대입연산자
    // 14. 콤마
    //========================    

    // // switch case
    // int score = 67;
    // switch (score / 10)
    // {
    // case 9 : printf("A\n");
    //     break;
    // case 8 : printf("B\n");
    //     break;
    // case 7 : printf("C\n");
    //     break;
    // case 6 : printf("D\n");
    //     break;
    // default: printf("F\n");
    //     break;
    // }

    // do while
    // int a = 0;
    // do{
    //     printf("%d\n",a++);
    // }while(a <= 10);

    // // void pointer
    // int num = 10;
    // void* pnum = &num;
    // // printf("%d",*(int*)pnum);
    // printf("%lu",sizeof(pnum));

    // // pointer array
    // int num1 = 1, num2 = 2, num3 = 3;
    // int* arr[3] = {&num1, &num2, &num3};
    // printf("%d",*(arr+2));

    // // summation program
    // int arr[6] = {10,20,30,40,50,60};
    // int sum = 0, *p = NULL;
    // for (p=arr; p<&arr[6]; p++){
    //     sum += *p;
    // }
    // printf("%d",sum);
    // return 0;

    // // array pointer
    // int arr[2][3]={
    //     {1,2,3},
    //     {4,5,6}
    // };
    // int (*parr1)[3] = arr;
    // // int (*parr2)[2][3] = arr;

    // printf("%d %d",**parr1,*(*(parr1+1)+2));


    // // "문자열은 포인터 상수이다"
    // printf("%p\n","father");

    // printf("%c\n",*"father");
    // printf("%c\n","father"[0]);

    // printf("%c\n",*("father"+1));
    // printf("%c\n","father"[1]);


    // // 동적 할당
    // int num=0, sum=0;
    // printf("num입력:");
    // scanf("%d",&num);
    // int* score = malloc(num*sizeof(num));

    // if (score == NULL){
    //     printf("할당 실패\n");
    //     exit(-1);
    // }

    // for (int i=0; i<num; i++){
    //     printf("%d번째 점수 입력:",i+1);
    //     scanf("%d",&score[i]);
    //     }

    // for (int i=0; i<num; i++){
    //     printf("%d번째 점수는 %d점입니다\n",i+1,score[i]); 
    // }
    // free(score);

    // 구조체

    // 정석
    // struct point2D {
    //     int a;
    //     int b;
    // };


    // struct point2D point1 = {3,4};          //순서대로 초기화
    // struct point2D point2 = {.b = 5};      //선택해서 초기화

    // 호출
    //  printf("%d %d\n", point1.a,point1.b);
    //  printf("%d %d\n", point2.a,point2.b);   

    // 선언과 동시에 초기화 + 이름부여
    // struct point2D {
    //     int a;
    //     int b;
    // }point1 = {3,4},point2 = {7,8};

    // typedef를 이용하여 간단하게 표현
    //정석
    // struct point2D {
    //     int a;
    //     int b;
    // };

    // typedef struct point2D p;

    //더 간단하게 별명 설정 + 본명 생략
    // typedef struct{
    //     int a;
    //     int b;
    // }p;

    // p p1={1,2};
    // p p2={3,4};

    // printf("%d %d\n", p1.a,p1.b);
    // printf("%d %d\n", p2.a,p2.b);

    
    // struct 배열 선언 (모든 자료형은 array 선언 가능하다)
    // typedef struct 
    // {
    //     int x; int y;
    // }P[];

    // P p = {{1,2}, {3,4}, {5,6}};

    // printf("%d %d\n", p[0].x,p[0].y);
    // printf("%d %d\n", p[1].x,p[1].y);
    // printf("%d %d\n", p[2].x,p[2].y);

  //   // 구조체의 크기와 바이트패딩
  //   typedef struct {
  //     char a;
  //     int b;
  //     double c;
  //   }structure;

  //   printf("실제 구조체 크기 = %d", sizeof(structure));   //16
  //   /*
  //   가장 큰 자료형인 double이 기준이 됨 
  //   char를 위해 8바이트 할당,1바이트사용, 남은 7바이트중 4바이트 int가 사용
  //   3바이트로는 double 표현 부족하니 한 단위 추가 
  //   >> 16바이트 / 3 패딩바이트
  //   */
    
  // // 열거체 enum
  // enum {
  //   Sun,Mon,Tue,Wed,Thur,Fri,Sat
  // };    //이름 설정해도되고 안해도되는듯 + 이제 Mon은 0과 동치 >> switch문에 사용가능해짐

  // int date = 0;
  // scanf("%d",&date);
  // int today = date%7;
  
  // switch (today){
  //   case(Mon):case(Tue):case(Wed):case(Thur):case(Fri):
  //   printf("평일 싫어\n");
  //   break;

  //   case(Sun):case(Sat):
  //   printf("주말 좋아~~~~\n");
  //   break;
    
  //   default:
  //   printf("잘못된 입력\n");
  //   break;
  // };


  // function >> 재귀함수로 피보나치 수열 구현하기

  // int fibonacci(int n){
  //   switch (n){
  //     case 1: 
  //       return 1;
  //       break;
  //     case 2:
  //       return 1;
  //       break;
  //     default:
  //       return (fibonacci(n-1)+fibonacci(n-2));
  //   }
  // //   if (n==1){
  // //     return 1;
  // //   }
  // //   else if (n==2){
  // //     return 1;
  // //   }
  // //   return (fibonacci(n-1)+fibonacci(n-2));
  // }

  // int main(void) {
  //   int n;
  //   scanf("%d",&n);
  //   printf("%d",fibonacci(n));
    
  // }



  // // 함수 미리 호출 + 포인터를 통해 영구 값 저장
  // int Plus_Ten(int *a);

  // int main(void) {
  //   int n, *ptr;
  //   ptr = &n;
  //   printf("10을 더할 숫자 입력\n");
  //   scanf("%d",&n);
  //   Plus_Ten(ptr);
  //   printf("더해진 n값은 %d입니다.\n",n);
  //   return 0;
  // }

  // int Plus_Ten(int *a){
  //   *a += 10;
  //   return *a;
  // }


  // // function pointer >> 함수 이름도 포인터상수임
  // void func1(void){
  //   printf("func 호출\n");
  // }


  // int main(void) {
  //   void (*p)() = func1;
  //   p();
  // }



  // // strlen 함수
  // int main(void) {
  //   printf("%d",strlen("Hello World"));
  //   return 0;
  // }

  //  // strcpy 함수
  // // 1. 그냥 배열로 선언
  // #include <stdio.h>
  // #include "string.h"

  // int main(void){
  //   char c1[] = "Hello", c2[] = "GoodBye";
  //   // "Hello\0e\0"
  //   //  01234567
  //   strcpy(c2,c1);
  //   printf("%s\n",c2);
  //   char *c3 = c2+4;
  //   printf("%s\n",c3);
  //   return 0;
  // }

  // //2. 포인터로 문자열 선언할 때 >> 공간할당과 포인터의 관계
  // #include <stdio.h>
  // #include "string.h"
  // #include "stdlib.h"

  //   int main(void){
  //     char *c1= "Hello", *c2 = "GoodBye";
  //     printf("%p %p\n",c1,c2);
  //     // c2 = malloc(20);  // 동적할당 해줘야만 cpy 됨... 그렇다면 포인터 선언은 공간할당이 안되는건가?
  //     // "Hello\0e\0"
  //     //  01234567
  //     strcpy(c2,c1);
  //     printf("%s\n",c2);
  //     printf("%p %p\n",c1,c2);
  //     // char *c3 = c2+6;
  //     // printf("%s\n",c3);
  //     return 0;
  //   }
  

  // // strcat 함수
  // #include <stdio.h>
  // #include "string.h"

  // int main(void){
  //   char c1[20] = "Hello", c2[] = "GoodBye";
  //   strcat(c1,c2);
  //   printf("%s\n",c1);         //helloGoodBye
  //   return 0;

  // }

  // // strncat 함수

  // #include <stdio.h>
  // #include "string.h"

  // int main(void){
  //   char c1[20] = "Hello", c2[] = "GoodBye";
  //   strncat(c1,c2,3);
  //   printf("%s\n",c1);       //HelloGoo
  //   return 0;

  
    return 0;
}



  /*  전처리기
  컴파일러
  어셈블러
  링커
  */