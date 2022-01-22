import os
import vlc
import random

tunedirectory = "/alarm/wakeuptunes"
pathDelim = "/"

def getGPIO():
    f = open('/alarm/gpio','r')
    state = f.readline()
    f.close()
    return state

tunes = os.listdir(tunedirectory)
tuneInt = random.randint(0, (len(tunes)-1))
tune = tunes[tuneInt]
tunepath = tunedirectory + pathDelim + tune

p = vlc.MediaPlayer(tunepath)

p.play()

while True:
    terminate = getGPIO()
    if terminate == str(0):
        p.stop()
        break
    else:
        continue

f.close()