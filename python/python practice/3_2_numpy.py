import numpy as np

a = np.zeros([5,5], dtype=np.int32)
# print(a)
# print(a.dtype)

# print(np.ones(5))
# print(np.full(10, -1).reshape(2, 5))



# a[0,-1] = 1
# print(a)

# a = np.zeros([5,5], dtype=np.int32)
# a[:,[0,-1]] = 1
# a[[0,-1],:] = 1
# print(a)

a = np.zeros([5,5], dtype=np.int32)
# a[1:-1,1:-1] = 2
# print(a)

ii = range(len(a))
a[ii, ii] = 3
# a[ii, list(reversed(ii))] = 3       # 에러
print(a)
print('-' * 30)
