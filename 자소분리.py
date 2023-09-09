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
