#include "string.h"
#include <stdio.h>
struct equation {
  int a;
  int b;
  int c;
  char det[7];
};

void root(struct equation *p) {
  if (p->b * p->b - 4 * p->a * p->c > 0)
    strcpy(p->det, "real");
  else if (p->b * p->b - 4 * p->a * p->c == 0)
    strcpy(p->det, "same");
  else
    strcpy(p->det, "complex");
}

int main(void) {
  struct equation eq[100];
  struct equation *p = &eq[0]; 
  /* p는 eq라는 리스트 중 한 덩어리의 struct 를 가리킴 --> 그런데 (p = eq; p < eq + n; p++)로 연산할 때는 위치는 상관없으나, (int i = 0; i < n; i++)로 연산하려 할 경우 p가 eq[0]을 가리키게 하는 초기항이 없으므로 처음부터 p가 eq[0]을 가리켜야 함 
  */

  int n;
  scanf("%d",&n);

  for (int i = 0; i < n; i++) {
    scanf("%d %d %d", &eq[i].a, &eq[i].b, &eq[i].c);
  }

  // // 1. p로 연산
  // // p연산시에 n을 단순 반복횟수로 해도 괜춘(ptr연산이므로 알아서 struct size만큼 커짐)
  // for (p = eq; p < eq + n; p++) {
  //   root(p);
  // }
  // for (p = eq; p < eq + n; p++) {
  //   printf("a = %d, b = %d, c = %d, %s\n", p->a, p->b, p->c, p->det);
  // }
  
  //2. i로 연산
  for (int i = 0; i < n; i++) {
    root(p + i);
  }
  for (int i = 0; i < n; i++) {
    printf("a = %d, b = %d, c = %d, %s\n", (p+i)->a, p[i].b, p[i].c,p[i].det);
  }
  return 0;

}