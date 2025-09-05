#include <stdio.h>

typedef struct{
	char first[20];
	char last[20];
}name;

typedef struct{
	name student_name;
	int grade;
}student;

int main(void){
	student kim = {.student_name.first="jiheon", .student_name.last="kim", .grade = 3};
//	student kim = {.grade = 3, .student_name = {.first = "jiheon"}};

	

	printf("%s",kim.student_name.first);
	
	return 0;
}

