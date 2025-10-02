#sound controller
import pygame.mixer
from time import sleep

mixer = pygame.mixer
mixer.init()

sound = mixer.Sound("./50459_M_RED_Nephlimizer.wav")
sound.play(loops=-1)
sound.set_volume(0.9)
sleep(4)
sound.set_volume(0.1)
sleep(4)
sound.stop()
