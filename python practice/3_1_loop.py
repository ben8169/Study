# 아래 모양대로 출력하세요

#   0123
# 0 *---
# 1 **--
# 2 ***-
# 3 ****

# sol1
# for i in range(1, 5):
#     print('*'*i+'-'*(4-i))

# sol2
# for i in range(4):
#     for j in range(4):
#         if i >= j:
#             print('*', end='')
#         else:
#             print('-', end='')
#     print()

# sol3
# str = '----'
# for i in range(4):
#     print(str.replace('-', '*', i+1))
