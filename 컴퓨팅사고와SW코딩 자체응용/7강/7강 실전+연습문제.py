-##7-1 도형 작성 프로그램
# import turtle as t

# x_width = t.numinput("가로 길이", "가로 길이를 입력하세요:") 
# y_width = t.numinput("세로 길이", "세로 길이를 입력하세요:") 
# line_color = t.textinput("색상","색상 입력:")
# line_thickness = t.textinput("굵기", "선 굵기 입력:")


# # t.bgcolor("pink")
# t.fillcolor(line_color)
# t.begin_fill()
# t.color("black")
# t.pensize(line_thickness)
# t.penup()
# t.goto(0,0)
# t.pendown()
# for _ in range(2):
#     t.forward(x_width)
#     t.right(90)
#     t.forward(y_width)
#     t.right(90)
# t.end_fill()
# t.mainloop()



#7-2 사각형 종류 구별 프로그램

# width = int(input("가로길이 입력:"))
# height = int(input("세로길이 입력:"))
# IsAngle90 = input("내각이 전부 90도인가요?")

# if IsAngle90.lower() == "y":
#     print("정사각형") if width == height else print("직사각형")
# else:
#     print("마름모") if width == height else print("사각형")



#7-3 구구단 출력

# num = int(input("출력할 구구단 입력"))
# [print(f"{num} * {n} = {num*n}") for n in range(1,10)]


#연습문제
#7-2 띠 확인 프로그램
# while True:
#     year_input = int(input("해 입력:"))
#     i = (year_input - 2000) % 12
#     a = ['용', '뱀', '말', '양', '원숭이', '닭', '개', '돼지', '쥐', '소', '범', '토끼']
#     print(a[i])



#7-3 팩토리얼 구현
#sol1
# import sys
# n = int(sys.stdin.readline())

# x = n
# for j in range(1,n):
#     m = n - j
#     print(m)
#     x *= m
# print(x)

#2 sol2
# import numpy as np
# import sys
# n = int(sys.stdin.readline())

# a = np.arange(1,n+1)
# print(np.prod(a))


