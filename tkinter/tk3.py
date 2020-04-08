# coding: UTF-8
from tkinter import *


"""
多选框 Checkbutton
"""

"""
root = Tk()
girls = ["嫦娥","西施","王昭君","貂蝉","杨玉环"]
v = []
for girl in girls:
    v.append(IntVar())
    b = Checkbutton(root, text=girl, variable=v[-1])
    b.pack(anchor=W)

    l=Label(root, textvariable=v[-1])
    l.pack()
mainloop()
"""

"""
单选框 Radiobutton
"""

root = Tk()

group = LabelFrame(root, text="最好的脚本语言是？", padx=5, pady=5)
group.pack(padx=10, pady=10)

langues = [('Python',1),('Perl',2),("Ruby",3),("Lua",4)]

v = IntVar()
v.set(1)

for lang, num in langues:
    b = Radiobutton(group, text=lang, variable=v, value=num, indicatoron=False)
    # b.pack(anchor=W)
    b.pack(fill=X)

mainloop()