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
        
#12-2 matplotlib 사용하기 
import matplotlib.pyplot as plt
def sorting(list):
    while True:
        ascend_or_descend = int(input("1.오름차순 2.내림차순 숫자를 입력하세요."))
        if ascend_or_descend == 1:
            list.sort()
            return list
        elif ascend_or_descend == 2:
            list.sort(reverse=True)
            return list
        else:
            print("잘못 입력하셨습니다.")

def axis(list):
    while True:
        axis = int(input("1.세로 막대그래프 2.가로 막대그래프 숫자를 입력하세요."))
        if axis == 1:
            plt.bar(range(1,len(list)+1),list)
        elif axis == 2:
            plt.barh(range(1,len(list)+1),list)
        else:
            print("잘못 입력하셨습니다.")
            continue
        plt.show()
        return

num_list = list(map(int,input("숫자 리스트 입력 : ").split()))
sorted_list = sorting(num_list)
axis(sorted_list)

       
        
