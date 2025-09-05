#include <stdio.h>

//enum Days {MON,TUE, WED, THU, FRI, SAT, SUN};
typedef enum Days {MON=10,TUE=20, WED, THU, FRI=30, SAT, SUN}nickday;

int main(void){
	enum Days today = SAT;
//	nickday today = SAT;
	printf("%d\n",today);

	today = MON;

	switch (today){
		case(MON): case(TUE): case(WED):
			printf("BOO\n");
			break;
		default:
			printf("GOOD.\n");
			break;
		}

	return 0;
	}
	
