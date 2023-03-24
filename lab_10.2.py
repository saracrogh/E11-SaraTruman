# coding=utf-8
 
import RPi.GPIO as GPIO
import datetime
import time

channel = 6

def my_callback(channel):
 print('\rising at ' + str(datetime.datetime.now()))
  
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(channel, GPIO.RISING, callback=my_callback, bouncetime=1)
 
while True:
 print("Running while loop")
 time.sleep(15)
  
print("Goodbye!")
