# ## 6-1 거스름돈 최소로 거슬러주기
# import sys
# money_input = int(sys.stdin.readline().strip())
# money_unit = [50000 , 10000, 5000, 1000, 500, 100, 50, 10, 1]


# # sol1 - 재귀함수

# # n = 0
# # def dividing(money):
# #     global n
# #     bill_num = int(money // money_unit[n])
# #     print(f"{money_unit[n]}원짜리 {bill_num}장") if money_unit[n] >= 1000 else print(f"{money_unit[n]}원짜리 {bill_num}개")
# #     money = int(money % money_unit[n])
# #     n += 1
# #     if n == 9:
# #         return
# #     dividing(money)


# # dividing(money_input)




# # sol2 - 반복문

# money = money_input

# # for n in range(9):
# #     bill_num = int(money // money_unit[n])
# #     print(f"{money_unit[n]}원짜리 {bill_num}장") if money_unit[n] >= 1000 else print(f"{money_unit[n]}원짜리 {bill_num}개")
# #     money = int(money % money_unit[n])



## 6-3 배수 구별하기
# import numpy as n

# a = np.arange(1,51)
# a = list(a)
# [print(i, end=' ') if i%2 == 0 and i%3 == 0 else None for i in a]
# print("")
# [print(j, end=' ') if j%3 == 0 or j%7 == 0 else None for j in a]
# print("")
# [print(k, end=' ') if k%5 != 0 else None for k in a]