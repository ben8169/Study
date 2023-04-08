# # # 제10강 실전문제
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


# # 10-3 변화하는 선 색
# sol1
# import turtle as t

# t.colormode(255)
# t.pensize(100)
# t.goto(0, 0)

# for i in range(0, 256):
#     t.pencolor(255-i, 0+i, 0)
#     t.forward(1)

# t.exitonclick()

# sol2
# import turtle as t

# t.pensize(100)

# for i in range(0, 256):
#     j = 255-i
#     i = str(hex(i)[2:])
#     j = str(hex(j)[2:])
#     if len(i) == 1:
#         i = '0'+i
#     if len(j) == 1:
#         j = '0'+j
#     hex_color ="#"+i+j+"FF"
#     t.pencolor(hex_color)
#     t.forward(1)

# t.exitonclick()

# # sol3
# import turtle as t
# import random

# t.pensize(100)
# t.speed(10)


# def changing_color(i):
#     j = 255 - i
#     k = 255 - i
#     values = [i, j, k]
#     hex_values = []
#     for val in values:
#         hex_val = str(hex(val)[2:])
#         if len(hex_val) == 1:
#             hex_val = '0' + hex_val
#         hex_values.append(hex_val)
#     hex_color = hex_values[0] + hex_values[1] + hex_values[2]
#     return hex_color


# for i in range(0, 256):
#     t.pencolor("#"+changing_color(i))
#     t.forward(1)

# t.penup()
# t.pensize(0)
# t.goto(-100, 100)
# t.ht()

# str1 = "색 변화 성공!!!!!"
# for char in str1:
#     t.pencolor("#"+changing_color(random.randint(0, 255)))
#     t.write(char, move=True, font=('Arial', 20, 'normal'))
#     t.forward(20)
# t.exitonclick()


# 10-4 장르/분류 리스트 병합
# lst1 = ['호러', '액션', '코믹', '로맨스']
# lst2 = ['드라마', '영화', '단막극', '웹툰']
# final_lst = []

# for i in lst1:
#     for j in lst2:
#         final_lst.append(i+j)

# print(final_lst)


# # # 10강 연습문제
# #1. 리스트 안의 요소들을 일정수 이상이 될 때 까지 랜덤으로 선택해 더하기
# import random

# x = list(map(int, input().split()))
# y = 0
# while y < 1200:
#     tmp = y
#     y += random.choice(x)
#     print(tmp) if y > 1200 else None


# # 2. 컴프리헨션으로 string 안의 글자수 파악
# str1 = "My name is Zico"
# x = {char: str1.count(char) for char in str1}
# print(x)
