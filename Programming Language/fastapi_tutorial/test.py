def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# 제너레이터 객체 생성
fib_gen = fibonacci_generator()

# 처음 10개의 피보나치 수열 값 출력
for _ in range(10):
    print(next(fib_gen))
