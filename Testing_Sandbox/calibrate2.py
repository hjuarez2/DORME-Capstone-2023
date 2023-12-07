# SPDX-FileCopyrightText: 2023 Cedar Grove Maker Studios
# SPDX-License-Identifier: MIT

"""
'lis3mdl_calibrator.py' is a simple CircuitPython calibrator example for
the LIS3MDL magnetometer. The resultant offset values can be used to
compensate for 'hard iron' effects, static magnetic fields, or to orient
the sensor with the earth's magnetic field for use as a compass.

The calibrator measures the minimum and maximum values for each axis as
the sensor is moved. The values are captured over a fixed number of
samples. A middle-of-the-range calibration offset value is calculated
and reported after all samples are collected.

The sensor needs to be tumbled during the collection period in a manner
that exercises the entire range of each axis. A series of overlapping
figure-eight patterns is recommended.

This code was derived from the '9dof_calibration.py' Blinka code
authored by Melissa LeBlanc-Williams for the 'Adafruit SensorLab -
Magnetometer Calibration' learning guide (c)2020.
"""

import time
import busio
from adafruit_lis3mdl import LIS3MDL, Rate, Range
from math import atan2, degrees
import board
import adafruit_lis3mdl
import RPi.GPIO as GPIO          
from time import sleep
import board
import sys



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

total_list=0
samples = 0

def stop_motors():
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.LOW)

def adjust_speed(left, right):
    global lSpeed
    global rSpeed 
    lSpeed = left
    rSpeed = right
    p1.ChangeDutyCycle(lSpeed)
    p2.ChangeDutyCycle(rSpeed)
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.HIGH)
    GPIO.output(in4,GPIO.LOW)


SAMPLE_SIZE = 6000

i2c = busio.I2C(board.SCL, board.SDA)
magnetometer = LIS3MDL(i2c)
magnetometer.Rate = Rate.RATE_155_HZ
magnetometer.range = Range.RANGE_4_GAUSS

while True:
    print("=" * 40)
    print("LIS3MDL MAGNETOMETER CALIBRATION")
    print("  Tumble the sensor through a series of")
    print("  overlapping figure-eight patterns")
    print(f"  for approximately {SAMPLE_SIZE/100:.0f} seconds \n")

    print("  countdown to start:", end=" ")
    for i in range(5, -1, -1):
        print(i, end=" ")
        time.sleep(1)
    print("\n  MOVE the sensor...")
    print("  >     progress     <")
    print("  ", end="")

    # Initialize the min/max values
    mag_x, mag_y, mag_z = magnetometer.magnetic
    min_x = max_x = mag_x
    min_y = max_y = mag_y
    min_z = max_z = mag_z

    adjust_speed(25, 70)

    for i in range(SAMPLE_SIZE):
        # Capture the samples and show the progress
        if not i % (SAMPLE_SIZE / 20):
            print("*", end="")
        
        if (i>SAMPLE_SIZE/2):
            adjust_speed(70, 25)


        mag_x, mag_y, mag_z = magnetometer.magnetic

        min_x = min(min_x, mag_x)
        min_y = min(min_y, mag_y)
        min_z = min(min_z, mag_z)

        max_x = max(max_x, mag_x)
        max_y = max(max_y, mag_y)
        max_z = max(max_z, mag_z)

        time.sleep(0.01)

    

    # Calculate the middle of the min/max range
    offset_x = (max_x + min_x) / 2
    offset_y = (max_y + min_y) / 2
    offset_z = (max_z + min_z) / 2
    stop_motors()

    print(
        f"\n\n  Final Calibration: X:{offset_x:6.2f} Y:{offset_y:6.2f} Z:{offset_z:6.2f} uT\n"
    )

    GPIO.cleanup()
    sys.exit()