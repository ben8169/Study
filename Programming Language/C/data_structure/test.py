import random

for _ in range(10):
    print(*[random.randint(0,100) for i in range(3)])