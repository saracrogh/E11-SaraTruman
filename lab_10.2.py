# coding=utf-8
 
import RPi.GPIO as GPIO
import datetime
import time

channel = 17
  
  
def my_callback(channel):
      print('\n▼  at ' + str(datetime.datetime.now()))
 
try:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(channel, GPIO.IN)
    GPIO.add_event_detect(channel, GPIO.FALLING, callback=my_callback)
 
finally:
    GPIO.cleanup()
 
while True:
  time.sleep(10)
  
print("Goodbye!")
