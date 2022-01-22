import os
import vlc
import random

tunedirectory = "/alarm/wakeuptunes"
pathDelim = "/"

tunes = os.listdir(tunedirectory)
print(tunes)
tuneInt = random.randint(0, (len(tunes)-1))
tune = tunes[tuneInt]
print(tune)
tunepath = tunedirectory + pathDelim + tune
print(tunepath)

p = vlc.MediaPlayer(tune)
p.play()

while True:
    terminate = getGPIO(pin)
    if terminate == 1:
        p.stop()
        break
    else:
        continue