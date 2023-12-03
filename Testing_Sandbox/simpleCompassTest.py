# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT
""" Display magnetometer data once per second """
import time
import board
import math
import adafruit_lis3mdl
i2c = board.I2C() # uses board.SCL and board.SDA
# i2c = board.STEMMA_I2C() # For using the built-in STEMMA QT connector on a microcontroller
sensor = adafruit_lis3mdl.LIS3MDL(i2c)

count = 0
total=0

while True:
 
 
 mag_x, mag_y, mag_z = sensor.magnetic
 #print("X:{0:10.2f}, Y:{1:10.2f}, Z:{2:10.2f} uT".format(mag_x, mag_y, mag_z))
 #print(mag_x)
 #readings=[]
 #count+=1
 #total+=mag_x
 #print("count: " + str(count)+ " avg: "+ str(total/count))
 #print(str(mag_x)+ "   " + str(magnetometer_to_compass_degree(mag_x)))
 heading = math.atan2(mag_y, mag_x) * (180 / math.pi)
 heading-=30
 if heading < 0:
    heading += 360
 print(heading)
 time.sleep(0.5)
