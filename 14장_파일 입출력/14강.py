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
