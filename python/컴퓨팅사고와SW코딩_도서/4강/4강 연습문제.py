##1 문자열 거꾸로 출력
# str = "teststring"
#1
# print(str[::-1])

##2
# for i in range(len(str)-1,-1,-1):
#     print(str[i],end='')
    
####3#### 불가능!! str은 인덱싱 불가넝
# for i in range(len(str)//2):
#     str[i] ,str[-i-1] = str[-i-1], str[i]
# print(str)


##3
# sentence = input("입력>>>>")
sentence = "3봄일이시오청나앞보정네오요"
# n = len(sentence)
# message = ''
# for i in range(n):
#     if i%2 == 0:
#         message += sentence[i]
#     else:
#         message += '*'
    
# print(message)

[print(sentence[n],end='') if n%2 == 0 else print('*',end='') for n in range(len(sentence))]


