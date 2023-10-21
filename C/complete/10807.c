#include <stdio.h>
#include <stdlib.h>

int main(void) {
  int N, v, cnt=0;
  scanf("%d",&N);
  int *ptr = (int*)malloc(sizeof(int)*N);

  for (int i=0; i<N;i++){
    int n=0;
    scanf("%d",&n);
    ptr[i]=n;
  };

  scanf("%d",&v);
  for (int i=0;i<N;i++){
    if (ptr[i] == v)
      cnt +=1;
  }

  printf("%d",cnt);
  return 0;
}