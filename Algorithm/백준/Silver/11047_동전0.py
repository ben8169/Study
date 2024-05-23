import sys
input = sys.stdin.readline


lst = input().split()
N = int(lst[0])
K = int(lst[1])


coins = []
cnt = 0

for _ in range(N):
    coin = int(input())
    if coin<=K : coins.append(coin) 
    

while coins:
    value = coins.pop()
    tmp=0
    while K>=value:
        tmp = K//value
        K = K%value
        cnt += tmp
print(cnt)