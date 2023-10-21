# 0. 알파벳 노이즈 제거 > 공백구별 정수 더하거

# sol1
import numpy as np
import re
noised_list = input("알파벳 노이즈가 있는 문장을 입력하세요: ").split()
filtered_list = []

for i in noised_list:
    filtered_str = ""
    for j in i:
        if j in list(map(str, range(0, 10))):
            filtered_str += j
    filtered_list.append(filtered_str)

filtered_list = map(int, filtered_list)
print(sum(filtered_list))

# sol2

noised_list = input("알파벳 노이즈가 있는 문장을 입력하세요: ").split()
unjoined_list = []
filtered_list = []

for i in noised_list:
    x = re.findall(r'\d+', i)
    unjoined_list.append(x)
# print(unjoined_list)

for j in unjoined_list:
    j = "".join(j)
    filtered_list.append(j)
# print(filtered_list)

filtered_list = map(int, filtered_list)
print(sum(filtered_list))

# sol3
sentence = input("Noisy Sentence: ")
space = sentence.split()
num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
total = []
for i in range(len(space)):
    a = ''
    for n in space[i]:
        if n in num:
            a = a + n
    a = int(a)
    # print(a)
    total.append(a)
print(sum(total))


# 1. 0~24까지 정수를 출력하세요
# sol1
for i in range(25):
    print(i, end=' ')

# 2. 0~24까지 정수를 한줄에 5개씩 출력하세요
# sol1
for i in range(5):
    for j in range(5):
        print(i * 5 + j, end=' ')
    print()

# sol2
print(np.arange(25).reshape(5, 5))

# sol3 표준화
row_num = int(input("행의 개수를 입력하세요: "))
end_num = int(input("마지막 숫자를 입력하세요: "))

for i in range(end_num):
    print(i, end=' ')
    print('') if (i+1) % row_num == 0 else None

# sol4 표준화
row_num = int(input("행의 개수를 입력하세요: "))
end_num = int(input("마지막 숫자를 입력하세요: "))
[print(i) if (i+1) % row_num == 0 else print(i, end=' ')
 for i in range(end_num)]


# sol5
for i in range(0, 25, 5):
    for j in range(5):
        print(i+j, end=' ')
    print()

# sol6 표준화
row_num = int(input("행의 개수를 입력하세요: "))
end_num = int(input("마지막 숫자를 입력하세요: "))
for i in range(0, end_num, row_num):
    for j in range(row_num):
        if (i+j) == end_num:
            break
        print(i+j, end=' ')
    print()
