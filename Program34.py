from tkinter import *   #ALL MODULES I NEED TO IMPORT
window= Tk() #INITIALIZE A WINDOW

def mouseClick(event):
    print("OK Button has been clicked")

def mouseClick1(event):
    print("Cancel Button has been clicked")
label1= Label(window,text="Choose your option")

label1.place(x=40,y=20)
label1.pack()  #THE COMPONENT WILL  BE VISIBLE

button1=Button(window, text="OK",bg="Red",fg="yellow")
button2=Button(window,text="Cancel", bg="Blue", fg="yellow")
button1.place(x=240, y=60)
button2.place(x=140,y=60)
button1.pack()   # TO MAKE IT VISIBLE 
button2.pack()   # TO MAKE IT VISIBLE
button1.bind("<Button>", mouseClick)
button2.bind("<Button>", mouseClick1)