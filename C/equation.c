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
  struct equation eq[10];
  struct equation *p = &eq[10];
  int n;
  scanf("%d", &n);

  for (int i = 0; i < n; i++) {
    scanf("%d %d %d", &eq[i].a, &eq[i].b, &eq[i].c);
  }
  // for (p = eq; p < eq + n; p++) {
  //   root(p);
  //   printf("%p\n", p);
  // }
  // for (p = eq; p < eq + n; p++) {
  //   printf("a = %d, b = %d, c = %d, %s\n", p->a, p->b, p->c, p->det);
  // }
  
  for (int i = 0; i < n; i++) {
    root(p + i);
  }
  for (int i = 0; i < n; i++) {
    printf("a = %d, b = %d, c = %d, %s\n", eq[i].a, eq[i].b, eq[i].c,
           eq[i].det);
  }
  return 0;
}
