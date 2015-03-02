import RPi.GPIO as GPIO
import time

# set pin constants
wait_time = 1
led1 = 4
led2 = 17
led3 = 22
led4 = 10

# set up pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)
GPIO.setup(led3, GPIO.OUT)
GPIO.setup(led4, GPIO.OUT)

#turn off all leds
GPIO.output(led1, 0)
GPIO.output(led2, 0)
GPIO.output(led3, 0)
GPIO.output(led4, 0)

# alternate sequentially through leds
GPIO.output(led1, 1)
time.sleep(wait_time)
GPIO.output(led1, 0)
GPIO.output(led2, 1)
time.sleep(wait_time)
GPIO.output(led2, 0)
GPIO.output(led3, 1)
time.sleep(wait_time)
GPIO.output(led3, 0)
GPIO.output(led4, 1)
time.sleep(wait_time)
GPIO.output(led4, 0)

#reset all pins
GPIO.cleanup()