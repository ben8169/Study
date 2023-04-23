# 13-1.tkinter label 이해
from tkinter import *

window = Tk()
window.title("window sample 1")
window.geometry("500x300")
window.resizable(width=False, height=False)

message = Label(window, text="example", bg='blue', fg='white',
                width=50, height=10, anchor=SE) #anchor은 방위로 표현, text의 위치
message.pack()
window.mainloop()
