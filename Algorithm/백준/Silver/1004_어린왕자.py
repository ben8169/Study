import math

x1, y1, x2, y2 = 0, 0, 0, 0

def is_in(x, y, r):
    des1, des2 = 0, 0
    des1 = math.sqrt((x-x1)**2 + (y-y1)**2)
    des2 = math.sqrt((x-x2)**2 + (y-y2)**2)

    if des1 < r:
        des1 = 0       #in
    elif des1 > r:
        des1 = 1       #out
    
    if des2 < r:
        des2 = 0       #in
    elif des2 > r:
        des2 = 1       #out
    if des1 == des2:
        return 0
    elif des1 != des2:
        return 1
    


T = int(input())

for _ in range(T):
    cnt = 0
    x1, y1, x2, y2 = map(int,input().split())
    iter = int(input())
    for _ in range(iter):
        x, y, r = map(int,input().split())
        cnt += is_in(x, y, r)
    print(cnt)