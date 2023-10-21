# 출처 : https://velog.io/@parkseungju3/python-%ED%95%9C%EA%B8%80-%EC%9E%90%EC%9D%8C%EB%AA%A8%EC%9D%8C-%EB%B6%84%EB%A6%AC%ED%98%84%EC%83%81-%ED%95%B4%EA%B2%B0%EC%BD%94%EB%93%9C


import sys
from unicodedata import normalize
import os
import argparse

def change_nfc_all_dir(dirname):
    filenames = os.listdir(dirname)
    for filename in filenames:
        before_filename = os.path.join(dirname, filename)
        after_filename = normalize('NFC', before_filename)
        os.rename(before_filename, after_filename)
        
        if os.path.isdir(before_filename):    
            change_nfc_all_dir(before_filename)


def main():
    parser = argparse.ArgumentParser(description='자소분리')
    parser.add_argument('-p','--path', type=str, default="C:\\Users\\ben81\\iCloudDrive", help='path')
    parser.add_argument('-r','--rep', type=int, default=10, help='numbers of repeat')
    args = parser.parse_args()

    print(f"current path = {args.path}")
    for i in range(args.rep):
        print(f"{i+1}th start")
        try:
            change_nfc_all_dir(args.path)
            print(f"{i+1}th complete")
        except:
            pass

if __name__ == '__main__':
    main()
