from tkinter import *
from tkinter.messagebox import showinfo,showerror
def showheight():
	if height.get():
		showinfo(title="Results",message=f"Your height is {height.get()}")
	else:
		showerror(title="Error",message="Text field can't be empty")
root = Tk()
root.title("Height Calculator")
root.geometry("300x150")
lbl = Label(root,text="Enter your height")
height = Entry(root)
btn = Button(root,text="Click me :)",command=showheight)
lbl.grid(row=1,column=1)
height.grid(row=1,column=2)
btn.grid(row=3,column=2)
root.mainloop()