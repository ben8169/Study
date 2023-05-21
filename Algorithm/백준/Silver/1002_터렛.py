import math


def circle(x1, y1, r1, x2, y2, r2):
    center_distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    if center_distance == 0 and r1 == r2:
        return -1
    elif center_distance == r1 + r2 or center_distance == abs(r1-r2):
        return 1
    elif center_distance > r1 + r2 or center_distance < abs(r1-r2):
        return 0
    else:
        return 2


T = int(input())
lst = []
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    lst.append(circle(x1, y1, r1, x2, y2, r2))

print(*lst, sep='\n')
