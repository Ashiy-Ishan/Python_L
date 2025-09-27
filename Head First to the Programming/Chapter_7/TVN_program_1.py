from tkinter import *

app = Tk()
app.title("TVN Question Program")
app.geometry('500x350+200+100')
#Left button
button_1 = Button(app,text="1\nCorrect",width=20)
button_1.pack(side="left",padx=10,pady=10)
#right button
button_2 = Button(app, text="2\nWrong",width=20)
button_2.pack(side="right",padx=10,pady=10)
app.mainloop()

