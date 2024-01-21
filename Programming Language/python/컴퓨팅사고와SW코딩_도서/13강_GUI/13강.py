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


# 13-2 label & button
from tkinter import *

def button_command():
    window = Toplevel(root)
    photo_path = PhotoImage(
        file='/Users/ben8169/Desktop/Image/Screenshot 2023-03-08 at 1.44.29 PM.png')
    photo = Label(window, image=photo_path)
    photo.pack()
    window.mainloop()

root = Tk()
root.title("이미지")
root.geometry("640x480+500+300")

button1 = Button(root, text='눌러보셈', padx=15,
                 pady=5, bg='green', command=button_command)
button1.pack()
root.mainloop()


#menubutton 사용해보기

from tkinter import *
window = Tk()

mb = Menubutton(window, text='분식집', relief=RAISED)
mb.menu = Menu(mb, tearoff=0)
mb['menu'] = mb.menu
mb.menu.add_checkbutton(label='1번')
mb.menu.add_radiobutton(label='2번')

mb.pack()

window.mainloop()
