# coding: UTF-8
import tkinter as tk

class App:
    def __init__(self, master):
        frame = tk.Frame(master)
        # frame.pack()
        # frame.pack(side=tk.LEFT)
        frame.pack(side=tk.LEFT, padx=10, pady=10)
        
        self.hi_there = tk.Button(frame, text="打招呼", bg="red", fg="blue", command = self.say_hi)
        self.hi_there.pack()

    def say_hi(self):
        print('hello everyone, i am cc!')


root = tk.Tk()
app = App(root)
root.mainloop()     


# if __name__ == '__main__':
#     app = tk.Tk()
#     app.title("cc Demo")

#     theLabel = tk.Label(app,text='我的第二个窗口程序')
#     theLabel.pack()
    
#     app.mainloop()
