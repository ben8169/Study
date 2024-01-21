# 14-1 두 txt 파일 번갈아가면서 한 줄씩 출력하기
with open('1.txt', 'r') as f1, open('2.txt', 'r') as f2:
    for (line1, line2) in zip(f1, f2):
        print(line1.strip())
        print(line2.strip())
    else:
        print('complete')


# 14-2 한 줄씩 입력하여 txt 생성
f = open('write_by_lines.txt', 'w')
text_sum = ''

while True:
    text = input("죽기 전에 하고 싶은 일은?:")
    text_sum += text + '\n'
    ask_continue = input("계속 입력?(Y/N)")
    if ask_continue.lower() == 'n':
        break
    else:
        continue

f.writelines(text_sum)
f.close()

txt_file = open('write_by_lines.txt', 'r')
print(txt_file.read())
txt_file.close()

# 연습문제
#한/영 가사 따로 출력하기
with open('butter_lyrics.txt','w') as f:
    lyrics = '''당신 눈이 내 눈에 닿을 때
Butterfly, high five
너의 손길이 내 손에 닿을 때
Run it, make fly
아슬하게 더 높이 날아올라
Butter fly, like a butterfly
하루 종일 소리쳐
I like that, in your eyes
그림자 너머로 또 다른 나의 문을 열어줘'''

    f.write(lyrics)
    f.close()

with open('butter_lyrics.txt','r') as f:
    lyrics = f.readlines()
while True:
    ko_eng_choice = int(input("1.한글 2.영어 어떤걸로 출력할까요? 숫자를 입력하세요.(3.exit)"))
    if ko_eng_choice == 1:
        ko_list = lyrics[0::2]
        ko_str = ''
        for i in ko_list:
            ko_str += i 
        print(ko_str)
    elif ko_eng_choice == 2:
        eng_list = lyrics[1::2]
        eng_str = ''
        for i in eng_list:
            eng_str += i 
        print(eng_str)
    elif ko_eng_choice == 3:
        break
        
    else:
        print("잘못 입력하셨습니다.")
