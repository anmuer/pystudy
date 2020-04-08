#coding: UTF-8
from tkinter import *

root = Tk()

"""
textLabel = Label(root, text="你不能打开, you can't open it")
textLabel.pack()

photo = PhotoImage(file = "/Users/cc/Desktop/cc/python/pystudy/tkinter/image/b.gif")
imageLabel = Label(root, image=photo)
imageLabel.pack()

photo2 = PhotoImage(file = "/Users/cc/Desktop/cc/python/pystudy/tkinter/image/c.gif")
theLabel = Label(root,
                 text="hello cc, welcome to learn python",
                 justify=LEFT,
                 image=photo2,
                 compound=CENTER,
                 font=("楷书",20),
                 fg="black")
theLabel.pack()
"""

frame1 = Frame(root)
frame2 = Frame(root)

var = StringVar()
var.set("can't open it")

textLabel = Label(frame1,
                  textvariable=var,
                  justify=LEFT)
textLabel.pack(side=LEFT)

photo = PhotoImage(file="/Users/cc/Desktop/cc/python/pystudy/tkinter/image/d.gif")
imgLabel = Label(frame1, image=photo)
imgLabel.pack(side=RIGHT)

def callback():
    var.set("no, you can't")
theButton = Button(frame2, text="no, you are wrong, i can do it", command=callback)
theButton.pack()

frame1.pack(padx=10,pady=10)
frame2.pack(padx=10,pady=10)

mainloop()