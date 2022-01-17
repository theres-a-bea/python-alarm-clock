import keyboard
import os
import random
from pygame import mixer

mixer.init()
tunedirectory = "wakeuptunes"
pathDelim = "\\"

def isInputPressed():
    if keyboard.is_pressed('m'):
        return 1
    else:
        return 0

tunes = os.listdir(tunedirectory)
tuneInt = random.randint(0, (len(tunes)-1))
tune = tunedirectory + pathDelim + tunes[tuneInt]
tunepath = os.path.abspath(tune)

mixer.music.load(tunepath)

mixer.music.play()

while True:
    terminate = isInputPressed()
    if terminate == 1:
        mixer.music.stop()
        break
    else:
        continue