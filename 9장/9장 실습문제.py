# 9-1 회원정보 입력받아 저장하고 출력하기 > json 파일로 만들어보자 + increment path 적용시켜보기
# # increment path 적용, 파일 없을경우 생성하도록
# # import os
# # i = 0
# # while os.path.exists("/Users/ben8169/Desktop/member%d.json" % i):
# #     i += 1
# # json_path = f"/Users/ben8169/Desktop/member{i}.json"


# import json
# global json_path
# json_path = "/Users/ben8169/Desktop/member.json"

# # json 파일이 없을경우 파일 생성 + 빈 json파일일 경우 빈 dict 오류 회피
# def input_information():
#     try:
#         with open (json_path,'r', encoding='utf-8') as f:
#             try:
#                 data = json.load(f)
#             except:
#                 data = {}
#     except:
#         with open (json_path,'w', encoding='utf-8') as f:
#             try:
#                 data = json.load(f)
#             except:
#                 data = {}
#     #정보 입력
#     member_num = int(input("회원수를 입력하세요:"))
#     for i in range(member_num):
#         print(f"{'='*5}{i+1}번째 회원 정보 입력{'='*5}")
#         member_name = input("회원 이름를 입력하세요:")
#         member_phone = input("전화번호를 입력하세요:(010-xxxx-xxxx)")
#         member_email = input("이메일을 입력하세요:")
#         data[member_name] = [member_phone,member_email]

#         #저장
#     with open(json_path,'w',encoding='utf-8') as f:
#             json.dump(data,f,ensure_ascii=False, indent='\t')


#         #조회
# def check_out():
#     try:
#         with open(json_path,'r', encoding='utf-8') as f:
#             member_dic = json.load(f)
#             name_list = list(member_dic.keys())
#             print("{:^5}|{:^12}|{:^20}".format('이름','전화번호','이메일'))
#             [print(f"{i} | {member_dic[i][0]}\t|  {member_dic[i][1]}") for i in name_list]
#     except:
#         print("에러가 발생했습니다.JSON 파일이 정확한지 확인해주세요.")


# def delete_member():
#     try:
#         with open(json_path,'r', encoding='utf-8') as f:
#             member_dic = json.load(f)

#         while True:
#             print(member_dic)
#             delete_target = input("삭제할 회원의 이름을 정확히 입력하세요.(q로 종료):")
#             if delete_target.lower() == 'q':
#                 return
#             else:
#                 del([member_dic[delete_target]])
#                 with open(json_path,'w',encoding='utf-8') as f:
#                     json.dump(member_dic,f,ensure_ascii=False, indent='\t')


#     except:
#         print("에러가 발생했습니다.JSON 파일이 정확한지, 입력값이 정확한지 확인해주세요.")


# def main():
#     menu = True
#     while menu:
#         try:
#             menu = int(input("메뉴 선택 1.입력 2. 조회 3.삭제 (0.종료)"))
#             if menu == 1:
#                 input_information()
#             elif menu == 2:
#                 check_out()
#             elif menu == 3:
#                 delete_member()
#         except ValueError as err:
#             print(err)
#             continue

# if __name__ == '__main__':
#     main()


# 9-2 369게임 - 3의배수 + 3, 6, 9 포함 >> * 출력
# #sol1
# n = int(input("번호 입력"))
# lst = [i if i % 3 != 0 else '*' for i in range(1, n+1)]
# for s in lst:
#     for t in str(s):
#         if t in ['3','6','9']:
#             change_index = lst.index(s)
#             lst[change_index] = '*'
#             break
# print(lst)

# sol2
# n = int(input("번호 입력"))
# prev_lst = [n for n in range(1, n+1)]
# aft_list = []
# for i in prev_lst:
#     k = 0
#     if i % 3 != 0:
#         for j in str(i):
#             if j in ['3', '6', '9']:
#                 k += 1
#         if k == 0:
#             aft_list.append(i)
#         elif k > 0:
#             aft_list.append('*')

#     elif i % 3 == 0:
#         aft_list.append('*')
# print(aft_list)


# #sol3
# n = int(input("번호 입력"))
# for i in range(1, n+1):
#     x = 0
#     if i % 3 == 0:
#         print('*', end=',')
#         continue
#     else:
#         for n in ['3', '6', '9']:
#             if f'{n}' in str(i):
#                 x = 1
#         print('*', end=',')s if x == 1 else print(i, end=',')


# 9-3 1부터 200까지 중 Prime Number 만 모아서 출력
