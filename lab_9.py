# coding=utf-8
 
import RPi.GPIO as GPIO
import datetime
import time


channel = 2
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

i = 0
while i < 10:
 i = i + 1
 start_time = int(time.time())
 end_time = start_time + 10
 counts = 0

 while time.time() <= end_time:
  GPIO.wait_for_edge(channel, GPIO.FALLING, timeout = 5)
  # print(str(datetime.datetime.now()))
  counts = counts + 1
  time.sleep(0.001)
 
 print(counts)
 

 
 
