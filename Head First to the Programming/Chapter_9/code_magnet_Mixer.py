from tkinter import *
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
#ui button
button_start = Button(text="Music start",width=10,command=sound_start)
button_start.pack(pady=5,padx= 5,side="left")
button_stop = Button(text="Music stop",width=10,command=sound_stop)
button_stop.pack(pady=5,padx= 5,side="right")

app.mainloop()
