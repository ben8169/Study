#include <stdio.h>

int main()
{
// 	// 1. 이런 식이면 어떻게든 arr길이는 i로 알게 된다. 왜? 인덱스가 꼭 필요하거든
//   static int arr[] = {}; // int *arr = NULL


//   int i = 0, n =0 ;
//   while(1){
//     scanf("%d",&n);
//     if (n == -3)
//       break;
//     *(arr+i) = n;
//     i++;
//   }

//   printf("[");
//   for (int j=0; j<i; j++){
//   	printf("%d ",arr[j]);
//   }
//    printf("]");
//   return 0;


	// 2. 동적할당도 똑같은데? 결국 malloc 할 만큼의 i 를 알고 있다는 가정하에 모든 할당이 이뤄지니깐요

}


/*
	포인터로 선언한 배열의 크기 구하는 프로그램 짜기
	1. 내생각대로
	2. https://blog.naver.com/tipsware/221250121797 참고
	
*/
