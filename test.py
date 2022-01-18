import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)

def getGPIO(pin):
        poll = GPIO.input(pin)
        time.sleep(0.05)
        poll = poll + GPIO.input(pin)
        if poll == 0:
                return 0
        else:
                return 1

while True:
        print(getGPIO(17))
