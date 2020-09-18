from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo, showerror


def showheight():
    if height.get():
        showinfo(title="Results", message=f"Your height is {height.get()}")
    else:
        showerror(title="Empty Field", message="Text field can't be empty")


root = Tk()
root.title("Height Calculator")
root.geometry("500x400")
lbl = Label(root, text="Enter your height", font=("bold", 18))
lbl.pack(pady=15)
height = ttk.Entry(root, width=30)
height.pack(pady=15, ipadx=25, ipady=5)
btn = ttk.Button(root, text="Calculate", command=showheight)
btn.pack(pady=15)
root.mainloop()
