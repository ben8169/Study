# #label
# from tkinter import *

# root = Tk()
# root.title("GUI 연습")
# root.geometry("400x200")

# label1 = Label(root, text="sql은")
# label2 = Label(root, text="쉽다", font=("궁서체", 30), bg="blue", fg="yellow")
# label1.pack()
# label2.pack()

# root.mainloop()

# #button
# from tkinter import *
# from tkinter import messagebox

# def clickButton():
#     messagebox.showinfo("버튼 클릭", "버튼이 클릭되었습니다.")

# root = Tk()
# root.title("버튼 연습")
# root.geometry("200x100")

# button1 = Button(root, text="버튼을 클릭하세요", fg="red", command=clickButton)
# button1.pack(expand=1)

# root.mainloop()

# #위젯 정렬
# from tkinter import *

# root = Tk()

# button1 = Button(root, text="버튼1")
# button2 = Button(root, text="버튼2")
# button3 = Button(root, text="버튼3")

# button1.pack(side=TOP, fill=X, padx=10, pady=10)
# button2.pack(side=TOP, fill=X, padx=10, pady=10)
# button3.pack(side=TOP, fill=X, padx=10, pady=10)

# root.mainloop()


# #프레임,엔트리, 리스트박스
from tkinter import *

from sympy import root
root = Tk()
root.geometry("600x400")

upFrame = Frame(root)
upFrame.pack()
downFrame = Frame(root)
downFrame.pack()

editBox = Entry(upFrame, width=10)
editBox.pack(padx=10, pady=10)

listbox = Listbox(downFrame, bg='yellow')
listbox.pack()

listbox.insert(END, "하나")
listbox.insert(END, "둘")
listbox.insert(END, "셋")

root.mainloop()