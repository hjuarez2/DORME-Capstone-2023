# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT
""" Display magnetometer data once per second """
import time
import board
import adafruit_lis3mdl
i2c = board.I2C() # uses board.SCL and board.SDA
# i2c = board.STEMMA_I2C() # For using the built-in STEMMA QT connector on a microcontroller
sensor = adafruit_lis3mdl.LIS3MDL(i2c)

compass_range = 360
    
    # Adjust the readings to fall within the range of 0 to 360 degrees
    

def magnetometer_to_compass(readout):
    # Define the range of values
    north_reading = 30.916822566500954
    south_reading = -2.943678748903833
    
    # Map the readings to compass degrees
    compass_range = north_reading - south_reading
    degrees = ((readout - south_reading) / compass_range) * 360
    
    # Normalize the degrees to [0, 360)
    normalized_degrees = degrees % 360
    
    return normalized_degrees


count = 0
total=0
while True:
 
 
 mag_x, mag_y, mag_z = sensor.magnetic
 #print("X:{0:10.2f}, Y:{1:10.2f}, Z:{2:10.2f} uT".format(mag_x, mag_y, mag_z))
 #print(mag_x)
 #count+=1
 #total+=mag_x
 #print("count: " + str(count)+ " avg: "+ str(total/count))
 #compass_degrees = (mag_x % compass_range + compass_range) % compass_range
 print(magnetometer_to_compass(mag_x)
 #print(str(mag_x) + " " + str(compass_degrees))
 print("")
 time.sleep(0.5)


#after 2000 ticks averaged, north is 30.916822566500954
#after 2000 ticks averaged, south is -2.943678748903833
#total degrees: 67.721002630809574, factor of 5.3159283828473400526702265028795

#to translate to degrees, -30.916822566500954 and times

#clockwise subtracts
#counterclockwise adds
