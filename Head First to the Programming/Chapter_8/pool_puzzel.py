from tkinter import *

app = Tk()
app.title("Pool puzzel")
app.geometry("350x200+100+200")

#crate label
Label(app,text="Depot :",highlightcolor="red").pack()
option = StringVar()
option.set("None")
Radiobutton(app,text="Cambridge, MA",value="Cambridge, MA",variable=option).pack()
Radiobutton(app,text="Cambridge, MA",value="Cambridge, UK",variable=option).pack()
Radiobutton(app,text="Cambridge, MA",value="Cambridge, WA",variable=option).pack()
option.set("None")
app.mainloop()