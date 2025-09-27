from tkinter import *
import pygame.mixer
sound = pygame.mixer
sound.init()

#create variable that store things
correct_count = 0
wrong_count = 0
sound_wrong = sound.Sound("./sound/wrong.wav")
sound_correct = sound.Sound("./sound/correct.wav")

#button click function
def button_correct():
    global correct_count
    correct_count += 1
    sound_correct.play()

def button_wrong():
    global wrong_count
    wrong_count += 1
    sound_wrong.play()

app = Tk()
app.title("TVN Question Program")
app.geometry('450x200+200+100')
#Left button
button_1 = Button(app,text="Correct",width=20 ,command=button_correct)
button_1.pack(side="left",padx=10,pady=10)
#right button
button_2 = Button(app, text="Wrong",width=20,command=button_wrong)
button_2.pack(side="right",padx=10,pady=10)
app.mainloop()

print(f"\nCorrect count : {correct_count}\nWrong count : {wrong_count}")

