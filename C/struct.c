#include <stdio.h>

typedef struct{
	char first[10];
	char last[20];
}name;


typedef struct{
	name student_name;
	int grade;
}student;



int main(void){
	student kim = {{"kim","jiheon"}, 1};
	student *ptr = &kim;
//	name *n_ptr = &(ptr->student_name);
	name *n_ptr = &((&kim)->student_name);
//	printf("%s %s %d\n",ptr->student_name.first,ptr->student_name.last, ptr->grade);
	printf("%s %s %d\n",n_ptr->first,n_ptr->last, ptr->grade);
	return 0;
}

