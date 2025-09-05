#include <stdio.h>

int main(void){
	int num=0;
	char s1[100];
	FILE* fp = fopen("number.txt","r+");
	//fscanf(fp, "%d", &num);
	//printf("%d\n",num);
	
	//fprintf(fp, "%d", num);
	fscanf(fp,"%s",s1);
	fscanf(fp,"%d",&num);
	printf("%s\n",s1);
	printf("%d\n",num);



	fclose(fp);

	return 0;
}
