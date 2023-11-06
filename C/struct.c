#include <stdio.h>

typedef struct{
	char first[10];
	char last[20];
}name;


typedef struct{
	name student_name;
	int grade;
}student;

typedef struct{
	int a : 31;
	int b : 1;
	int c : 1;
}s1;

typedef struct{
	int a;
	int b;
	int c;
}s2;


int main(void){
//  // struct reference
// 	student kim = {{"kim","jiheon"}, 1};
// 	student *ptr = &kim;
// //	name *n_ptr = &(ptr->student_name);
// 	name *n_ptr = &((&kim)->student_name);
// //	printf("%s %s %d\n",ptr->student_name.first,ptr->student_name.last, ptr->grade);
// 	printf("%s %s %d\n",n_ptr->first,n_ptr->last, ptr->grade);
// 	return 0;

// //struct size
// printf("%d\n",sizeof(s1));
// printf("%d\n",sizeof(s2));

	enum Days {MON,TUE,WED};
	typedef enum Days hi;
	enum Days day = 3;
	hi day2 = TUE;
	// printf("%d",day);
	printf("%d",day2);

	switch (day2)
	{
	case (MON):
		printf("%d",MON);
		break;
	case (TUE):
		printf("%d",TUE);
		break;
	case (WED):
		printf("%d",WED);
		break;
	default:
		break;
	}
	
	return 0;
}
