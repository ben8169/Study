# 14-1 두 txt 파일 번갈아가면서 한 줄씩 출력하기
with open('1.txt', 'r') as f1, open('2.txt', 'r') as f2:
    for (line1, line2) in zip(f1, f2):
        print(line1.strip())
        print(line2.strip())
    else:
        print('complete')

