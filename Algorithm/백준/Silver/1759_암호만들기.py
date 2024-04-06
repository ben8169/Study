## Sol1
# from itertools import combinations
# L, C = map(int, input().split())
# S = input().split()
# S.sort()

# vowels = ['a','e','i','o','u']

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


## Sol2
#모음 1개와 자음 2개를 선택한 후, 나머지는 자유롭게 선택하는 
#아이디어에서 착안

from itertools import combinations
L, C = map(int, input().split())
S = input().split()
S.sort()



vowels = ['a','e','i','o','u']
vowel_list = []
consonant_list = []
answer = []


for i in S:
    if i in vowels:
        vowel_list.append(i)
    else:
        consonant_list.append(i)


distribute = L-3
for i in range(0,distribute+1):
    v_list = list(combinations(vowel_list,1+i))
    c_list = list(combinations(consonant_list, 2+(distribute-i)))
    
    for v in v_list:
        for c in c_list:
            tmp = sorted(v+c)
            tmp_str = "".join(tmp) 
            answer.append(tmp_str)

answer.sort()

for i in answer:
    print(i)
