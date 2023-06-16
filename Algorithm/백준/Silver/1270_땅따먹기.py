from collections import Counter



n = int(input())

for _ in range(n):
    _, *lst = map(int, input().split())
    cnt = Counter(lst)
    print(cnt.most_common(1)[0][0])
