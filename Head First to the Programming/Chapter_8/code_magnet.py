from tkinter import *

#app create
app = Tk()
app.title("Head-ex deliveries")
app.geometry("650x500+100+200")

#app body
Label(app,text="Depot :",height=3).pack()
depot = Entry(app)
depot.pack()
Label(app,text="Description :",height=3).pack()
description = Entry(app)
description.pack()
Label(app,text="Address :").pack()
address = Text(app)
address.pack(pady=10)

Button(app,text = "Save",width=10).pack()

app.mainloop()


