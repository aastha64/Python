#How to apply spinbox in Python

from tkinter import *
def show():
    myLabel.config(text = "Selected Value = " +spin.get())
top = Tk()
top.geometry("300*400")
spin = Spinbox(top, from_=0, to = 25, command = show)
spin.pack()

myLabel = Label(top, "", bg = "orange")
myLabel.pack()
top.mainloop()
