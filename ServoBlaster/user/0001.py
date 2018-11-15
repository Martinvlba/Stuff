import RPi.GPIO as GPIO
from time import sleep
from time import time
import os

GPIO.setmode(GPIO.BCM)

GPIO.setup(9,GPIO.OUT)
GPIO.setup(10,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)

Motor1 = GPIO.PWM(11, 50)
Motor1.start(0)

Echo = 26
Steer = 4

def forward(speed):
  GPIO.output(9,GPIO.HIGH)
  GPIO.output(10,GPIO.LOW)
  Motor1.ChangeDutyCycle(speed)
 

def backward(speed):
  GPIO.output(9,GPIO.LOW)
  GPIO.output(10,GPIO.HIGH)
  Motor1.ChangeDutyCycle(speed)
  

def left(speed):

  string = "echo 0=110 > /dev/servoblaster"
  os.system(string)
  sleep(1)
  GPIO.output(9,GPIO.LOW)
  GPIO.output(10,GPIO.HIGH)
  Motor1.ChangeDutyCycle(speed)


def right(speed):

  string = "echo 0=190 > /dev/servoblaster"
  os.system(string)
  sleep(1)
  GPIO.output(9,GPIO.LOW)
  GPIO.output(10,GPIO.HIGH)
  Motor1.ChangeDutyCycle(speed)


def stop():
  Motor1.ChangeDutyCycle(0)



def get_range():
  GPIO.setup(Echo,GPIO.OUT)
  GPIO.output(Echo, 0)
  sleep(0.1)
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
  return distance


while True:
  distance = get_range()
  if distance < 30:
    print "Distance %.1f " % distance
    stop()
    string = "echo 0=110 > /dev/servoblaster"
    os.system(string)
    sleep(1)
    disleft = get_range()
    print "Left %.1f " % disleft

    string = "echo 0=190 > /dev/servoblaster"
    os.system(string)
    sleep(1)
    disright = get_range()
    print "Right %.1f " % disright

    if disleft < disright:
      print "Turn right"
      left(100)
      sleep(2)
    else:
      print "Turn left"
      right(100)
      sleep(2)

    os.system("echo 0=150 > /dev/servoblaster")

  else:
    forward(80)
    print "Distance %.1f " % distance

  sleep(0.5)

GPIO.cleanup()
