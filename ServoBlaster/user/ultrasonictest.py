import RPi.GPIO as GPIO
from time import sleep
from time import time

GPIO.setmode(GPIO.BCM)

Echo = 26

while True:
  GPIO.setup(Echo,GPIO.OUT)
  GPIO.output(Echo, 0)

  sleep(0.1)

  print "Sending Trigger"

  GPIO.output(Echo,1)
  sleep(0.00001)
  GPIO.output(Echo,0)

  GPIO.setup(Echo,GPIO.IN)

  while GPIO.input(Echo) == 0:
    pass
  start = time()

  while GPIO.input(Echo) == 1:
    pass
  stop = time()

  elapsed = stop - start
  distance = elapsed * 17000
  print "Distance %.1f " % distance

  sleep(1)

GPIO.cleanup()