# coding=utf-8
 
import RPi.GPIO as GPIO
import datetime
import time
start_time = int(time.time())

channel = 2
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

i = 0

while i < 10:
 GPIO.wait_for_edge(channel, GPIO.FALLING)
 print(str(datetime.datetime.now()))
 i = i + 1
 time.sleep(0.01)
