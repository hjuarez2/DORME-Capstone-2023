# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT
""" Display magnetometer data once per second """
import time
import board
import adafruit_lis3mdl
i2c = board.I2C() # uses board.SCL and board.SDA
# i2c = board.STEMMA_I2C() # For using the built-in STEMMA QT connector on a microcontroller
sensor = adafruit_lis3mdl.LIS3MDL(i2c)

count = 0
total=0


def magnetometer_to_compass_degree(reading):
    if reading >= 0:
        return 180 - (reading * (180 / 30.916822566500954))
    else:
        return abs(reading) * (180 / 2.943678748903833)




while True:
 
 
 mag_x, mag_y, mag_z = sensor.magnetic
 #print("X:{0:10.2f}, Y:{1:10.2f}, Z:{2:10.2f} uT".format(mag_x, mag_y, mag_z))
 #print(mag_x)
 readings=[]
 count+=1
 total+=mag_x
 #print("count: " + str(count)+ " avg: "+ str(total/count))
 #print(str(mag_x)+ "   " + str(magnetometer_to_compass_degree(mag_x)))
 readings.append(mag_x)
 print(max(readings) - min(readings))
 time.sleep(0.01)


#after 2000 ticks averaged, north is 30.916822566500954
#after 2000 ticks averaged, south is -2.943678748903833
#after 2000 ticks averaged, east is 10.669614989375537
#after 2000 ticks averaged, west is 12.901322549049544


#clockwise subtracts
#counterclockwise adds
