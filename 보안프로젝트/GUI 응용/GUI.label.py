import tkinter as tk

win = tk.Tk()
win.title("Label붙이기")
win.geometry("400x300+100+100")

label1 = tk.Label(win, text="문자열 붙이기", font=("System", 15))
label1.place(x=100, y=100)

win.mainloop()
