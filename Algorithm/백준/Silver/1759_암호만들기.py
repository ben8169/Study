from itertools import combinations
L, C = map(int, input().split())
S = input().split()
S.sort()

vowels = ['a','e','i','o','u']

def check(s):
    vowel_num = 0; consonant_num = 0
    for ch in s:
        if ch in vowels:
            vowel_num += 1
        else:
            consonant_num +=1

    if vowel_num >=1 and consonant_num >= 2:
        return s
    else:
        return False




for i in combinations(S,L):
    i_checked = check(i)
    if i_checked:
        print(''.join(i_checked))


# n = C-L+1
# for i in range(n):
#     for j in range(i+1,n+1):
#         for k in range(j+1,n+2):
#             for l in range(k+1,n+3):
#                 print(S[i]+S[j]+S[k]+S[l])

