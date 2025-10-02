import pygame.mixer
from tkinter import *
import tkinter.messagebox as mg
from create_gui import *

app = Tk()
app.title("Sound panel")
mixer = pygame.mixer
mixer.init()

create_gui_app(app, mixer, "songs/abcdefu.mp3")
create_gui_app(app, mixer, "songs/Ugly_Heart.mp3")

# ---------------------------------------------------------------------------------------------------------------
# shutdown function
def shutdown_app():
    mg.askokcancel("Shutdown Notice", "Mixer window going to shutdown\nDo you want to quit ?")
    app.destroy()

    # ----------------------------------------------------------------------------------------------------------------
# call windows manager protocol
app.protocol("WM_DELETE_WINDOW", shutdown_app)
app.mainloop()
