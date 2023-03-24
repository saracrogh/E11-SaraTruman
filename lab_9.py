# coding=utf-8
 
import RPi.GPIO as GPIO
import datetime
import time


channel = 17
tests = 4
time_per_test = 30



GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

i = 0
while i < tests:
 i = i + 1
 start_time = int(time.time())
 end_time = start_time + time_per_test
 counts = 0

 while time.time() <= end_time:
  GPIO.wait_for_edge(channel, GPIO.FALLING, timeout = 5)
  if False == GPIO.input(channel):
   counts = counts + 1
   print(str(datetime.datetime.now()))
  time.sleep(0.005)
 
 print(counts)
 

 
 
