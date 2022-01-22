import RPi.GPIO as GPIO
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

while True:
    interrupt = str(getGPIO(pin))
    f = open('gpio','w')
    f.write(interrupt)
    f.close()

    f = open('gpio','r')
    state = f.readline()
    f.close()
    print(state)