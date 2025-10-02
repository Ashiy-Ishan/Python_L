from tkinter import *


#app creation
app = Tk()
app.title("Check Box Test")
app.geometry("250x150+200+100")

def flip_it():
    if flipper.get()==1:
        print("Selected")
    else:
        print("Not selected")
flipper = IntVar()
Checkbutton(app,variable=flipper,
            command=flip_it,
            text="flip it ? ").pack()

app.mainloop()