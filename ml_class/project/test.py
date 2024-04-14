import numpy as np


x = np.array([1,2,3,4,-5,-6])

y = ['p' if i>0 else 'n' for i in x]
print(y)