#1.코드 수정하기
x, y = 10, 20

age = int(input("나이 입력"))
retire = 65 - age
print("정년까지", retire, '남았습니다')

value = int('10101',2)
print("%d"%value)


real_num = 2.42e-4
print(real_num)


#2. 무한의 방 이름넣기
name_dic = {}

def recursion(n):
    global name_dic
    if n  == -1:
        return
    name_dic[n+1] = name_dic[n]
    n -= 1
    recursion(n)
    return
n = 0
name_dic[0] = "최초"

while True:
    recursion(n)
    name_dic[0] = input("추가 이름 입력")
    n+=1
    print(name_dic)


#3. 