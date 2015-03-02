import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(4, GPIO.OUT, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(17, GPIO.OUT, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(22, GPIO.OUT, pull_up_down = GPIO.PUD_DOWN)

while True:

	GPIO.output(2) = 1
	GPIO.output(4) = 1
	GPIO.output(17) = 1
	GPIO.output(22) = 1

GPIO.cleanup()