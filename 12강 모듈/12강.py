# 실전문제
# 12-1 모듈 작성해보기

# my_math.py

# def add(lst):
#     print(sum(lst))
#     return


# def subtract(lst):
#     if len(lst) == 1:
#         print(lst[0])
#         return
#     elif len(lst) == 0:
#         print("null")
#         return
#     else:
#         lst[1:] = map(lambda x: -1*x, lst[1:])
#         print(list(lst))
#         print(sum(lst))
#         return


# def multiply(lst):
#     identity = 1
#     for i in lst:
#         identity *= i
#     print(identity)


# def divide(lst):
#     pivot = lst[0]
#     for i in lst[1:]:
#         pivot /= i
#     print(pivot)


import my_math as mm

while True:
    operator = input("연산자를 입력하세요[+ - * /]")
    if operator not in ['+', '-', '*', '/']:
        print("연산자 입력오류")
        continue

    num_list = list(map(int, input().split()))

    if operator == '+':

        # mm.add()
        # mm.subtract()
        # mm.multiply()
        # mm.divide()
