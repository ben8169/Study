import numpy as np

lst = [1,2,3]
print(list((map(lambda x:x/sum(lst), lst))))