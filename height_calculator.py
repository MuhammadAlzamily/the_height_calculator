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
root.configure({'bg': 'lightgrey'})
myframe = Frame(root, bd=0, bg='lightgrey')
myframe.pack(padx=20, pady=80)
lbl = Label(myframe, text="Enter your height",
            bg='lightgrey', font=("halvetica", 18))
lbl.pack(pady=15)
height = ttk.Entry(myframe, width=30)
height.pack(pady=15, ipadx=25, ipady=5)
btn = Button(myframe, text="Calculate", command=showheight,
             relief='flat', bg='red', fg='white')
btn.pack(pady=15)
root.mainloop()
