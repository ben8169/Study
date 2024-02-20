import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    n = int(input())
    cnt = 0
    tbl = [0]*(n+1)
    tbl[0] = 0
    tbl[1] = 1
    tbl[2] = 2
    tbl[3] = 4
    for i in range(4, n+1):
        tbl[i] = tbl[i-1]+tbl[i-2]+tbl[i-3]

    print(tbl[n])
