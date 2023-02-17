#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time
import random
import sys
import csv


print (sys.argv)
start_time = int(time.time())
itime= start_time

run_time= int(sys.argv[0])
file_name = 'data.csv'

if(len (sys.argv)>2):
    file_name = sys.argv[2]

print(file_name)
file=open(file_name, "w", newline='')

wrtier = csv.writer(file)
meta_data= ["Time", "Data"]
writer.write:row(meta_data)

while itime < (start_time+run_time):
    itime= int(time.time())
    value = random.random()
    print(itime,value)
    time.sleep(1)


