import pygame.mixer
sound =  pygame.mixer
sound.init()

def wait_finish(channel):
    while channel.get_busy():
        pass

s = sound.Sound("./sound/heartbeat.wav")
wait_finish(s.play())

s2 = sound.Sound("./sound/buzz.wav")
wait_finish(s2.play())

s3 = sound.Sound("./sound/ohno.wav")
wait_finish(s3.play())

s4 = sound.Sound("./sound/carhorn.wav")
wait_finish(s4.play())