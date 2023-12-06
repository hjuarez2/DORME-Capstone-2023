# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

""" Display compass heading data five times per second """
import time
from math import atan2, degrees
import board
import adafruit_lis3mdl
from adafruit_lis3mdl import  Range, Rate

i2c = board.I2C()  # uses board.SCL and board.SDA
# i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller
sensor = adafruit_lis3mdl.LIS3MDL(i2c)

sensor.Rate = Rate.RATE_155_HZ
sensor.range = Range.RANGE_4_GAUSS


x_offfset= -16.11
y_offset = -14.28
z_offset = 32.02
degree_offset = 0

total_list=0
samples = 0

def vector_2_degrees(x, y):
    angle = degrees(atan2(y, x))
    angle -= degree_offset
    if angle < 0:
        angle += 360
    return angle


def get_heading(_sensor):
    magnet_x, magnet_y, _ = _sensor.magnetic
    magnet_x += x_offfset
    magnet_y +=y_offset
    return vector_2_degrees(magnet_x, magnet_y)


while True:
   # total_list+=get_heading(sensor)
    #samples+=1
    #print(total_list/samples)
    print("heading: {:.2f} degrees".format(get_heading(sensor)))
    time.sleep(0.5)