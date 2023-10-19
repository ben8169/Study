#include <stdio.h>

int main(void){
	char *stuff1 = "TV", *stuff2 = "Tablet", *stuff3 = "shaver";
	double stuff1_price = 1320., stuff2_price = 299., stuff3_price = 129.;
	int stuff1_ea = 3, stuff2_ea = 2, stuff3_ea = 5;


	printf("%s = %dea, %s = %dea, %s = %dea\n", stuff1,stuff1_ea,stuff2,stuff2_ea,stuff3,stuff3_ea);
	printf("Total amount = %.2lf", stuff1_ea * stuff1_price+stuff2_ea * stuff2_price+stuff3_ea * stuff3_price);
	return 0;
}


