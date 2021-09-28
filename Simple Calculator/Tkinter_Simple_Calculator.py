from tkinter import *


root =Tk()
root.title("calculator")


num1 = Label(root, text = "Enter the 1st number: ")
ent1 = Entry(root)
num2 = Label(root, text = "Enter the 2nd number: ")
ent2 = Entry(root)


def add():
    x = int(ent1.get())
    y = int(ent2.get())
    result["text"] = x + y
def sub():
    x = int(ent1.get())
    y = int(ent2.get())
    result["text"] = x - y
def mul():
    x = int(ent1.get())
    y = int(ent2.get())
    result["text"] = x * y
def div():
    x = int(ent1.get())
    y = int(ent2.get())
    result["text"] = x / y
def mod():
    x = int(ent1.get())
    y = int(ent2.get())
    result["text"] = x % y


add = Button(root, text="Add", width = 10, command = add)
sub = Button(root, text="Sub", width = 10, command = sub)
mul = Button(root, text="Mul", width = 10, command = mul)
div = Button(root, text="Div", width = 10, command = div)
mod = Button(root, text="Mod", width = 10, command = mod)


result = Label(root)


num1.grid(row=0, column=0)
ent1.grid(row=0, column=1)
num2.grid(row=1, column=0)
ent2.grid(row=1, column=1)
add.grid(row=2, column=0)
sub.grid(row=2, column=1)
mul.grid(row=3, column=0)
div.grid(row=3, column=1)
mod.grid(row=4, column=0)
result.grid(row=5, column=1)



root.mainloop()