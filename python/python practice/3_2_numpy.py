import numpy as np

# a = np.zeros([5,5], dtype=np.int32)
# # print(a)
# # print(a.dtype)

# # print(np.ones(5))
# # print(np.full(10, -1).reshape(2, 5))



# # a[0,-1] = 1
# # print(a)

# # a = np.zeros([5,5], dtype=np.int32)
# # a[:,[0,-1]] = 1
# # a[[0,-1],:] = 1
# # print(a)

# a = np.zeros([5,5], dtype=np.int32)
# # a[1:-1,1:-1] = 2
# # print(a)

# ii = range(len(a))
# a[ii, ii] = 3
# a[ii, list(reversed(ii))] = 3       # 에러
# print(a)
# print('-' * 30)

# print(np.random.rand(3,4))
# print(np.random.choice(['a', 'b', 'c']))
# print(np.random.choice(range(10), 10, replace=False))


# b = sorted(set('weekend'))  
# b = np.array(b)
# print(b.dtype)


# c = np.array(['red', 'green', 'blue', 12])
# print(c, c.dtype)


# # 퀴즈
# # choice 함수를 사용해서 100보다 작은 양수 3행 4열 배열을 만드세요
np.random.seed(23)
d = np.random.choice(range(100), [3, 4])
print(d)

# print(np.sum(d))
# print(np.sum(d, axis=0))    # 수직(열)
# print(np.sum(d, axis=1))    # 수평(행)


# print(np.max(d))
# print(np.max(d, axis=0))
# print(np.max(d, axis=1))


# c = d
# while np.sum(c) > 0:
#     idx = int(np.argmax(c))
#     div = c.shape[1]
#     c[idx//div, idx%div] = 0
#     print(c)
# print(np.argmax(d, axis=0))
# print(np.argmax(d, axis=1))


e = d.reshape(-1)   
print(e)

# 퀴즈
# argsort 함수를 이용해서 정렬된 배열을 만드세요
e.sort()
print(e)
f = e.argsort()
print(f)
print(e[f])     #== e.sort()