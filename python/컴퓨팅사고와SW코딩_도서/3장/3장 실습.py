##실습 3-1  변수선언 (심화)
rep_num = int(input("숫자 몇개를 입력하실껀가요?"))

def avgcalculator(n):
    sum_list = []
    for i in range(n):
        x = float(input(f"{i+1}/{n}번째 숫자 입력"))
        sum_list.append(x)

    sum_result = sum(sum_list)
    print("%.3f"%sum_result)

    avg_result = (sum_result) / len(sum_list)
    print("{1:>.3f}".format(sum_result,avg_result))

    return


if __name__ == "__main__":
    avgcalculator(rep_num)




## 실습 3-2 진법 변경하기
base_type = int(input("몇 진수로 입력하나요?(2/8/16/10)"))
input_num = input("해당 진수의 숫자를 입력하세요.")

x = int(input_num,base_type)


print(f"""======
입력하신 숫자의 각 진수별 표현은 다음과 같습니다.
16진수 = {hex(x)}
10진수 = {x}
8진수 = {oct(x)}
2진수 = {bin(x)}""")



## 실습 3-3 GUI로 그래프 그리기
import turtle as t

num_input = t. numinput("막대 수","막대그래프의 개수를 입력하세요")
num_input = int(num_input)
t.penup()
t.goto(-300,-250)
t.pendown()
t.pensize(3)
t.forward(600)
t.penup()
t.goto(-200,-250)
t.pendown()

for i in range(num_input):
    color_input = t.textinput("Color", "Choose the graph color.")
    t.fillcolor(color_input)
    t.begin_fill()
    t.pensize(1)
    t.pencolor(color_input)
    distance_input = t.numinput("Height", "Type the height.")
    t.left(90)
    t.forward(distance_input)
    t.write(distance_input)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(distance_input)
    t.left(90)
    t.end_fill()
    
t.exitonclick()