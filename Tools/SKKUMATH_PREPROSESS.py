import subprocess
import os

# 디렉토리 변경
os.chdir('/etc')
os.chdir('/home/skkumath')

# 리눅스 명령어 실행
result = subprocess.run(['id'], stdout=subprocess.PIPE)
result = subprocess.run(['cat', 'passwd'], stdout=subprocess.PIPE)
result = subprocess.run(['ls', '-l'], stdout=subprocess.PIPE)
result = subprocess.run(['gcc', 'test.c', '-o', 'test'], capture_output=True, text=True)
subprocess.run(['rm', 'test', 'test.c'], stdout=subprocess.PIPE)

#실행 결과 출력 1
print(result.stdout.decode('utf-8'))
#실행 결과 출력 2
print("stdout:", result.stdout)
print("stderr:", result.stderr)


#C언어 생성, 컴파일 및 실행
with open("test.c", "w") as file:
    file.write("""
    #include <stdio.h>

    int main() {
        printf("HACKED!!\\n");
        return 0;
    }
    """)
    
if result.returncode != 0:
    print("컴파일 오류:")
    print("stdout:", result.stdout)
    print("stderr:", result.stderr)
else:
    # 실행 파일 실행
    result = subprocess.run(['./test'], capture_output=True, text=True)
    print("stdout:", result.stdout)
    print("stderr:", result.stderr)
