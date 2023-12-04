# This program will be run to initate total functionality of DORM-E 

#import Course_Correction.py as cc
#import Path_Selection.py as ps
#import sensors as ss
#import draft_pathfind.py as pf
import RPi.GPIO as GPIO          
from time import sleep
import board
import math
import adafruit_lis3mdl

i2c = board.I2C() # uses board.SCL and board.SDA
# i2c = board.STEMMA_I2C() # For using the built-in STEMMA QT connector on a microcontroller
sensor = adafruit_lis3mdl.LIS3MDL(i2c)


#import motor_controller_code_function.py as mc

# Pin setup and Constants
in1 = 24
in2 = 23
in3 = 17
in4 = 27
ena = 12
enb = 13

lSpeed = 75
rSpeed = 75

#Distance and Angle Conversion
meter=3
degree=1

#compass setup
i2c = board.I2C()


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

def forward():
    adjust_speed(75, 80)
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.HIGH)
    GPIO.output(in4,GPIO.LOW)


def backward(distance=1):
    adjust_speed(50,50)
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.HIGH)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.HIGH)

def rotate():
    adjust_speed(50, 50)
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.HIGH)

def adjust_speed(left, right):
    global lSpeed
    global rSpeed 
    lSpeed = left
    rSpeed = right
    p1.ChangeDutyCycle(lSpeed)
    p2.ChangeDutyCycle(rSpeed)


def stop_motors():
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.LOW)

def calculate_heading(x, y):
    heading = math.atan2(y, x)
    # Convert radians to degrees
    heading_degrees = math.degrees(heading)
    # Normalize heading to be between 0 and 360 degrees
    normalized_heading = (heading_degrees + 360) % 360
    return normalized_heading

if __name__ == "__main__":
    target = 163.28849548873222
    threshold_angle = 3
    consecutive_within_threshold = 0
    threshold_consecutive_readings = 1

    while True:
        mag_x, mag_y, mag_z = sensor.magnetic
        heading = calculate_heading(mag_x, mag_y)

        rotate()

        if abs(heading - target) <= threshold_angle:
            consecutive_within_threshold += 1
            if consecutive_within_threshold >= threshold_consecutive_readings:
                print("Reached the target heading within threshold.")
                stop_motors()
                break  # Exit the loop once the target heading is reached within the threshold for consecutive readings
        else:
            consecutive_within_threshold = 0  # Reset the counter if not consecutive within threshold
    stop_motors
    sleep(3)
    forward()
    sleep(5)
    stop_motors()

    target = 26.28528081645544
    threshold_angle = 3
    consecutive_within_threshold = 0
    threshold_consecutive_readings = 3

    while True:
        mag_x, mag_y, mag_z = sensor.magnetic
        heading = calculate_heading(mag_x, mag_y)

        rotate()

        if abs(heading - target) <= threshold_angle:
            consecutive_within_threshold += 1
            if consecutive_within_threshold >= threshold_consecutive_readings:
                print("Reached the target heading within threshold.")
                stop_motors()
                break  # Exit the loop once the target heading is reached within the threshold for consecutive readings
        else:
            consecutive_within_threshold = 0  # Reset the counter if not consecutive within threshold

    GPIO.cleanup


#translations
#61: 90
#89: 180
#13: 270
#12: 0