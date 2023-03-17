# coding=utf-8
 
import RPi.GPIO as GPIO
import datetime
import time

def my_callback(channel):
    if GPIO.input(channel) == GPIO.HIGH:
        print('\n▼  at ' + str(datetime.datetime.now()))
    else:
        print('\n ▲ at ' + str(datetime.datetime.now()))
          
GPIO.setmode(GPIO.BCM)
GPIO.setup(6, GPIO.IN)
#PIO.add_event_detect(6, GPIO.BOTH, callback=my_callback)


channel = 2
start_time = int(time.time())
i = 0

while i < 10:
 GPIO.wait_for_edge(channel, GPIO.FALLING)
 print(int(time.time()))
 i = i + 1
