# coding=utf-8
 
import RPi.GPIO as GPIO
import datetime
import time
channel = 2
start_time = int(time.time())
i = 0

while i < 1000:
 GPIO.wait_for_edge(channel, GPIO.FALLING)
 print(int(time.time())
 i = i + 1
