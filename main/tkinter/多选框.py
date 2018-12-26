import tkinter


win = tkinter.Tk()
win.title("Tang")
win.geometry("400x400+200+20")

check1 = tkinter.Checkbutton(win, text="money")
check1.pack()
check2 = tkinter.Checkbutton(win, text="power")
check2.pack()
check3 = tkinter.Checkbutton(win, text="person")
check3.pack()

win.mainloop()
