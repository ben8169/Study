#묵찌빠 만들어보기
# com = 0, player = 1
import random
from time import sleep

option = ['가위','바위','보']

def evaluate_winner(a,b):
    if a == b:
        return -1
    elif (a,b) in (("가위","보"),("바위","가위"),("보","바위")):
        return 0
    elif (a,b) in (("가위","바위"),("바위","보"),("보","가위")):
        return 1
    
while True:
    player_input = input("무엇을 낼까요? (가위, 바위, 보)")
    for i in range(3):
        print(f"묵찌빠를 시작합니다! {option[i]}!! ")
        sleep(1)
        turn = ''
    while True:
        print(f"나는..{player_input}!!")
        computer_input = option[random.randint(0,2)]
        print(f"컴퓨터는 {computer_input}을 선택했습니다!!")

        result = evaluate_winner(computer_input,player_input)
        
        if result == -1:
            break
        elif result == 0:
            turn = '컴퓨터' ; inputed = computer_input
        elif result == 1:
            turn = '당신'; inputed = player_input

        if inputed == '가위':
            inputed = '찌'
        elif inputed == '바위':
            inputed = '묵'
        elif inputed == '보':
            inputed = '빠'

        player_input = input("무엇을 낼까요? (가위, 바위, 보)")

        for n in range(3,0,-1):
            print(f"({turn} 차례){inputed}에 {inputed}에..({n})")
            sleep(1)
    if turn == '':
        print("무승부입니다! 다시 시작")
        continue
    else:
        print(f"{turn} 승리!")
        break
        
        
 
-# 1 수축기, 이완기 혈압으로 고혈압, 저혈압 판정하기
# systolic, diastolic = [int(input(f"{i}기 혈압을 입력하세요. (높은 쪽이 수축기)")) for i in ['수축','이완']]

# class pressure_evaluate():
#     def systolic_evaluation(self,n):
#         if n >= 140:
#             return 1
#         elif n >= 120 and n < 140:
#             return 0
#         else:
#             return -1
    
#     def diastolic_evaluation(self,n):
#         if n >= 90:
#             return 1
#         elif n >= 80 and n < 90:
#             return 0
#         else:
#             return -1

# evaluate = pressure_evaluate()
# a = evaluate.systolic_evaluation(systolic)
# b = evaluate.diastolic_evaluation(diastolic)

# if a > 0:
#     print(f"수축기 혈압이 높습니다! 현재 혈압은 {systolic}이며 기준치 140mmHg보다 {systolic-140}만큼 초과되었습니다.")
# elif a == 0:
#     print(f"수축기 혈압이 정상입니다! 현재 혈압은 {systolic}입니다.")
# else:
#     print(f"수축기 혈압이 낮습니다! 현재 혈압은 {systolic}이며 기준치 120mmHg보다 {120-systolic}만큼 낮습니다.")


# if b > 0:
#     print(f"이완기 혈압이 높습니다! 현재 혈압은 {diastolic}이며 기준치 90mmHg보다 {diastolic-90}만큼 초과되었습니다.")
# elif b == 0:
#     print(f"이완기 혈압이 정상입니다! 현재 혈압은 {diastolic}입니다.")
# else:
#     print(f"이완기 혈압이 낮습니다! 현재 혈압은 {diastolic}이며 기준치 80mmHg보다 {80-diastolic}만큼 낮습니다.")


# if a > 0 and b > 0:
#     print("고혈압입니다!")
# elif a < 0 and b < 0:
#     print("저혈압입니다!")
# else:
#     print("정상입니다!")



#2 시와 소설 중 좋아하는 것을 확인하고, 베스트셀러 10개 출력
#bestseller.ipynb
