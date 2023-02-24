
import time
import random
import sys
import csv
import board
import busio
import adafruit_pm25
from digitalio import DigitalInOut, Direction, Pull
from adafruit_pm25.i2c import PM25_I2C
import adafruit_bme680
import board

print (sys.argv)
start_time = int(time.time())
itime= start_time
run_time= int(sys.argv[1])

file_name = 'outside_data.csv'
if(len(sys.argv)>2):
    file_name=sys.argv[2]
    
print(file_name)
file=open(file_name, "w", newline='')
writer = csv.writer(file)
meta_data= ["Time", "pm10_standard", "pm25_standard", "pm100_standard", "Temperature", "Gas", "Humidity","Pressure","Altitude"]
writer.writerow(meta_data)

reset_pin = None

# For use with Raspberry Pi/Linux:
import serial
uart = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=0.95)

# Connect to a PM2.5 sensor over UART
from adafruit_pm25.uart import PM25_UART
pm25 = PM25_UART(uart, reset_pin)

i2c = board.I2C()
bme680 = adafruit_bme680.Adafruit_BME680_I2C(i2c, debug=False)
bme680.sea_level_pressure = 1013.25

print("Found PM2.5 sensor, reading data...")


while itime < (start_time+run_time):
    time.sleep(1)
    itime = int (time.time())
    value = random.random()
    print(itime,value)
    timeCurrent = time.time()
    print(timeCurrent)
    
    try:
        aqdata = pm25.read()
        print(aqdata)
    except RuntimeError:
        print("Unable to read from sensor, retrying...")
        continue
    
    writer.writerow([itime, aqdata["pm10 standard"], aqdata["pm25 standard"], aqdata["pm100 standard"],bme680.temperature,bme680.gas,bme680.relative_humidity,bme680.pressure,bme680.altitude]) 
    

file.close()


