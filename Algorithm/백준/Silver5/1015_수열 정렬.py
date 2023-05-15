#sol1
N = int(input())
lst = [0]*N
arr = list(map(int, input().split()))
cnt = 0
limit = max(arr)
for i in range(limit+1):
    for j in arr:
        if i == j:
            lst[arr.index(j)] = cnt
            arr[arr.index(j)] = -1
            cnt += 1

print(*lst)

#sol2
import sys
N = int(sys.stdin.readline())
lst = [0]*N
arr = list(map(int, sys.stdin.readline().split()))
s=sorted(arr,key=int)
for i in arr:print(x:=s.index(i));s[x]=-1