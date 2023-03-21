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







