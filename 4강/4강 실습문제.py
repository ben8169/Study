##4-1 스케줄 입력
# schedule_list = [] 
# while True:
#     time = input("시간 입력:")
#     work = input("할일 입력:")
#     schedule = time + "\t" + work
#     schedule_list.append(schedule)
#     print("="*10, "오늘의 스케줄","="*10)
#     [print(f) for f in schedule_list]
#     x = input("종료?[Y/N]:")
#     if x.lower() == 'y':
#         break 


##4-2 홀수 인덱스 제거
#1
# sentence = "3봄일이시오청나앞보정네오요"
# print(sentence[::2])

#2
# sentence = input("입력>>>>")
# sentence = "3봄일이시오청나앞보정네오요"
# n = len(sentence)
# message = ''
# for i in range(n):
#     if i%2 == 0:
#         message += sentence[i]
#     else:
#         pass
    
# print(message)

##4-3 문자열 인덱싱 수정 + enumerate로 인덱스 쉽게 확인하도록 개선
# input_string = input("수정할 문장 입력:")

# start_revise_string = input("수정 시작할 글자 입력:")
# start_revise_string_list = [(n, name) for n, name in enumerate(input_string) if name in start_revise_string]
# print("정확한 인덱스를 선택하세요","="*10)
# [print(start_revise_string_list, end=" ")]
# start_revise_index =int(input("\n인덱스 입력>>"))

# end_revise_string = input("수정 종료할 글자 입력:")
# end_revise_string_list = [(n, name) for n, name in enumerate(input_string) if name in end_revise_string]
# print("정확한 인덱스를 선택하세요","="*10)
# [print(end_revise_string_list, end=" ")]
# end_revise_index =int(input("\n인덱스 입력>>"))

# revise_string = input(f"<{input_string[start_revise_index:end_revise_index + 1]}>의 단어를 무엇으로 바꿀까요?")
# revised_string = input_string[:start_revise_index] + revise_string + input_string[end_revise_index+1:]
# print("수정된 문장:", revised_string)




##4-4 생일 메세지 출력
# name = input("이름 입력:")
# age = int(input("나이 입력:"))
# sender = input("보내는 사람 이름:")

name = '가나다'
age = 20
sender = 'abc'

#1
print("%s님의 %d번째 생일을 축하합니다! %s로부터"%(name,age,sender))

#2
print("{0:<10}님의 {1:^10.2f}번째 생일을 축하합니다! {2:>10}로부터".format(name,age,sender))
