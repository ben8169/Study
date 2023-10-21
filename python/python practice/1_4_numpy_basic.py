import numpy as np

a = np.arange(6)
print(a)
print(type(a))              # <class 'numpy.ndarray'>
print(a.shape, a.dtype)     # (6,) int32

# ----------------------------------------------
print(a[0], a[-1])  # indexing 가능
print(a[0:3], a[:3])  # slicing 가능
# ----------------------------------------------
print(a+1)  # broadcasting
print(a+a)  # vector
print(np.sin(a))  # universal function
print(np.sum(a))  # sum
# ----------------------------------------------

b = np.arange(6)

c = b.reshape(2, 3)
c = b.reshape(2, -1)
c = b.reshape(-1, 3)

b[3] = 99
print(b)
print(c)  # b의 값이 바뀌면 c의 값도 바뀜
print(c.shape, c.dtype)     # (2, 3) int32

print(c + 1)                # broadcast
print(c + c)                # vector
print(np.sin(c))            # universal function

# ----------------------------------------------

d = np.random.randint(0, 100, 12, dtype=np.int64).reshape(3, 4)
print(d)
print(d.dtype)

# 2차원 배열을 1차원으로 변환하는 방법
print(d.reshape(12))
print(d.reshape(d.size))
print(d.reshape(d.shape[0]*d.shape[1]))
print(d.reshape(-1))


a = np.arange(3)        # [0 1 2]
b = np.arange(6)        # [0 1 2 3 4 5]
c = np.arange(3).reshape(1, 3)    # [[0 1 2]]
d = np.arange(3).reshape(3, 1)  # [[0] [1] [2]]
e = np.arange(6).reshape(2, 3)  # [[0 1 2] [3 4 5]]

print(a + b)        # 에러
print(a + c)
print(a + d.reshape(-1))  # 스칼라화
print(a + d)
print(a + e)

# --broadcasting rule--
# 뒤에서부터 대응하는 축의 크기가 1.1이거나, 2.동일하거나 3.아예 없거나
# 축의 큰 것을 따라감
arr1 = np.arange(15).reshape(3, 1, 5)
arr2 = np.arange(20).reshape(4, 5)
print(arr1, arr2, arr1+arr2, sep='\n')  # (3, 4, 5)

np.random.seed(23)
f = np.random.randint(0, 100, 12)
print(f)

g = (f >= 50)       # boolean indexing
print(f[g])         # filtering

h = np.reshape(f, [3, 4])
print(h)
print(h[-1], h[-1][-1], h[-1, -1], sep='\n')           # fancy indexing


# 2차원 배열에서 마지막 열만 출력하기
print(h[:, -1])
[print(h[i, -1]) for i in range(3)]

# 2차원 배열을 거꾸로 출력하기
print(h[::-1], end='\n')      # == print(h[::-1,:],end='\n')
print(h[:, ::-1], end='\n')
print(h[::-1, ::-1], end='\n')
