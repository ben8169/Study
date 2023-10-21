# 실전문제
# 11-1 반복횟수, 색상, 각형 입력받아서 그리기
# sol1
import turtle as t

def ask_continue():
    question = t.textinput("반복", "반복하시겠습니까")
    return 1 if question.lower() == 'y' else 0

def choosing_color():
    color = t.textinput("색 선택", "펜 색깔을 선택하세요")
    return color

def choosing_angle():
    angle = t.numinput("각 선택", "몇각형을 그리실껀가요?")
    return int(angle)

def drawing(color, angle):
    t.pencolor(color)
    for i in range(angle):
        t.forward(50)
        t.right(360/angle)
    return


if __name__ == '__main__':
    t.speed(100)
    x = 1
    while x:
        input_color = choosing_color()
        input_angle = choosing_angle()
        t.penup()
        t.goto(-400, 400)
        t.pendown()
        drawing(input_color, input_angle)
        x = ask_continue()


# sol2
import turtle as t
import random

t.speed(100)
for i in range(3):
    for j in range(4):
        t.penup()
        t.goto(-300+200*j, 300-200*i)
        t.pendown()
        angle = random.randint(3, 20)
        for _ in range(angle):
            t.forward(40)
            t.right(360/angle)
t.exitonclick()

# 11-2 동아리 회원 json, email 검증까지
import json
import re

try:
    with open("path/to/save/json/club_member.json", "r", encoding="utf-8") as f:
        member_dic = json.load(f)
        print("json에서 불러옴.")

except:
    member_dic = {}
    print("json파일 없음. 새로 시작")

[print(i, member_dic[i], end="\n") for i in member_dic]


def matching(info_name, re_rule):
    while True:
        input_info = input(f"{info_name}을 입력하세요: ")
        if re.fullmatch(re_rule, input_info) == None:
            print(f"{info_name} 형식 오류")
        else:
            break
    return input_info


continue_alert = 'y'
while continue_alert == 'y':
    member_name = input("1.이름을 입력하세요: ")
    member_email = matching("이메일", "[A-z0-9]+@[A-z0-9]+\.[A-z.]+")
    member_phone = matching("전화번호", "[0-9]{2,3}-[0-9]{2,4}-[0-9]{4}")

    print(f"등록 완료. {member_name}/{member_email}/{member_phone}")

    confirm_alert = input("위 정보로 등록하시겠습니까?(Y/N)")
    if confirm_alert.lower() == 'y':
        member_dic[member_name] = [member_email, member_phone]
    else:
        print("내용을 파기하고 재등록을 시작합니다.")
        continue

    continue_alert = input("추가 등록 하시겠습니까?(Y/N) N 또는 아무 키를 눌러 종료하여 저장하십시오.")
    if continue_alert.lower() == 'y':
        continue
    else:
        break

with open("path/to/save/json/club_member.json", "w", encoding="utf-8") as f:
    json.dump(member_dic, f, indent=2, ensure_ascii=False)


# 11-3 lambda로 두 수식 비교하여 큰값, 작은값 구별하기

x1 = eval(input("첫번째 수식을 입력하세요:"))
x2 = eval(input("두번째 수식을 입력하세요:"))

print(f"큰 값은 {x1}, 작은 값은 {x2}") if x1>x2 else print(f"큰 값은 {x2}, 작은 값은 {x1}")
print(f"큰 값은 {max(x1,x2)}, 작은 값은 {min(x1,x2)}")


# lambda와 map 추가예제
lst = [1, 2, 3, 4, 10]
lst2 = [4, 6, 7, 8, 2]

new_lst = list(map(lambda x, y: x + y, lst, lst2))
print(new_lst)


#lambda와 filter 추가예
lst = [1, 2, 3, 4, 10]

new_lst = list(filter(lambda x: x < 10, lst))
print(new_lst)


# 11-4 동생과 내가 같이 저금하여 어버이날 선물 자금마련하기!
total_amount = 0


class making_money():
    def __init__(self):
        None

    def add(self, name, money):
        global total_amount
        self.name = name
        self.money = money
        print(f"{name} {money}원 저축합니다.")
        total_amount += money


dp = making_money()

while total_amount < 1000000:
    who = input("누가 저금했나요?(me,bro)")
    amount = int(input("얼마나 저금했나요?"))
    if who == 'me':
        dp.add('내가', amount)
    elif who == 'bro':
        dp.add("동생이", amount)
    else:
        print("잘못 입력하였습니다.")
    print("\n최종금액 %d" % total_amount)
print("완성!")

#연습문제

#1.리스트 내 최대,최소,평균값 출력
#sol1
import random
n = int(input("데이터셋 개수 입력"))
lst = [random.randint(-100, 100) for _ in range(n)]
print(lst)
print(f"최댓값 : {max(lst)}, 최솟값 : {min(lst)}, 평균 : {sum(lst)/n}")

# sol2
import random
n = int(input("데이터셋 개수 입력"))
lst = [random.randint(-100, 100) for _ in range(n)]
max_value, min_value = 0, 0
for i in lst:
    if i > max_value:
        max_value = i
    elif i < min_value:
        min_value = i
print(max_value, min_value)


#2.난수 리스트 생성 후 prime number로 필터링
import random
random.seed(13)
lst = [random.randint(0, 10000) for _ in range(100)]
is_prime = lambda num: num > 1 and all(num % i != 0 for i in range(2, num))

primes = list(filter(is_prime,lst))
print(primes)


#3. 변수의 유효범위

value = int(input('수를 입력하세요 '))

def add(num):
    num = num*2
    print("함수 안에서 값:", num)
    return num

print("함수 호출전:",value)
value = add(value)
print("함수 호출후:",value)
