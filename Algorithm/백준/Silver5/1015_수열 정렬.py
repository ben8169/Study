N = int(input())
lst = [0]*N
arr = list(map(int, input().split()))
cnt = 0
limit = max(arr)
for i in range(limit+1):
    for j in arr:
        if i == j:
            lst[arr.index(j)] = cnt
            cnt += 1
            print(lst)

print(*lst)
