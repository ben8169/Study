# # 9-1 300~0까지 3의 배수에 대해 제곱과 루트 값을 출력
# import math
# [print(f"{i}의 제곱은 {i**2}, 제곱근은 {math.sqrt(i):.5f}입니다.",end='\n') for i in range(300,0,-3)]

# # 9-2 지역번호 입력으로 번호 완성

# local_num_dict={
#     '서울':'02',
#     '부산':'051',
#     '대구':'053',
#     '인천':'032',
#     '광주':'062',
#     '대전':'042',
#     '울산':'052',
#     '세종':'044',
#     '경기':'031',
#     '강원':'033',
#     '충북':'043',
#     '충남':'041',
#     '전북':'063',
#     '전남':'061',
#     '경북':'054',
#     '경남':'055',
#     '제주':'064'
# }

# answer_list = []

# print(f"지역 목록 : {list(local_num_dict.keys())}")

# i = int(input("총 번호 개수"))

# for _ in range(i):
#     local_name, tel_num = input("지역과 번호 입력 (xxx-xxxx)").split()
#     local_num  = local_num_dict[local_name]
#     x = local_num + "-" + tel_num
#     answer_list.append(x)

# else:
#     print("완성된 목록")
#     [print(n) for n in answer_list]

# # 9-4 나선형으로 육각형 그리기
# import turtle as t
# t.speed(10000)
# t.bgcolor('black')
# t.penup()
# t.goto(0,0)
# t.pendown()

# j = 5
# pencolor_list = ['red','blue','green','yellow']
# for i in range(60):
#     t.pencolor(pencolor_list[i%4])
#     for _ in range(6):
#         t.forward(j)
#         t.right(60)
#     t.right(20)
#     j += 3

# t.exitonclick()


