import sys

def fibonacci(n):
    global cnt0, cnt1
    if n == 0:
        cnt0 += 1
        return 
    elif n == 1:
        cnt1 += 1
        return
    else:
        return fibonacci(n-2) , fibonacci(n-1)
    

T = int(sys.stdin.readline())

for _ in range(T):
    cnt0, cnt1 = 0, 0
    fibonacci(int(sys.stdin.readline()))
    print(cnt0, cnt1)
