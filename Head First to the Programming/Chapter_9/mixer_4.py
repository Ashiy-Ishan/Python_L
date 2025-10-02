from tkinter import *
import tkinter.messagebox as mg
import pygame.mixer

#import sound file
sound_file = "./50459_M_RED_Nephlimizer.wav"

#initalize app
app = Tk()
app.title("Mixer code magnet")
app.geometry("450x200+200+100")

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
#create checkbutton
Checkbutton(app,text="50459_M_RED_Nephlimizer.wav",
            command=flip_music,
            variable=flipped_value).pack()

#call windows manager protocol
app.protocol("WM_DELETE_WINDOW",shutdown_app)
app.mainloop()