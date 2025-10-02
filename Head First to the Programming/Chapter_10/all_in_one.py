import pygame.mixer
from tkinter import *
import tkinter.messagebox as mg
from create_gui import *

def create_gui_app(app,mixer,sound_file):
    sound_track = mixer.Sound(sound_file)
    # function making
    def sound_start():
        sound_track.play(loops=-1)
    def sound_stop():
        sound_track.stop()
    # flip box
    flipped_value = IntVar()
    # flip function
    def flip_music():
        if flipped_value.get() == 1:
            sound_start()
        else:
            sound_stop()
    def change_volume(v):
        sound_track.set_volume(volume_sound.get())
        print("Volume changed")
    #  double variable
    volume_sound = DoubleVar()
    # create checkbutton
    Checkbutton(app, text=f"{sound_file}",
                command=flip_music,
                variable=flipped_value).pack(side="left")
    volume_scale = Scale(app,
                         variable=volume_sound,
                         from_=0.0,
                         to=1.0,
                         resolution=0.2,
                         command=change_volume,
                         label="Volume",
                         orient="horizontal")
    volume_scale.pack(side="right")
    # call windows manager protocol
    return sound_file
import create_gui

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
