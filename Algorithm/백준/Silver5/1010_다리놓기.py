#sol1
T= int(input())
answer_list = []


def factorial(n):
    x = 1
    for i in range(n,0,-1):
        x *= i
    return x


def Combination(a, b):
    p = factorial(b)
    q = factorial(a)*factorial(b-a)
    return p/q


    
for _ in range(T):
    m, n = map(int, input().split())
    answer_list.append(Combination(m, n))


[print(int(i)) for i in answer_list]

#sol2
import math

def combination(n, r):
    return math.factorial(n) // (math.factorial(r) * math.factorial(n-r))

T = int(input())
lst = [0]*T
for i in range(T):
    N, M = map(int, input().split())
    lst[i] = combination(M, N)

[print(i) for i in lst]
