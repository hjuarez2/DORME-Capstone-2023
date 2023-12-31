# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

""" Display compass heading data five times per second """

# Libraries
from math import atan2, degrees
import board
import adafruit_lis3mdl
from adafruit_lis3mdl import  Range, Rate
import RPi.GPIO as GPIO          
from time import sleep
import board

i2c = board.I2C()  # uses board.SCL and board.SDA
sensor = adafruit_lis3mdl.LIS3MDL(i2c)
sensor.Rate = Rate.RATE_155_HZ
sensor.range = Range.RANGE_4_GAUSS

# Pin setup and Constants
in1 = 24
in2 = 23
in3 = 17
in4 = 27
ena = 12
enb = 13

lSpeed = 75
rSpeed = 75
forwardStartHeading = 0

#GPIO initialization
GPIO.setmode(GPIO.BCM)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(ena,GPIO.OUT)
GPIO.setup(enb,GPIO.OUT)
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)
p1 = GPIO.PWM(ena,1000)
p2 = GPIO.PWM(enb,1000)
p1.start(25)
p2.start(25)

# Sensor calibration offsets
x_offset= -1.90
y_offset = -17.63
z_offset = 84.87
degree_offset = 17

total_list=0
samples = 0

# Stop motors
def stop_motors():
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.LOW)

# Rotate
def rotate(degrees):
    adjust_speed(40, 40)
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.HIGH)
    print("orienting to: "+ str(degrees))
    while (abs(get_heading(sensor)-degrees) > 1.5):
        continue
    print(get_heading(sensor))
    stop_motors()

# Adjust speed
def adjust_speed(left, right):
    global lSpeed
    global rSpeed 
    lSpeed = left
    rSpeed = right
    p1.ChangeDutyCycle(lSpeed)
    p2.ChangeDutyCycle(rSpeed)

# Convert vector components to degrees
def vector_2_degrees(x, y):
    angle = degrees(atan2(y, x))
    if angle < 0:
        angle += 360
    return angle

# Get the heading from the LIS3MDL sensor
def get_heading(_sensor):
    magnet_x, magnet_y, _ = _sensor.magnetic
    magnet_x += x_offset
    magnet_y +=y_offset
    return vector_2_degrees(magnet_x, magnet_y)

while True:
    rotate(0)
    sleep(1)

    rotate(180)
    sleep(1)