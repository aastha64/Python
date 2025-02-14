# Implementing ToolBars in Tkinter

import tkinter as tk
from tkinter import messagebox
def New():
    messagebox.showinfo("Info","New ToolBar Clicked")

def Open():
    messagebox.showinfo("Info","Open ToolBar Clicked")

mywindow=tk.Tk()
mywindow.title("ToolBar Example")
mywindow.geometry("400x300")
mytoolbar=tk.Frame(mywindow,bd=2,relief=tk.RAISED)
mytoolbar.pack(side=tk.TOP,fill=tk.X)
button1=tk.Button(mytoolbar,text="New",command=New)
button1.pack(side=tk.LEFT,padx=4, pady=4)
button2=tk.Button(mytoolbar,text="Open",command=Open)
button2.pack(side=tk.LEFT,padx=4, pady=4)

mywindow.mainloop()