import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(19, GPIO.IN)

while True:
    GPIO.output(25, 0)
    if GPIO.input(19) != 1:
        GPIO.output(25, 1)
        time.sleep(1)
        GPIO.output(25, 0)
        time.sleep(1)