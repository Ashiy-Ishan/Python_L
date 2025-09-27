from tkinter import *
app = Tk()
app.title("Lable test one")
app.geometry("350x200+100+100")

#lable creation
lb_1 = Label(app,text="This is first lable",height=3)
lb_1.pack()
num = IntVar()
num1 = IntVar()
num.set(1)
lb_2 = Label(app,textvariable=num,height=3)
lb_2.pack()
num1.set(100)
lb_3 = Label(app,textvariable=num1,height=3)
lb_3.pack()
app.mainloop()