from email.headerregistry import Address
from os import write
from tkinter import *

def save_functon():
    deliver_file = open("./deliveries.txt", "a")
    deliver_file.write("Depot :\n%s\n"%depot.get())
    deliver_file.write("Description : \n%s\n"%description.get())
    deliver_file.write("Address :\n%s\n"%address.get("1.0",END))
    deliver_file.close()
    #clear field
    depot.set("None")
    description.delete(END)
    address.delete("1.0",END)
    print("Details saved ")

depots = []
depots_file = open("./Depots.txt")
for line in depots_file:
    depots.append(line.rstrip())

print(depots)

#app create
app = Tk()
app.title("Head-ex deliveries")
app.geometry("650x500+100+200")

#app body
Label(app,text="Depot :",height=3).pack()
depot = StringVar()
depot.set("None")
#create option menu and read files
OptionMenu(app,depot,*depots).pack()
Label(app,text="Description :",height=3).pack()
description = Entry(app)
description.pack()
Label(app,text="Address :").pack()
address = Text(app,height=10,width=50)
address.pack()

Button(app,text = "Save",width=10,command=save_functon).pack()

app.mainloop()


