from tkinter import *


app = Tk()
app.title("GUI slider")
app.geometry("350x200+100+200")

def volume_change():
    print("Volume changed")
#initalize double variable
volume_sound = DoubleVar()
volume_scale = Scale(app,
                     variable=volume_sound,
                     from_=0.0,
                     to=1.0,
                     resolution=0.2,
                     command=volume_change,
                     label="Volume",
                     orient= "horizontal" )
volume_scale.pack()
app.mainloop()