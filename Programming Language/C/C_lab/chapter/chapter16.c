#include <stdio.h>

int main(void){
//	int numTest;
//	float stTest, avg, total = 0.0;
//	
//	for (numTest=0; numTest<25; numTest++){
//		printf("Score of the student?\n");
//		scanf(" %f", &stTest);
//		if (stTest<0.0){
//			break;
//		}
//		total += stTest;
//}    
//
//avg = total/numTest;
//printf("avg = %.1f\n", avg);



//	int i;
//	for (i=0; i<10; i++){
//		printf(i%2!=0 ? "odd number\n" : "even number\n");
//	}


// lab
	int iter;
	double product=1, input_num=0;
	printf("input iter\n");
	scanf("%d",&iter);
	for (int i =0; i<iter; i++){
		printf("%dth number:\n",i+1);
		scanf(" %lf", &input_num);
		if (input_num <0){
			break;
		} else if (input_num == 0){
			continue;
		} else {
			product *= input_num;
		}
	}
	printf("calculated sum: %.2lf", product);	




    return 0;
}




