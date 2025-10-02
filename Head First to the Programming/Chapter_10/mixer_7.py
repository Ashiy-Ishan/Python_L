import pygame.mixer
from tkinter import *
from sound_panel_class import *
import os


#create app
app = Tk()
mixer = pygame.mixer
mixer.init()
app.title("Separate song GUI")
def shutdown():
    app.destroy()

try:
    flist = os.listdir("./songs/.")
    for fname in flist:
        if fname.endswith(".mp3"):
            panels = SoundPanel(app,mixer,fname)
            panels.pack()
except Exception as ex:
    print(ex)
    print("Try again ")
    app.protocol("WM_DELETE_WINDOW",shutdown)


app.protocol("WM_DELETE_WINDOW",shutdown)
app.mainloop()