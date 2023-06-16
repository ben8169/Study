from collections import Counter



n = int(input())

for _ in range(n):
    a, *lst = map(int, input().split())
    cnt = Counter(lst)
    if (cnt.most_common(1)[0][1]) > (a/2):
        print(cnt.most_common(1)[0][0])
    else:
        print('SYJKGW')

