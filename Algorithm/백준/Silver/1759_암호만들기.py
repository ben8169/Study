from itertools import combinations
L, C = list(map(int, input().split()))
S = input().split()
S.sort()


vowels = ['a','e','i','o','u']

# def check(s):
#     vowel_num = 0; consonant_num = 0
#     for ch in s:
#         if ch in vowels:
#             vowel_num += 1
#         else:
#             consonant_num +=1

#     if vowel_num >=1 and consonant_num >= 2:
#         return s
#     else:
#         return False




# for i in combinations(S,L):
#     i_checked = check(i)
#     if i_checked:
#         print(''.join(i_checked))




