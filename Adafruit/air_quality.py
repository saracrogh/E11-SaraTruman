import time
import board
import busio
import adafruit_pm25
import csv
from digitalio import DigitalInOut, Direction, Pull
from adafruit_pm25.i2c import PM25_I2C
import adafruit_bme680

reset_pin = None

# For use with Raspberry Pi/Linux:
import serial
uart = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=0.25)

# Connect to a PM2.5 sensor over UART
from adafruit_pm25.uart import PM25_UART
pm25 = PM25_UART(uart, reset_pin)

i2c = board.I2C()
bme680 = adafruit_bme680.Adafruit_BME680_I2C(i2c, debug=False)
bme680.sea_level_pressure = 1013.25
temperature_offset = -5
timeElapsed = 0


print("Found PM2.5 sensor, reading data...")

f = open("Lab4Data.csv","w", newline='')
meta_data = ["Time", "pm10_standard", "pm25_standard", "pm100_standard"]
writer = csv.writer(f)
writer.writerow(meta_data)

for i in range(0,10):
    time.sleep(1)
    timeCurrent = time.time()
    print(timeCurrent)
    
    try:
        aqdata = pm25.read()
        print(aqdata)
    except RuntimeError:
        print("Unable to read from sensor, retrying...")
        continue
    
    writer.writerow([timeCurrent, aqdata["pm10 standard"], aqdata["pm25 standard"], aqdata["pm100 standard"],]) 

f.close()
