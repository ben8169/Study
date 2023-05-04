# 1. 0~24까지 정수를 출력하세요
# sol1
# for i in range(25):
#     print(i, end=' ')

# 2. 0~24까지 정수를 한줄에 5개씩 출력하세요
# sol1
for i in range(5):
    for j in range(5):
        print(i * 5 + j, end=' ')
