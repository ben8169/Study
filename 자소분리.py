import sys
from unicodedata import normalize
import os
import argparse

def change_nfc_all_dir(dirname):
    filenames = os.listdir(dirname)
    print(filenames)
    for filename in filenames:
        before_filename = os.path.join(dirname, filename)
        after_filename = normalize('NFC', before_filename)
        os.rename(before_filename, after_filename)
        
        if os.path.isdir(before_filename):    
            change_nfc_all_dir(before_filename)


def main():
    parser = argparse.ArgumentParser(description='자소분리')
    parser.add_argument('--path', type=str, default="C:\\Users\\ben81\\iCloudDrive", help='path')
    parser.add_argument('--num', type=int, default=10, help='numbers of repeat')
    args = parser.parse_args()

    for i in range(args.num):
        try:
            change_nfc_all_dir(args.p)
            print(f"{i}th complete")
        except:
            pass

if __name__ == '__main__':
    main()
