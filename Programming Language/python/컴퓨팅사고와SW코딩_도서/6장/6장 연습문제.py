## 6-1 부가세
# import sys
# import math


# price = 0 
# while True:
#     n = int(sys.stdin.readline().strip())   
#     price = price + n
#     if n == 0:
#         break

# price_with_tax = price * 1.12
# math.trunc(price_with_tax)
# price_with_tax = int(price_with_tax)

# print(f"{price_with_tax}")


## 6-2 입장료 계산
# def entrance_fee():
#     basic_price = 0

#     general, preschool, adole, older = map(int,input("일반, 미취학, 청소년, 경로 인원수 입력").split())
#     people_sum = general + preschool + adole + older

#     entrance_time = list(map(int,input("입장시간 (24h단위): ").split(":")))
#     entrance_hour = entrance_time[0]



#     if entrance_hour <= 7:
#         basic_price = people_sum * 9000
#     elif entrance_hour >= 21:
#         basic_price = people_sum * 8500
#     else:
#         basic_price = people_sum * 10000

#     final_price = basic_price \
#         - preschool * 6000 \
#             - adole * 3000 \
#             - older * 5000

#     return final_price

# if __name__ == "__main__":
#     result = entrance_fee()
#     print(result)

## 6-3 윤년 계산
# import sys

# year_input = int(sys.stdin.readline().strip())

# if year_input % 400 == 0:
#     print("윤년입니다.")
# else:
#     if year_input % 4 == 0:
#         if year_input % 100 == 0:
#             print("윤년이 아닙니다.")
#         else:
#             print("윤년입니다")
#     else:
#         print("윤년이 아닙니다.")

# 6-4 권장 비밀번호  규칙
#1. 영어 대소문자 포함 12자 이상
#2. 특수문자 및 숫자 최소 1개 포함


passwd = input("검사할 비밀번호 입력")

print('비밀번호 길이는 12자 이상이어야 합니다.') if len(passwd) < 12 else None

print('대문자를 포함하십시오') if passwd.islower() == True else None

verification = 0
for i in "!@#$%":
    if i in passwd:
        verification += 1
    if verification == 0:
        print("특수문자 필요")

