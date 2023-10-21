import sys
from unicodedata import normalize
import os
import time

def change_nfc_all_dir(dirname):
    filenames = os.listdir(dirname)
    for filename in filenames:
        before_filename = os.path.join(dirname, filename)
        after_filename = normalize('NFC', before_filename)
        os.rename(before_filename, after_filename)
        
        if os.path.isdir(before_filename):    
            change_nfc_all_dir(before_filename)

def main():

    print("Welcome!!!")
    print("MacOS<->Windows 파일 자소병합 프로그램 V1.0.0.")
    print("="*100)
    print("1.한글이 포함된 주소는 오류가 있을 수 있습니다.        e.g., C:\\Users\\admin\\바탕 화면 (X)")
    print("**영어로 된 주소 하에서 잘 작동합니다.                  e.g., C:\\Users\\admin\\Download (O)**")
    print("파일 이름은 당연히 상관없습니다.                        e.g., C:\\Users\\admin\\Download\\ㅇㅗㄹㅠ.docx")
    print("="*100)
    print("2.상위 폴더에서는 Permission Error가 발생할 수 있습니다.  e.g., C:\\ㅇㅗㄹㅠ.docx >> C드라이브에 바로 접근 권한 요구하면 오류")
    print("반드시 권한 문제가 없는 하위 폴더에서 진행해 주세요.      e.g., C:\\Users\\admin\\Download (O)")

    
    while True:
        path = input("Enter the path (e.g., C:\\Users\\admin\\Download): ")
        print(path)
        if os.path.exists(True):
            break
        else:
            print("Invalid path. Please enter a valid path.")

    print(f"Current path: {path}")
    
    rep = 10

    try:
        for i in range(rep):
            print(f"{i+1}th start")
            try:
                change_nfc_all_dir(path)
                print(f"{i+1}th complete")
            except KeyboardInterrupt:
                print("프로그램이 강제로 종료되었습니다.")
                break
            except Exception as e:
                print("failed:", str(e))
    except KeyboardInterrupt:
        print("프로그램이 강제로 종료되었습니다.")


if __name__ == '__main__':
    main()
    for t in range(3,0,-1):
        print(f"Completed!! Closing in {t}s...")
        time.sleep(1)
    sys.exit(0)

