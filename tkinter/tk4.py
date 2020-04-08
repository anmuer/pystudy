# coding: UTF-8

from tkinter import *


# pack 布局

"""
root = Tk()

e = Entry(root)
e.pack(padx=10, pady=10)

e.delete(0, END)
e.insert(0, "default string...")

mainloop()
"""


# grid 布局

"""
root = Tk()
Label(root, text="作品：").grid(row=0, column=0)
Label(root, text="作者：").grid(row=1, column=0)

e1 = Entry(root)
e1.grid(row=0, column=1, padx=10, pady=5)
e2 = Entry(root)
e2.grid(row=1, column=1, padx=10, pady=5)

def show():
    print("作品：《%s》" % e1.get())
    print("作者：%s" % e2.get())

Button(root, text="获取信息", width=10, command=show)\
                    .grid(row=3, column=0, sticky=W, padx=10, pady=5)

Button(root, text="退出", width=10, command=root.quit)\
                    .grid(row=3, column=1, sticky=E, padx=10, pady=5)

mainloop()

"""

# 账号密码输入
"""
root = Tk()
Label(root, text="账号：").grid(row=0, column=0)
Label(root, text="密码：").grid(row=1, column=0)

user = StringVar()
pwd = StringVar()

# textvariable 可不用这个参数
e1 = Entry(root, textvariable=user) 
e1.grid(row=0, column=1, padx=10, pady=5)
e2 = Entry(root, textvariable=pwd, show="*")
e2.grid(row=1, column=1, padx=10, pady=5)

def show():
    print("账号：%s" % e1.get())
    print("密码：%s" % e2.get())

Button(root, text="获取信息", width=10, command=show)\
                    .grid(row=3, column=0, sticky=W, padx=10, pady=5)

Button(root, text="退出", width=10, command=root.quit)\
                    .grid(row=3, column=1, sticky=E, padx=10, pady=5)

mainloop()

"""

# 失焦验证 focusout validatecommand
"""
root = Tk()
v = StringVar()
def test():
    if e1.get() == "cc":
        print("right!")
        return True
    else:
        print("wrong!")
        e1.delete(0, END)
        return False
e1 = Entry(root, textvariable=v, validate="focusout", validatecommand=test)
e2 = Entry(root)
e1.pack(padx=10, pady=10)
e2.pack(padx=10, pady=10)
mainloop()
"""

# 验证参数
"""
root = Tk()
v = StringVar()
def test(content, reason, name):
    if content == "cc":
        print("Right!")
        print(content, reason, name)
        return True
    else:
        print("Wrong!")
        return False

testCMD = root.register(test)
e1 = Entry(root, textvariable=v, validate="focusout", \
                validatecommand=(testCMD,"%P","%v","%W"))
e2 = Entry(root)
e1.pack(padx=10,pady=10)
e2.pack(padx=10,pady=10)
mainloop()
"""
# 简易计算器

root = Tk()
frame = Frame(root)
frame.pack(padx=10,pady=10)
v1 = StringVar()
v2 = StringVar()
v3 = StringVar()

def test(content):
    return content.isdigit()

testCMD = root.register(test)
e1 = Entry(frame, textvariable=v1, validate="key",\
                validatecommand=(testCMD,"%P"))
e1.grid(row=0,column=0)
Label(frame, text="+").grid(row=0,column=1)
e2 = Entry(frame, textvariable=v2, validate="key",\
                validatecommand=(testCMD,"%P"))
e2.grid(row=0,column=2)
Label(frame, text="=").grid(row=0,column=3)
e3 = Entry(frame, textvariable=v3, state="readonly")
e3.grid(row=0,column=4)

def cal():
    result = int(e1.get())+int(e2.get())
    v3.set(str(result))
Button(frame, text="计算", command=cal).grid(row=1,column=2,pady=5)
mainloop()