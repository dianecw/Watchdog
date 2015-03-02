import RPi.GPIO as GPIO
import time
import os
import atexit

#initialize constants
led1 = 4
led2 = 17
led3 = 22
led4 = 10

#initialize slightly sketchier constants
routerIP = "192.168.0."
deviceDictionary = {
  "dianedroid":(2,led1),
  "dianePC":(3,led2),
  "ethanMac":(4,led3),
  "ethandroid":(5,led4)
}

#set up pins
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)
GPIO.setup(led3, GPIO.OUT)
GPIO.setup(led4, GPIO.OUT)

#turns off all leds
def turnOffLights():
  GPIO.output(led1, 0)
  GPIO.output(led2, 0)
  GPIO.output(led3, 0)
  GPIO.output(led4, 0)

#ping addresses, update LEDs
try:
  while(True):
    for device,info in deviceDictionary.items(): #info[0] is ip address, info[1] is led number
      fullAddress = routerIP + str(info[0])
      if os.system("ping -c 1 -w 1 " + fullAddress) == 0:
        print device + "is in the house."
        GPIO.output(info[1], 1)
      else:
        print device + "is not in the house."
        GPIO.output(info[1], 0)
    time.sleep(1)

except KeyboardInterrupt:
  turnOffLights()
  GPIO.cleanup()