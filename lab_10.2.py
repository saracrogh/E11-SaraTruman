# coding=utf-8
 
import RPi.GPIO as GPIO
import datetime
import time

channel = 17

def my_callback(channel):
 print('\n▼  at ' + str(datetime.datetime.now()))
  
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)
GPIO.add_event_detect(channel, GPIO.FALLING, callback=my_callback)
 
while True:
 print("Running while loop")
 time.sleep(15)
  
print("Goodbye!")
