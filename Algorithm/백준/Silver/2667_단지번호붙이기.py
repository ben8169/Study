import sys
sys.setrecursionlimit(100000)

N = int(input())
lst = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    tmp = input()
    for j in range(len(tmp)):
        lst[i][j] = int(tmp[j])

def DFS(x, y):
    if x<0 or y<0 or x>=N or y>=N:
        return False
    if lst[x][y] == 1:
        global cnt
        lst[x][y] = 0
        cnt += 1
        DFS(x+1,y)
        DFS(x-1,y)
        DFS(x,y+1)
        DFS(x,y-1)
        return True
    return False



cnt = 0
complex_num = 0
answer = []
for i in range(N):
    for j in range(N):
        if DFS(i,j) == True:
            answer.append(cnt)
            complex_num +=1 
            cnt = 0

print(complex_num)
[print(i) for i in sorted(answer)]


