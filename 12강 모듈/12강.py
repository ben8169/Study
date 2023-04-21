# 실전문제
# 12-1 모듈 작성해보기

#my.math.py
def add(lst):
    print(sum(lst))
    return


def subtract(lst):
    if len(lst) == 1:
        print(lst[0])
        return
    elif len(lst) == 0:
        print("null")
        return
    else:
        lst[1:] = map(lambda x: -1*x, lst[1:])
        print(sum(lst))
        return


def multiply(lst):
    identity = 1
    for i in lst:
        identity *= i
    print(identity)


def divide(lst):
    pivot = lst[0]
    for i in lst[1:]:
        pivot /= i
    print(pivot)

#main.py
import my_math as mm

while True:
    operator = input("연산자를 입력하세요[+ - * /]")
    if operator not in ['+', '-', '*', '/']:
        print("연산자 입력오류")
        continue

    num_list = list(map(int, input("숫자 리스트를 띄어쓰기로 입력하세요").split()))
    if len(num_list) == 0:
        print('숫자가 입력되지 않았습니다. 다시 시작')
        continue

    if operator == '+':
        mm.add(num_list)
    elif operator == '-':
        mm.subtract(num_list)
    elif operator == '*':
        mm.multiply(num_list)
    elif operator == '/':
        mm.divide(num_list)

    print("="*30)

    if input("계속할까요?(Y/N)").lower() == 'n':
        print('종료')
        break
    else:
        print("="*30)
        
