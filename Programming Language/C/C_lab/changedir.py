import sys
import os

folder_path = "/Users/ben8169/Documents/GitHub/Study/Programming Language/C/C_lab"

for filename in os.listdir(folder_path):
    if filename.startswith("lab"):
        new_filename = filename.replace("lab", "chapter")
        os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))