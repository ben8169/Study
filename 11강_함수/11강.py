# # 11-1 반복횟수, 색상, 각형 입력받아서 그리기
# sol1
# import turtle as t

# def ask_continue():
#     question = t.textinput("반복", "반복하시겠습니까")
#     return 1 if question.lower() == 'y' else 0

# def choosing_color():
#     color = t.textinput("색 선택", "펜 색깔을 선택하세요")
#     return color

# def choosing_angle():
#     angle = t.numinput("각 선택", "몇각형을 그리실껀가요?")
#     return int(angle)

# def drawing(color, angle):
#     t.pencolor(color)
#     for i in range(angle):
#         t.forward(50)
#         t.right(360/angle)
#     return


# if __name__ == '__main__':
#     t.speed(100)
#     x = 1
#     while x:
#         input_color = choosing_color()
#         input_angle = choosing_angle()
#         t.penup()
#         t.goto(-400, 400)
#         t.pendown()
#         drawing(input_color, input_angle)
#         x = ask_continue()


# # sol2
# import turtle as t
# import random

# t.speed(100)
# for i in range(3):
#     for j in range(4):
#         t.penup()
#         t.goto(-300+200*j, 300-200*i)
#         t.pendown()
#         angle = random.randint(3, 20)
#         for _ in range(angle):
#             t.forward(40)
#             t.right(360/angle)
# t.exitonclick()

# 11-2 동아리 회원 json, email 검증까지
import json
import re

try:
    with open("path/to/save/json/club_member.json", "r", encoding="utf-8") as f:
        member_dic = json.load(f)
        print("json에서 불러옴.")

except:
    member_dic = {}
    print("json파일 없음. 새로 시작")

[print(i, member_dic[i], end="\n") for i in member_dic]


def matching(info_name, re_rule):
    while True:
        input_info = input(f"{info_name}을 입력하세요: ")
        if re.fullmatch(re_rule, input_info) == None:
            print(f"{info_name} 형식 오류")
        else:
            break
    return input_info


continue_alert = 'y'
while continue_alert == 'y':
    member_name = input("1.이름을 입력하세요: ")
    member_email = matching("이메일", "[A-z0-9]+@[A-z0-9]+\.[A-z.]+")
    member_phone = matching("전화번호", "[0-9]{2,3}-[0-9]{2,4}-[0-9]{4}")

    print(f"등록 완료. {member_name}/{member_email}/{member_phone}")

    confirm_alert = input("위 정보로 등록하시겠습니까?(Y/N)")
    if confirm_alert.lower() == 'y':
        member_dic[member_name] = [member_email, member_phone]
    else:
        print("내용을 파기하고 재등록을 시작합니다.")
        continue

    continue_alert = input("추가 등록 하시겠습니까?(Y/N) N 또는 아무 키를 눌러 종료하여 저장하십시오.")
    if continue_alert.lower() == 'y':
        continue
    else:
        break

with open("path/to/save/json/club_member.json", "w", encoding="utf-8") as f:
    json.dump(member_dic, f, indent=2, ensure_ascii=False)
