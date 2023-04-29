##5-1 글자 회오리
# import turtle as t

# text = "this is test sample"
# color = ['red', 'blue', 'black', 'green', 'yellow']

# t.bgcolor('lightblue')
# t.speed(10)
# for n in range(0,50):
#     t.pencolor(color[n%5])
#     t.pendown()
#     t.write(text, font=20)
#     t.penup()
#     t.left(75)
#     t.forward(n*5)

# t.exitonclick()

##5-2 튜플 생성하기(더하기 할 수있다/요소 한개는 쉼표!!)

# cur_tuple = ()
# while True:
#     str = input("튜플에 추가할 입력값:(exit:Q)")
#     if str == "q".lower():
#         break
#     else:
#         new_tuple = (str,)      ##쉼표!!!!!!
#         cur_tuple += new_tuple
# print(cur_tuple)

##5-3 딕셔너리
# dict = {}
# while True:
#     tmp_key = input("새로운 key 값 입력:")
#     new_value = input("새로운 value 값 입력:")
#     dup_list = list(dict.keys())
#     new_key = input(f"이미 있는 key입니다. 다른 key를 입력하세요. 현재 value:{new_value}:") if tmp_key in dup_list else tmp_key

#     dict[new_key] = new_value
#     print(dict)
#     x = input("계속하시겠습니까?(Y/N)")
#     if x.lower() == 'n':
#         print(dict)
#         break
#     else:
#         continue
