from tkinter import *
from tkinter.messagebox import showinfo, showerror


def showheight():
    if height.get():
        showinfo(title="Results", message=f"Your height is {height.get()}")
    else:
        showerror(title="Error", message="Text field can't be empty")


root = Tk()
root.title("Height Calculator")
root.geometry("300x150")
lbl = Label(root, text="Enter your height")
lbl.pack(pady=15)
height = Entry(root)
height.pack(pady=15)
btn = Button(root, text="Click me :)", command=showheight)
btn.pack(pady=15)
root.mainloop()
