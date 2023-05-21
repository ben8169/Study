def finding_next(x, y):
    global cabbage
    if (x + 1, y) in cabbage:
        cabbage.remove((x + 1, y))
        finding_next(x + 1, y)
    if (x, y + 1) in cabbage:
        cabbage.remove((x, y + 1))
        finding_next(x, y + 1)
    if (x - 1, y) in cabbage:
        cabbage.remove((x - 1, y))
        finding_next(x - 1, y)
    if (x, y - 1) in cabbage:
        cabbage.remove((x, y - 1))
        finding_next(x, y - 1)
    else:
        return

import sys
sys.setrecursionlimit(100000)

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    cabbage = []
    cnt = 0
    for _ in range(K):
        cabbage.append(tuple(map(int, input().split())))

    while cabbage:
        x, y = cabbage.pop(0)
        cnt += 1
        finding_next(x, y)
    else:
        print(cnt)

