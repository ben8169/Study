//Tip - If you don't initialize the values, those
automatically initialized by 0.
1. basic declaration

#include <stdio.h>

struct p2D{
	int x;
	int y;
};

int main(void){
//1
	struct p2D point = {5,4};
//2
//	struct p2D point;
//	point.x = 5;
//	point.y = 4;

//3
//	struct p2D p4 = {.x=7,.y=8};
	
//4
//	struct p2D p5 = {.y=8}; //x=0


	printf("%d, %d", point.x, point.y);
	return 0;
}



2. declaration simultaneously

struct p2D{
	int x;
	int y;
}p1,p2,p3;


//even..
struct p2D{
     int x;
     int y;
}
p1={1,2},
p2={3,4},
p3={5,6};



3.typedef

//typedef int jungsoo;
typedef struct p2D{
	int x;
	int y;
}point;

int main(void){
	point p1 = {5,4};
	struct p2D p2 = {4,5}:
	}


4. Array

typedef struct{
	int x;
	int y;
}point;

int main(void){
	point pgroup[3] = {
		{1,2},
		{3,4},
		{5,6}
	};
}


5. Pointer
	typedef...

	point p1 = {3,5};
	point* ptr1 = &p1;

	printf("%d, (*ptr).x);	// == p1.x
	printf("%d, ptr->x);
 







