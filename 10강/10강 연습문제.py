# # 10-1 요청받아 원 이어그리기
# import turtle as t

# t.speed(10)

# i = 0
# while True:
#     t.penup()
#     t.goto(i, i)
#     t.pendown()
#     t.circle(50)
#     x = t.textinput("continue", "그만할까요?")
#     try:
#         if x.lower() == 'y':
#             break
#     except:
#         pass
#     i += 50*1.414
# t.exitonclick()


# # 10-2 주사위 게임 무한반복
# import random


# def battle(n):
#     com = random.randint(1, 6)
#     player = n
#     if com > player:
#         return -1, com, n
#     elif com == player:
#         return 0, com, n
#     elif com < player:
#         return 1, com, n


# while True:
#     try:
#         option = int(input("주사위 숫자를 선택하세요!(0:종료)>>>"))
#     except ValueError as err:
#         print(err, "\n=========숫자만 입력하세요===========\n")
#         continue
#     if option in [1,2,3,4,5,6]:
#         result = battle(option)
#         if result[0] == -1:
#             print(f"컴퓨터 승! 컴퓨터:{result[1]}, 본인:{result[2]}\n")
#         elif result[0] == 0:
#             print(f"무승부! 컴퓨터:{result[1]}, 본인:{result[2]}\n")
#         elif result[0] == 1:
#             print(f"플레이어 승! 컴퓨터:{result[1]}, 본인:{result[2]}\n")
#     elif option == 0:
#         break
#     else:
#         print("\n입력값 오류\n")
#         continue
