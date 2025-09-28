from tkinter import *

app = Tk()
app.title("Head-ex deliveries")
app.geometry("550x300+100+200")

Label(app,text="Radio Buttons").pack()
Radiobutton(app,text = "Option 1").pack()
Radiobutton(app,text = "Option 2").pack()
Radiobutton(app,text = "Option 3").pack()

app.mainloop()

