# 1 수축기, 이완기 혈압으로 고혈압, 저혈압 판정하기
# systolic, diastolic = [int(input(f"{i}기 혈압을 입력하세요. (높은 쪽이 수축기)")) for i in ['수축','이완']]

# class pressure_evaluate():
#     def systolic_evaluation(self,n):
#         if n >= 140:
#             return 1
#         elif n >= 120 and n < 140:
#             return 0
#         else:
#             return -1
    
#     def diastolic_evaluation(self,n):
#         if n >= 90:
#             return 1
#         elif n >= 80 and n < 90:
#             return 0
#         else:
#             return -1

# evaluate = pressure_evaluate()
# a = evaluate.systolic_evaluation(systolic)
# b = evaluate.diastolic_evaluation(diastolic)

# if a > 0:
#     print(f"수축기 혈압이 높습니다! 현재 혈압은 {systolic}이며 기준치 140mmHg보다 {systolic-140}만큼 초과되었습니다.")
# elif a == 0:
#     print(f"수축기 혈압이 정상입니다! 현재 혈압은 {systolic}입니다.")
# else:
#     print(f"수축기 혈압이 낮습니다! 현재 혈압은 {systolic}이며 기준치 120mmHg보다 {120-systolic}만큼 낮습니다.")


# if b > 0:
#     print(f"이완기 혈압이 높습니다! 현재 혈압은 {diastolic}이며 기준치 90mmHg보다 {diastolic-90}만큼 초과되었습니다.")
# elif b == 0:
#     print(f"이완기 혈압이 정상입니다! 현재 혈압은 {diastolic}입니다.")
# else:
#     print(f"이완기 혈압이 낮습니다! 현재 혈압은 {diastolic}이며 기준치 80mmHg보다 {80-diastolic}만큼 낮습니다.")


# if a > 0 and b > 0:
#     print("고혈압입니다!")
# elif a < 0 and b < 0:
#     print("저혈압입니다!")
# else:
#     print("정상입니다!")



#2 시와 소설 중 좋아하는 것을 확인하고, 베스트셀러 10개 출력
#bestseller.ipynb

