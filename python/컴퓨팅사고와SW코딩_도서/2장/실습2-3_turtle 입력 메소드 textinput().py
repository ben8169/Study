import turtle as t

input_color= t.textinput("선의 색", "선 색을 입력하세요")
input_fill_color = t.textinput("색 채우기","색을 채우시겠습니까?")
input_fill_color = input_fill_color.lower()
input_shape = t.numinput("형태 정하기","몇 각형으로 하시겠습니까?")
input_shape = int(input_shape)


if input_color:
    t.pencolor(input_color)
else:
    t.pencolor("black")

if input_fill_color == 'y':
    t.fillcolor(input_color)
else:
    t.fillcolor("white")

t.begin_fill()
for i in range(input_shape):
    t.forward(100)
    t.right(360/input_shape)
t.end_fill()

