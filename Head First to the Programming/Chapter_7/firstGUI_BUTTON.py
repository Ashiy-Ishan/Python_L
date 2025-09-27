from tkinter import *

#first test window creation
#crate app object
app = Tk()
app.title("First GUI window")
app.geometry('500x300+200+100')
button_1 = Button(app,text = "Left ",width=10)
button_1.pack(side = 'left',padx = 10,pady = 10)

button_1 = Button(app,text = "Right ",width=10)
button_1.pack(side = 'right',padx = 10,pady = 10)

button_1 = Button(app,text = "Top ",width=10)
button_1.pack(side = 'top',padx = 10,pady = 10)

button_1 = Button(app,text = "Bottom ",width=10)
button_1.pack(side= 'bottom',padx = 10,pady = 10)

app.mainloop()