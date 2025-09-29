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

#ui button
button_start = Button(text="Music start",width=10,command=sound_start)
button_start.pack(pady=5,padx= 5,side="left")
button_stop = Button(text="Music stop",width=10,command=sound_stop)
button_stop.pack(pady=5,padx= 5,side="right")

#call windows manager protocol
app.protocol("WM_DELETE_WINDOW",shutdown_app)
app.mainloop()