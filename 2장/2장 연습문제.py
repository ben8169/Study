#1. 계산기 만들기
class calculator:
    def __init__(self,first,second):
        self.first = first
        self.second = second
    
    def addition(self):
        result = self.first + self.second
        result = result
        return result
    def subtraction(self):
        result = self.first + self.second
        return result
    def multiplication(self):
        result = self.first * self.second
        return result 
    def division(self):
        if self.second == 0:
            return 0
        result = self.first/self.second
        return result
    

input1 = float(input("첫번째 수 입력"))

a = calculator(input1,input2)

# print방법1
# print("{:.2f}".format(a.addition()))
# print("{:.2f}".format(a.subtraction()))
# print("{:.2f}".format(a.multiplication()))
# print("{:.2f}".format(a.division()))


# print방법2
print("{:.2f}\n{:.2f}\n{:.2f}\n{:.2f}".format(a.addition(),a.division(),a.multiplication(),a.division()))



# print방법3
# print("%.2f"%a.addition())


# "--------------------------------------------------------------------------------------------------------------------"

##2. 별 표시하기

#1 재귀함수 이용
def drawstar(start,end):
    print("*"*start)
    if start == end:
       return 
    start += 1
    drawstar(start,end)
    print("*"*(start-1))
drawstar(1,5)

#2 comprehension 이용
num = int(input("숫자 입력"))
[print("*"*i) for i in range(1,num+1)]
[print("*"*j) for j in range(num-1, 0,-1)]



#3. turtle로 도형 그리기(zip으로 리스트 합치기 이용,penup>setpos/goto>pendown)

import turtle as t 

position = -300

def draw_shape(shape, color):
    global x_pos
    t.begin_fill()
    t.pencolor("black")
    t.penup()
    t.setpos(x_pos,0)
    t.pendown()
    for i in range(int(shape)):
        t.forward(100)
        t.right(360/int(shape))
    t.fillcolor(color)
    t.end_fill()
    x_pos += 180
# list = [(3,"red"), (4,"yellow"), (5, "green"), (6,"blue")]

shape_list = [3,4,5,6]
color_list = ["red", "yellow", "green", "blue"]
zipped_list = zip(shape_list,color_list)


for shape, color in zipped_list:
    print(shape, color)
    draw_shape(shape, color)


# "--------------------------------------------------------------------------------------------------------------------"


