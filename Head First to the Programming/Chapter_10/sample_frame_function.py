from tkinter import *

# Create the main window
app = Tk()
app.title("Frame Example")
app.geometry("300x150")

# 1. Create a Frame widget
# The frame is placed inside the main window 'app'
my_frame = Frame(app, borderwidth=2, relief="groove") # Added a border to see it
my_frame.pack(side="left", padx=10, pady=10) # Place the frame on the left

# 2. Put other widgets INSIDE the frame
# Notice they are created with 'my_frame' as their parent, not 'app'
label = Label(my_frame, text="This is inside the frame!")
label.pack()

button = Button(my_frame, text="Click Me")
button.pack()

# This label is NOT in the frame
other_label = Label(app, text="This is outside the frame.")
other_label.pack(side="right", padx=10)

app.mainloop()