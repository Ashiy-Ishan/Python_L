from tkinter import *
import pygame.mixer
sound = pygame.mixer
sound.init()

#load sound effects
sound_wrong = sound.Sound("./sound/wrong.wav")
sound_correct = sound.Sound("./sound/correct.wav")

#button click function
def button_correct():
    correct_count.set(correct_count.get()+1)
    sound_correct.play()

def button_wrong():
    wrong_count.set(wrong_count.get()+1)
    sound_wrong.play()

app = Tk()
app.title("TVN Question Program")
app.geometry('450x200+200+100')

#create variable that store things
correct_count = IntVar()
correct_count.set(0)
wrong_count= IntVar()
wrong_count.set(0)

#Left button
lb = Label(text="Click the buttons ",height=5)
lb.pack()
label_display = Label(app,textvariable=correct_count,height=3)
label_display.pack(side='left',padx=10,pady=10)
label_display = Label(app,textvariable=wrong_count,height=3)
label_display.pack(side='right',padx=10,pady=10)



#buttons
button_1 = Button(app,text="Correct",width=20 ,command=button_correct)
button_1.pack(side="left",padx=10,pady=10)
#right button
button_2 = Button(app, text="Wrong",width=20,command=button_wrong)
button_2.pack(side="right",padx=10,pady=10)
app.mainloop()



