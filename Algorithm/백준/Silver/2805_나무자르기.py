import sys
input = sys.stdin.readline

N, M = map(int, input().split())
trees = list(map(int, input().split()))
trees.sort()

start = 0
end = trees[-1]

while start <= end:
    mid = (start + end) // 2
    sum = 0
    
    for tree in trees:
        if tree > mid:
            sum += tree - mid
        
    if sum >= M:
        result = mid
        start = mid + 1

    else:
        end = mid - 1

print(result)

