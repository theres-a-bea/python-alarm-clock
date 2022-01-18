import os
import pygame
import RPi.GPIO as GPIO
import time
import random

tunedirectory = "/alarm/wakeuptunes"
pathDelim = "/"
pin = 17

pygame.mixermixer.init()
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN)

def getGPIO(pin):
        poll = GPIO.input(pin)
        time.sleep(0.05)
        poll = poll + GPIO.input(pin)
        if poll == 0:
                return 0
        else:
                return 1

tunes = os.listdir(tunedirectory)
tuneInt = random.randint(0, (len(tunes)-1))
tune = tunedirectory + pathDelim + tunes[tuneInt]
tunepath = os.path.abspath(tune)

pygame.mixer.music.load(tunepath)

pygame.mixer.music.play()

while True:
    terminate = getGPIO(pin)
    if terminate == 1:
        pygame.mixer.music.stop()
        break
    else:
        continue