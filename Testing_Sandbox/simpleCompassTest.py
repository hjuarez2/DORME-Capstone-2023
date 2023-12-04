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



def calculate_heading(x, y):
    heading = math.atan2(y, x)
    # Convert radians to degrees
    heading_degrees = math.degrees(heading)
    # Normalize heading to be between 0 and 360 degrees
    normalized_heading = (heading_degrees + 360) % 360
    return normalized_heading



while True:
 
 
 mag_x, mag_y, mag_z = sensor.magnetic
 

 
 #heading = math.atan2(mag_y, mag_x) * (180 / math.pi)
 #print("X:{0:10.2f}, Y:{1:10.2f}, Z:{2:10.2f} uT".format(mag_x, mag_y, mag_z))
 #print(mag_x)
 #readings=[]
 count+=1
 #total+=mag_x
 #print("count: " + str(count)+ " avg: "+ str(total/count))
 #print(str(mag_x)+ "   " + str(magnetometer_to_compass_degree(mag_x)))
 #heading_rad = math.atan2(mag_y, mag_x)
 #heading_deg = math.degrees(heading_rad)
 #if heading_deg < 0:
  #  heading_deg += 360
 #print(heading)

 # Replace these values with your magnetometer readings
 # magnetometer_x = 0.5
 # magnetometer_y = -0.866
 result_heading = calculate_heading(mag_x, mag_y)
 print("Heading:", result_heading)
 count = 0
 total=0
 time.sleep(0.5)


#after 2000 ticks averaged, north is 30.916822566500954
#after 2000 ticks averaged, south is -2.943678748903833
#after 2000 ticks averaged, east is 10.669614989375537
#after 2000 ticks averaged, west is 12.901322549049544


#clockwise subtracts
#counterclockwise adds
