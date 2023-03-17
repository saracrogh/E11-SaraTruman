# coding=utf-8
 
import RPi.GPIO as GPIO
import datetime
channel = 2
start_time = int(time.time())

while true:
 GPIO.wait_for_edge(channel, GPIO.FALLING)
 print(int(time.time())
