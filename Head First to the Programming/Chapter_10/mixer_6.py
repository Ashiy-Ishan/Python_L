import pygame.mixer
from tkinter import *
from sound_panel_class import *


#create app
app = Tk()
mixer = pygame.mixer
mixer.init()
app.title("Separate song GUI")

panel_1 = SoundPanel(app, mixer, "songs/abcdefu.mp3")
panel_1.pack()
panel_2 = SoundPanel(app, mixer, "songs/Ugly_Heart.mp3")
panel_2.pack()

def shutdown():
    app.destroy()

app.protocol("WM_DELETE_WINDOW",shutdown)
app.mainloop()