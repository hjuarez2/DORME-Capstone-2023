# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

""" Display compass heading data five times per second """

from math import atan2, degrees
import board
import adafruit_lis3mdl
from adafruit_lis3mdl import  Range, Rate
import RPi.GPIO as GPIO          
from time import sleep
import board



i2c = board.I2C()  # uses board.SCL and board.SDA
# i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller
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

x_offfset= -6.18
y_offset = -15.63
z_offset = 38.71
degree_offset = -326.8828

total_list=0
samples = 0

def stop_motors():
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.LOW)

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

def adjust_speed(left, right):
    global lSpeed
    global rSpeed 
    lSpeed = left
    rSpeed = right
    p1.ChangeDutyCycle(lSpeed)
    p2.ChangeDutyCycle(rSpeed)

def vector_2_degrees(x, y):
    angle = degrees(atan2(y, x))
    if angle < 0:
        angle += 360
    return angle


def get_heading(_sensor):
    magnet_x, magnet_y, _ = _sensor.magnetic
    magnet_x += x_offfset
    magnet_y +=y_offset
    return vector_2_degrees(magnet_x, magnet_y)


while True:
    rotate(0)
   # total_list+=get_heading(sensor)
    #samples+=1
    #print(total_list/samples)
   # print("heading: {:.2f} degrees".format(get_heading(sensor)))
    sleep(1)

    rotate(180)
    sleep(1)