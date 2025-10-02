from tkinter import *
import tkinter.messagebox as mg
import pygame.mixer

#import sound file
sound_file = "./50459_M_RED_Nephlimizer.wav"

#initalize app
app = Tk()
app.title("Mixer code magnet")

#make sound file
mixer = pygame.mixer
mixer.init()
sound_track = mixer.Sound(sound_file)

#function making
def sound_start():
    sound_track.play(loops=-1)

def sound_stop():
    sound_track.stop()
#---------------------------------------------------------------------------------------------------------------
#shutdown function
def shutdown_app():
    mg.askokcancel("Shutdown Notice","Mixer window going to shutdown\nDo you want to quit ?")
    sound_track.stop()
    app.destroy()
#----------------------------------------------------------------------------------------------------------------

#flip box
flipped_value = IntVar()
#flip function
def flip_music():
    if flipped_value.get() == 1:
        sound_start()
    else:
        sound_stop()

def change_volume(v):
    sound_track.set_volume(volume_sound.get())
    print("Volume changed")
#initalize double variable
volume_sound = DoubleVar()

#create checkbutton
Checkbutton(app,text="50459_M_RED_Nephlimizer.wav",
            command=flip_music,
            variable=flipped_value).pack(side="left")

volume_scale = Scale(app,
                     variable=volume_sound,
                     from_=0.0,
                     to=1.0,
                     resolution=0.2,
                     command= change_volume,
                     label="Volume",
                     orient= "horizontal" )
volume_scale.pack(side="right")

#call windows manager protocol
app.protocol("WM_DELETE_WINDOW",shutdown_app)
app.mainloop()