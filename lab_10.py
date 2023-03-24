import RPi.GPIO as GPIO
import datetime
import time
import sys
if len(sys.argv) > 1:
 run_time = sys.argv[1]
 if len(sys.argv) > 2:
  count_per_entry = sys.argv[2]
  if len(sys.argv) > 3:
   output_file_name = sys.argv[3]
   output_file_name = output_file_name + ".csv"
 


channel = 2
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

f = open(output_file_name,"w")
meta_data = ["CPM","Time Tags"]
import csv
f = open(output_file_name,"w",newline='')
writer = csv.writer(f)
writer.writerow(meta_data)

startTime=int(time.time())
iTime=startTime
count = 0
list_of_times = []
originalStart = int(time.time())

while iTime < (originalStart + int(run_time)):
 temp = GPIO.wait_for_edge(channel, GPIO.FALLING, timeout = 1000)
 if temp is None:
  print("Timeout")
 else:
  count = count + 1
  print(str(datetime.datetime.now()))
  #list_of_times.append(str(datetime.datetime.now()))
 iTime = int(time.time())
 if iTime > (startTime + int(count_per_entry)):
  data = [str(count),str(list_of_times)]
  writer.writerow(data)
  print("Counts in the last minute: " + str(count))
  count = 0
  list_of_times = []
  startTime = int(time.time())
 
print("Total Counts Since Last Minute:" + str(count))
f.close()
