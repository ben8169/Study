# import random

# a0 = [random.randrange(100) for _ in range(10)]
# a1 = [random.randrange(100) for _ in range(10)]
# a2 = [random.randrange(100) for _ in range(10)]

# a = [a0, a1, a2]
# print(a)

# b = [j for i in a for j in i]
# print(b)

# print(max([max(i) for i in a]))


# # [i.remove(j) for i in a for j in i if j % 2 == 0]
# # print(a)

# print([[j for j in i if j % 2] for i in a])


# # 1~10000 사이에 포함된 8의 갯수를 구하세요
# cnt = 0
# for i in range(1, 10001):
#     cnt += str(i).count('8')
# print(cnt)


# print(str(list(range(10000))).count('8'))

##str(lst) # Output: '[1, 2, 3]'
## map(str, lst)  # Output: ['1', '2', '3']
