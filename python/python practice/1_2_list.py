# 1. 0~99 사이의 정수 난수 10개로 이루어진 리스트 생성
import random
random.seed(23)

# sol1
a = []
for _ in range(10):
    a.append(random.randrange(100))
print(a)

# sol2
b = [0] * 10
for i in range(10):
    b[i] = random.randrange(100)
print(b)

# sol3
c = [random.randrange(100) for _ in range(10)]
print(c)

# 2. 1차원 리스트 거꾸로 뒤집기
lst = [99, 37, 10, 2, 75, 39, 54, 48, 67, 45]

# sol1
for i in range(5):
    lst[i], lst[-1-i] = lst[-1-i], lst[i]
print(lst)

# sol2
lst.reverse()
print(lst)

# sol3
print(lst[::-1])

# sol4
[print(lst[-1-i], end=',') for i in range(10)]

# sol5
print(list(reversed(lst)))
