import RPi.GPIO as GPIO
import os
import threading
import time

pin = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN)

def getGPIO(pin):
    poll = GPIO.input(pin)
    time.sleep(0.05)
    poll = poll + GPIO.input(pin)
    time.sleep(0.05)
    poll = poll + GPIO.input(pin)
    if poll == 0:
            return 0
    else:
            return 1

def startMusic():
    command = "runuser -l pi -c 'python3 /alarm/play.py'"
    os.system(command)

playThread = threading.Thread(target=startMusic)
playThread.start()

interrupt = str(1)

while interrupt == str(1):
    interrupt = str(getGPIO(pin))
    f = open('/alarm/gpio','w')
    f.write(interrupt)
    f.close()